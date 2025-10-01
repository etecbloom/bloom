<template>
  <nav class="navbar">
    <div class="navbar-logo">
      <img src="/logo_bloom.png" alt="Bloom" class="logo-image">
    </div>
    <ul :class="['navbar-links', { 'active': isMobileMenuOpen }]">
      <li><a href="/details">Visão geral</a></li>
      <li><a href="#">Contate-nos</a></li>
      <li><a href="#">Recursos</a></li>
    </ul>
    <div class="hamburger" @click="toggleMobileMenu">
      <span class="bar"></span>
      <span class="bar"></span>
      <span class="bar"></span>
    </div>
  </nav>
</template>

<script setup>
import { ref } from 'vue'

const isMobileMenuOpen = ref(false)

const toggleMobileMenu = () => {
  isMobileMenuOpen.value = !isMobileMenuOpen.value
}
</script>

<style scoped>
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #FFFFFF;
  width: 100%;
  min-height: 80px;
  padding: 0 2rem;
  box-sizing: border-box;
  border-bottom: 1px solid #f0f0f0;
}

.navbar-logo {
  flex: 0 0 auto;
}

.logo-image {
  height: 40px;
  width: auto;
  display: block;
}

.navbar-links {
  list-style: none;
  display: flex;
  margin: 0;
  padding: 0;
  gap: 3rem;
}

.navbar-links a {
  color: #333;
  font-family: 'Poppins', sans-serif;
  font-weight: 500;
  font-size: 1.1rem;
  text-decoration: none;
  transition: color 0.3s ease;
  position: relative;
}

.navbar-links a:hover {
  color: #c09dc9;
}

.navbar-links a::after {
  content: '';
  position: absolute;
  bottom: -5px;
  left: 0;
  width: 0;
  height: 2px;
  background: #c09dc9;
  transition: width 0.3s ease;
}

.navbar-links a:hover::after {
  width: 100%;
}

.hamburger {
  display: none;
  flex-direction: column;
  cursor: pointer;
}

.bar {
  width: 25px;
  height: 3px;
  background-color: #333;
  margin: 3px 0;
  transition: all 0.3s ease;
}

@media (max-width: 768px) {
  .navbar {
    padding: 0 1rem;
    min-height: 70px;
  }
  
  .logo-image {
    height: 35px;
  }
  
  .navbar-links {
    display: none;
    flex-direction: column;
    position: absolute;
    top: 100%;
    left: 0;
    width: 100%;
    background: white;
    padding: 1rem 0;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    gap: 0;
  }
  
  .navbar-links.active {
    display: flex;
  }
  
  .navbar-links li {
    margin: 0.75rem 0;
  }
  
  .navbar-links a {
    padding: 0.5rem 2rem;
    display: block;
    font-size: 1.1rem;
  }
  
  .hamburger {
    display: flex;
  }
}

@media (max-width: 480px) {
  .logo-image {
    height: 30px;
  }
}
</style>