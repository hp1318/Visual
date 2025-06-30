<template>
  <div class="card-wrapper">
    <nav class="tab-nav">
      <button
        class="tab-btn"
        :class="{ active: activeTab === 'image' }"
        @click="activeTab = 'image'"
      >
        <i class="fas fa-camera"></i> 图像深度估计
      </button>
      <button
        class="tab-btn"
        :class="{ active: activeTab === 'video' }"
        @click="activeTab = 'video'"
      >
        <i class="fas fa-video"></i> 视频流分析
      </button>
      <!-- <button
        class="tab-btn"
        :class="{ active: activeTab === 'realtime' }"
        @click="activeTab = 'realtime'"
      >
        <i class="fas fa-satellite-dish"></i> 实时三维重建
      </button> -->
    </nav>

    <hr class="divider" />

    <section class="panel">
      <div class="demo-container">
        <div class="input-area">
          <h3 class="area-title"><i class="fas fa-upload"></i> 输入图像</h3>
          <PreviewBox 
            type="input"
            :image="inputImage"
            title="请上传图像进行深度估计分析"
            description="支持格式: JPG, PNG, BMP"
            buttonText="上传图像"
            icon="fas fa-cloud-upload-alt"
            buttonIcon="fas fa-upload"
            @buttonClick="triggerFileInput"
          />
          <!-- 隐藏的文件选择框 -->
          <input
            ref="fileInput"
            type="file"
            accept="image/*"
            style="display: none"
            @change="uploadImage"
          />
        </div>
        
        <div class="output-area">
          <h3 class="area-title"><i class="fas fa-project-diagram"></i> 深度图输出</h3>
          <PreviewBox 
            type="output"
            :image="outputImage"
            title="深度分析结果将在此处显示"
            description="包含深度图、点云与3D模型"
            buttonText="开始分析"
            icon="fas fa-wave-square"
            buttonIcon="fas fa-cogs"
            :buttonDisabled="!inputImage"
            @buttonClick="processImage"
          />
        </div>
      </div>
    </section>
    
    <!-- <div class="stats-container">
      <StatsCard 
        v-for="(stat, index) in stats"
        :key="index"
        :value="stat.value"
        :label="stat.label"
      />
    </div> -->
  </div>
</template>

<script>
import { ref } from 'vue';
import PreviewBox from './PreviewBox.vue';
// import StatsCard from './StatsCard.vue';

export default {
  components: { PreviewBox, /*StatsCard*/ },
  setup() {
    const activeTab = ref('image');
    const inputImage = ref('');
    const outputImage = ref('');
    const fileInput = ref(null);
    const uploadedFile = ref(null);
    
    // const stats = [
    //   { value: '98.7%', label: '深度估计准确率' },
    //   { value: '24ms', label: '单帧处理时间' },
    //   { value: '4K', label: '最大分辨率支持' },
    //   { value: '60FPS', label: '实时处理性能' }
    // ];

    function triggerFileInput() {
      fileInput.value && fileInput.value.click();
    }
    
    function uploadImage(event) {
      const file = event.target.files[0];
      if (file) {
        uploadedFile.value = file;
        const reader = new FileReader();
        reader.onload = (e) => {
          inputImage.value = e.target.result;
        };
        reader.readAsDataURL(file);
      }
    }

    async function processImage() {
      if (!inputImage.value) return;

      const formData = new FormData();
      formData.append('image', uploadedFile.value);

      try {
        const response = await fetch('http://localhost:5000/estimate_depth', {
          method: 'POST',
          body: formData
        });
        
        const result = await response.json();
        if (result.depth_estimate) {
          outputImage.value = 'data:image/jpeg;base64,' + result.depth_estimate;
        } else {
          alert('后端未返回预期数据');
        }
      } catch (err) {
        console.error('分析失败:', err);
        alert('请求出错，请确认后端运行中并允许跨域访问');
      }
      }
    
    return {
      activeTab,
      inputImage,
      outputImage,
      fileInput,
      triggerFileInput,
      uploadImage,
      processImage
    };
  }
}
</script>

<style scoped>
.card-wrapper {
  position: relative;
  max-width: 1200px;
  margin: 0 auto;
  padding: 2.5rem;
  background: var(--card-bg);
  backdrop-filter: blur(14px);
  border-radius: 24px;
  border: 1px solid var(--card-border);
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.6);
  z-index: 10;
}

.card-wrapper::before {
  content: '';
  position: absolute;
  top: -2px;
  left: -2px;
  right: -2px;
  bottom: -2px;
  border-radius: 26px;
  background: linear-gradient(135deg, var(--secondary), var(--primary));
  z-index: -1;
}

.divider {
  border: none;
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
  margin: 1.5rem 0;
}

.tab-nav {
  display: flex;
  justify-content: center;
  gap: 1.5rem;
  margin-bottom: 1rem;
}

.tab-btn {
  padding: 1rem 2.5rem;
  border: none;
  border-radius: 16px;
  cursor: pointer;
  background: rgba(255, 255, 255, 0.1);
  color: #eee;
  font-size: 1.1rem;
  font-weight: 500;
  transition: all 0.3s;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.tab-btn:hover {
  transform: translateY(-3px);
  background: rgba(255, 255, 255, 0.15);
  box-shadow: 0 5px 15px rgba(76, 194, 255, 0.2);
}

.tab-btn.active {
  background: linear-gradient(135deg, var(--secondary), var(--primary));
  color: #fff;
  box-shadow: 0 6px 20px rgba(108, 92, 231, 0.6);
}

.panel {
  display: flex;
  justify-content: center;
  padding: 1.5rem 0;
  min-height: 450px;
}

.demo-container {
  display: flex;
  gap: 2rem;
  width: 100%;
  max-width: 1000px;
}

.input-area, .output-area {
  flex: 1;
  display: flex;
  flex-direction: column;
}

.area-title {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 1rem;
  font-size: 1.2rem;
  font-weight: 500;
  color: var(--primary);
}

/* .stats-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
  margin-top: 2rem;
} */

@media (max-width: 900px) {
  .card-wrapper {
    padding: 1.5rem;
  }
  
  .tab-btn {
    padding: 0.8rem 1.5rem;
    font-size: 1rem;
  }
  
  .feature-item {
    width: 130px;
    padding: 1rem;
  }
}

@media (max-width: 600px) {
  .feature-item {
    width: 100px;
  }
}
</style>