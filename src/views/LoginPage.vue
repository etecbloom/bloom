<template>
  <div class="login-page">
   
    <div class="logo">
      <img src="/logo_bloom.png" alt="Bloom Logo">
    </div>

    <h1 class="welcome-title">Bem-vindo de volta!</h1>

    <LoginCard class="centered-login-card" />
  </div>
</template>

<script setup>
import LoginCard from '../components/LoginCard.vue';
</script>

<style scoped>
.login-page {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;

  background-color: white; 
  position: relative;

  padding-top: 80px; 
}

.logo {
  position: absolute; 
  top: 10px;
  left: 15px;
  z-index: 20;
}

.logo img {
  width: clamp(120px, 12vw, 140px);
  height: auto;
  display: block;
  transition: transform 0.3s ease;
}

.logo img:hover {
  transform: scale(1.05);
}

.welcome-title {
  font-family: 'Montserrat', sans-serif; 
  color: #333;
  margin-bottom: 30px;
  z-index: 10; 
  font-size: 1.8rem;
  text-align: center;
}

.centered-login-card {
  z-index: 10;
  margin-bottom: 40px; 
}

@media (max-width: 600px) {
  .welcome-title {
    font-size: 1.5rem;
    margin-bottom: 20px;
  }

  .logo {
    top: 1rem;
    left: 1rem;
  }
  
  .logo img {
    width: 120px;
  }
}
</style>