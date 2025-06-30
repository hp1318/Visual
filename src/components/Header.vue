<template>
  <section class="header-wrapper" :class="{ enter: animateTitle }">
    <h1 class="title-row">
      <span class="gradient-text">深度视觉分析平台</span>
    </h1>
    <p class="tagline">Vision Depth Estimation System</p>
    <p class="author-text">作者: 王森 & 霍鹏</p>
    <p class="intro-text">基于视觉大模型技术，为图像和视频提供精准的深度估计能力。基于深度学习算法，实现三维场景重建，适用于自动驾驶、机器人导航、AR/VR等多种应用场景。</p>

    <div class="feature-list">
      <FeatureCard 
        v-for="(feature, index) in features" 
        :key="index"
        :icon="feature.icon"
        :title="feature.title"
      />
    </div>
  </section>
</template>

<script>
import { ref, onMounted } from 'vue';
import FeatureCard from './FeatureCard.vue';

export default {
  components: { FeatureCard },
  setup() {
    const animateTitle = ref(false);
    
    onMounted(() => {
      setTimeout(() => (animateTitle.value = true), 500);
    });
    
    const features = [
      { icon: 'fas fa-bullseye', title: '高精度' },
      { icon: 'fas fa-bolt', title: '实时性' },
      { icon: 'fas fa-shield-alt', title: '鲁棒性' },
      { icon: 'fas fa-expand', title: '多尺度' },
      { icon: 'fas fa-sync-alt', title: '自适应' }
    ];
    
    return {
      animateTitle,
      features
    };
  }
}
</script>

<style scoped>
.header-wrapper {
  text-align: center;
  margin: 2rem auto 3rem;
  padding: 2rem 1rem;
  max-width: 1200px;
  opacity: 0;
  transform: translateY(-20px);
  transition: opacity 1s ease, transform 1s ease;
}

.header-wrapper.enter {
  opacity: 1;
  transform: translateY(0);
}

.title-row {
  display: inline-block;
  white-space: nowrap;
  font-size: 4rem;
  background: linear-gradient(135deg, var(--primary), var(--accent));
  background-clip: text;
  -webkit-text-fill-color: transparent;
  margin: 0;
  letter-spacing: 1px;
  text-shadow: 0 4px 20px rgba(76, 194, 255, 0.3);
  font-weight: 700;
}

.tagline {
  margin-top: 0.8rem;
  font-size: 1.3rem;
  color: #6c5ce7;
  font-weight: 700;
}

.intro-text {
  margin: 1.5rem auto 0;
  font-size: 1.1rem;
  color: #aaa;
  max-width: 700px;
  line-height: 1.7;
  font-weight: 300;
}

.author-text {
  margin-top: 1rem;
  font-size: 1.1rem;
  color: #6c5ce7;
  font-weight: 500;
}

.feature-list {
  display: flex;
  justify-content: center;
  gap: 2rem;
  margin-top: 2.5rem;
  flex-wrap: wrap;
}

@media (max-width: 900px) {
  .title-row {
    font-size: 3rem;
  }
  
  .tagline {
    font-size: 1.1rem;
  }
}

@media (max-width: 600px) {
  .title-row {
    font-size: 2.2rem;
  }
  
  .tagline {
    font-size: 1rem;
  }
}
</style>