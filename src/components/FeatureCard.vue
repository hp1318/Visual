<template>
  <div class="feature-item">
    <i :class="icon"></i>
    <p>{{ title }}</p>
  </div>
</template>

<script>
export default {
  props: ['icon', 'title']
}
</script>

<style scoped>
.feature-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 1.5rem;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 16px;
  width: 150px;
  transition: all 0.3s;
  backdrop-filter: blur(5px);
  border: 1px solid rgba(108, 92, 231, 0.2);
}

.feature-item:hover {
  transform: translateY(-8px);
  background: rgba(255, 255, 255, 0.1);
  box-shadow: 0 10px 25px rgba(76, 194, 255, 0.15);
}

.feature-item i {
  font-size: 2.5rem;
  margin-bottom: 1rem;
  color: var(--primary);
  background: linear-gradient(135deg, var(--primary), var(--accent));
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.feature-item p {
  margin: 0;
  font-size: 1rem;
  color: #eee;
  font-weight: 500;
}
</style>