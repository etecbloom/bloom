<template>
  <button :type="type" class="auth-button">
    <span class="button-text">{{ text }}</span>
  </button>
</template>

<script setup>
defineProps({
  text: String,
  type: {
    type: String,
    default: 'button'
  }
})
</script>

<style scoped>
.auth-button {
  width: 100%;
  max-width: 400px;
  padding: 16px 24px;
  background: linear-gradient(135deg, #c09dc9, #a87db3);
  border: none;
  border-radius: 12px;
  color: white;
  font-family: 'Poppins', sans-serif;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  margin-top: 10px;
  box-shadow: 0 4px 15px rgba(168, 125, 179, 0.3);
}

.auth-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(168, 125, 179, 0.4);
  background: linear-gradient(135deg, #a87db3, #9665a3);
}

.auth-button:active {
  transform: translateY(0);
}

@media (max-width: 768px) {
  .auth-button {
    padding: 14px 20px;
    font-size: 15px;
  }
}

@media (max-width: 480px) {
  .auth-button {
    padding: 12px 18px;
    font-size: 14px;
  }
}
</style>