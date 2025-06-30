<!-- <template>
  <div class="stat-card">
    <div class="stat-value" :class="colorClass">{{ value }}</div>
    <div class="stat-label">{{ label }}</div>
  </div>
</template>

<script>
export default {
  props: ['value', 'label'],
  computed: {
    colorClass() {
      const cleanVal = parseFloat(this.value); // 提取数值部分

      if (this.label.includes('准确率')) {
        if (cleanVal >= 95) return 'green-gradient';
        else if (cleanVal >= 85) return 'orange-gradient';
        else return 'red-gradient';
      }

      if (this.label.includes('时间')) {
        if (cleanVal <= 20) return 'green-gradient';
        else if (cleanVal <= 50) return 'orange-gradient';
        else return 'red-gradient';
      }

      if (this.label.includes('FPS')) {
        if (cleanVal >= 60) return 'green-gradient';
        else if (cleanVal >= 30) return 'orange-gradient';
        else return 'red-gradient';
      }

      if (this.label.includes('分辨率')) {
        if (this.value.includes('4K')) return 'green-gradient';
        else if (this.value.includes('1080')) return 'orange-gradient';
        else return 'red-gradient';
      }

      return 'default-gradient';
    }
  }
}
</script>

<style scoped>
.stat-card {
  background: rgba(255, 255, 255, 0.05);
  border-radius: 16px;
  padding: 1.5rem;
  text-align: center;
  border: 1px solid rgba(108, 92, 231, 0.2);
  transition: all 0.3s;
}

.stat-card:hover {
  transform: translateY(-5px);
  background: rgba(255, 255, 255, 0.08);
  box-shadow: 0 8px 20px rgba(76, 194, 255, 0.1);
}

.stat-value {
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.stat-label {
  font-size: 1rem;
  font-weight: 500;
  background: linear-gradient(135deg, #b0a8e3, #e0e0e0);
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  opacity: 0.85;
}

/* 颜色渐变类（仅用于 text） */
.green-gradient {
  background: linear-gradient(135deg, #2ecc71, #27ae60);
}

.orange-gradient {
  background: linear-gradient(135deg, #f39c12, #e67e22);
}

.red-gradient {
  background: linear-gradient(135deg, #e74c3c, #c0392b);
}

.default-gradient {
  background: linear-gradient(135deg, #999999, #666666);
}
</style> -->
