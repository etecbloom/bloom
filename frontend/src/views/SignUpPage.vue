<template>
  <div class="signup-page">
    <div class="content-layer">
      <SignUpCard />
    </div>
    <div class="logo">
      <img src="/logo_bloom.png" alt="Bloom Logo">
    </div>
  </div>
</template>

<script setup>
import SignUpCard from "../components/SignUpCard.vue"
</script>

<style scoped>
.signup-page {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: white;
  position: relative;
  padding: clamp(1rem, 3vw, 1.25rem);
  box-sizing: border-box;
}

.background-container {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  z-index: 1;
}

.content-layer {
  position: relative;
  z-index: 10;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.logo {
  position: absolute;
  top: clamp(1rem, 3vw, 1.25rem);
  left: clamp(1rem, 3vw, 1.5rem);
  z-index: 20;
}

.logo img {
  width: clamp(90px, 12vw, 140px);
  height: auto;
  display: block;
  transition: transform 0.3s ease;
}

.logo img:hover {
  transform: scale(1.05);
}

@media (max-width: 768px) {
  .signup-page {
    padding: 1rem;
    align-items: flex-start;
    padding-top: clamp(70px, 12vw, 80px);
  }
  
  .logo {
    top: 1rem;
    left: 1rem;
  }
  
  .logo img {
    width: 120px;
  }
}

@media (max-width: 480px) {
  .signup-page {
    padding: 0.75rem;
    padding-top: 60px;
  }
  
  .logo {
    top: 0.75rem;
    left: 0.75rem;
  }
  
  .logo img {
    width: 100px;
  }
}

@media (min-width: 1200px) {
  .signup-page {
    padding: 2rem;
  }
}

@media (max-width: 768px) and (max-height: 500px) {
  .signup-page {
    min-height: auto;
    padding-top: 70px;
    padding-bottom: 1rem;
  }
}
</style>