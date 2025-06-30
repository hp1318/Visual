<template>
  <div class="depth-ui">
    <div class="bg-container">
      <div class="bg-particles"></div>
      <div class="bg-gradient"></div>
      <div class="floating-element float-1"></div>
      <div class="floating-element float-2"></div>
    </div>

    <Header />
    <MainCard />
    
    <footer class="app-footer">
      <p>© 2025 视觉检测与深度学习 | 基于视觉大模型的深度估计 | H.P. & W.S</p>
    </footer>
  </div>
</template>

<script>
import Header from './components/Header.vue'
import MainCard from './components/MainCard.vue'

export default {
  components: { Header, MainCard }
}
</script>

<style scoped>
.depth-ui {
  position: relative;
  min-height: 100vh;
  overflow: hidden;
  max-width: 1400px;
  margin: 0 auto;
  padding: 20px;
}

.bg-container {
  position: absolute;
  inset: 0;
  overflow: hidden;
  z-index: -1;
}

.app-footer {
  text-align: center;
  padding: 2rem;
  margin-top: 3rem;
  color: #aaa;
  font-size: 0.9rem;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  max-width: 1200px;
  margin-left: auto;
  margin-right: auto;
}

@media (max-width: 600px) {
  .depth-ui {
    padding: 1rem;
  }
}
</style>