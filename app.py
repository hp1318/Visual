from flask import Flask, request, jsonify
from flask_cors import CORS
import torch
import numpy as np
from torch.autograd import Variable
from skimage.transform import resize
from newcrfs.utils import post_process_depth, flip_lr
from newcrfs.networks.NewCRFDepth import NewCRFDepth
from scipy import ndimage
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO
import base64
import argparse

app = Flask(__name__)
CORS(app)

# 模拟 argparse.Namespace 的参数
class Args:
    model_name = 'newcrfs'
    encoder = 'large07'
    max_depth = 10
    checkpoint_path = 'model_nyu.ckpt'
    input_height = 480
    input_width = 640
    dataset = 'nyu'
    crop = 'non'
    mode = 'test'
    video = ''

args = Args()

height_rgb, width_rgb = args.input_height, args.input_width
height_depth, width_depth = height_rgb, width_rgb

# 加载模型
def load_model():
    model = NewCRFDepth(version=args.encoder, inv_depth=False, max_depth=args.max_depth)
    model = torch.nn.DataParallel(model)
    checkpoint = torch.load(args.checkpoint_path)
    model.load_state_dict(checkpoint['model'])
    model.eval()
    model.cuda()
    return model

model = load_model()

@app.route('/estimate_depth', methods=['POST'])
def estimate_depth():
    file = request.files['image']
    image = Image.open(BytesIO(file.read())).convert('RGB')
    image = image.resize((width_rgb, height_rgb))
    rgb = np.array(image).astype(np.float32)

    # 归一化处理（与 demo.py 相同）
    rgb[:, :, 0] = (rgb[:, :, 0] - 123.68) * 0.017
    rgb[:, :, 1] = (rgb[:, :, 1] - 116.78) * 0.017
    rgb[:, :, 2] = (rgb[:, :, 2] - 103.94) * 0.017

    if args.crop == 'kbcrop':
        top_margin = int(height_rgb - 352)
        left_margin = int((width_rgb - 1216) / 2)
        rgb = rgb[top_margin:top_margin + 352, left_margin:left_margin + 1216]
    elif args.crop == 'edge':
        rgb = rgb[32:-32, 32:-32]

    # 转换为 tensor
    input_tensor = np.transpose(rgb[np.newaxis, :, :, :], (0, 3, 1, 2))
    image_tensor = Variable(torch.from_numpy(input_tensor)).cuda()

    with torch.no_grad():
        depth = model(image_tensor)
        image_flipped = flip_lr(image_tensor)
        depth_flipped = model(image_flipped)
        depth = post_process_depth(depth, depth_flipped)

    depth_np = depth[0].cpu().squeeze().numpy() / args.max_depth

    # 如果 crop，需要放回原图大小
    if args.crop == 'kbcrop':
        full_depth = np.zeros((height_rgb, width_rgb), dtype=np.float32)
        full_depth[top_margin:top_margin + 352, left_margin:left_margin + 1216] = depth_np
        depth_np = full_depth
    elif args.crop == 'edge':
        full_depth = np.zeros((height_rgb, width_rgb), dtype=np.float32)
        full_depth[32:-32, 32:-32] = depth_np
        depth_np = full_depth

    # 映射为彩色深度图
    colored_depth = (plt.get_cmap('Greys')(np.log10(depth_np * args.max_depth + 1e-8))[:, :, :3] * 255).astype('uint8')

    # 转为 base64 字符串
    output_image = Image.fromarray(colored_depth)
    buffered = BytesIO()
    output_image.save(buffered, format="JPEG")
    img_bytes = buffered.getvalue()
    img_base64 = base64.b64encode(img_bytes).decode('utf-8')

    return jsonify({'depth_estimate': img_base64})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
