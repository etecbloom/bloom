<template>
  <div class="login-card">
    <LoginForm />
  </div>
</template>

<script setup>
import LoginForm from './LoginForm.vue';
</script>

<style scoped>
.login-card {
  background-color: #F6F1FF; 
  border-radius: 20px;
  box-shadow: 0 10px 30px rgba(168, 125, 179, 0.2), 
              0 5px 15px rgba(0, 0, 0, 0.05);
  padding: 40px 30px;
  width: 100%;
  max-width: 400px;
  box-sizing: border-box;
}

@media (max-width: 600px) {
  .login-card {
    margin: 0 20px; 
    padding: 30px 20px;
  }
}
</style>