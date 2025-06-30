<template>
  <div class="preview-box">
    <img v-if="image" :src="image" :alt="title">
    <div v-else>
      <i :class="icon" :style="{ fontSize: '3rem', color: type === 'input' ? '#4bc2ff' : '#a66efa', marginBottom: '1rem' }"></i>
      <p class="placeholder-text">{{ title }}</p>
      <p class="placeholder-text">{{ description }}</p>
      <button 
        class="upload-btn" 
        @click="$emit('buttonClick')"
        :disabled="buttonDisabled"
      >
        <i :class="buttonIcon"></i> {{ buttonText }}
      </button>
    </div>
  </div>
</template>

<script>
export default {
  props: ['type', 'image', 'title', 'description', 'buttonText', 'icon', 'buttonIcon', 'buttonDisabled'],
  emits: ['buttonClick']
}
</script>

<style scoped>
.preview-box {
  flex: 1;
  background: rgba(0, 0, 0, 0.3);
  border-radius: 16px;
  border: 2px dashed rgba(255, 255, 255, 0.2);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 2rem;
  transition: all 0.3s;
  overflow: hidden;
  position: relative;
}

.preview-box:hover {
  border-color: var(--primary);
}

.preview-box img {
  max-width: 100%;
  max-height: 300px;
  border-radius: 12px;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.4);
}

.placeholder-text {
  text-align: center;
  color: #aaa;
  margin-top: 1rem;
  font-size: 0.9rem;
}

.upload-btn {
  margin-top: 1.5rem;
  padding: 0.8rem 2rem;
  background: linear-gradient(135deg, var(--secondary), var(--primary));
  color: white;
  border: none;
  border-radius: 12px;
  font-size: 1rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.upload-btn:hover {
  transform: translateY(-3px);
  box-shadow: 0 6px 18px rgba(108, 92, 231, 0.5);
}

.upload-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}
</style>