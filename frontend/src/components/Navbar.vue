<script setup>
import { ref } from 'vue';

const isMobileMenuOpen = ref(false);

function toggleMobileMenu() {
  isMobileMenuOpen.value = !isMobileMenuOpen.value;
}

function closeMobileMenu() {
  isMobileMenuOpen.value = false;
}
</script>

<template>
  <header class="navbar-header">
    <nav class="navbar">
      <div class="logo">
        <img src="/logo_bloom.png">
      </div>

      <ul class="navbar-links">
        <li><a href="/details">Visão geral</a></li>
        <li><a href="#contact">Contate-nos</a></li>
        <li><a href="#resources">Recursos</a></li>
      </ul>

      <button class="hamburger-menu" @click="toggleMobileMenu" aria-label="Toggle navigation">
        <span class="bar"></span>
        <span class="bar"></span>
        <span class="bar"></span>
      </button>
    </nav>

    <div class="mobile-nav" :class="{ 'is-active': isMobileMenuOpen }">
       <a href="/details" @click="closeMobileMenu">Visão geral</a>
       <a href="#contact" @click="closeMobileMenu">Contate-nos</a>
       <a href="#resources" @click="closeMobileMenu">Recursos</a>
    </div>
  </header>
</template>

<style scoped>
.navbar-header {
  background: white;
  position: sticky;
  top: 0;
  z-index: 1000;
}

.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 1.5rem;
  height: 40px;
}

.logo img {
  height: 32px;
}

.navbar-links { 
  display: none;
}

.hamburger-menu {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  width: 24px;
  height: 24px;
  background: transparent;
  cursor: pointer;
  border: none;
  padding: 0;
  z-index: 20;
}

.hamburger-menu .bar {
  display: block;
  width: 24px;
  height: 2px;
  background-color: #3D3A3A;
}

.mobile-nav {
  position: fixed;
  top: 90px;
  left: 0;
  width: 100%;
  font-family: 'Poppins', sans-serif;
  font-weight: 700;
  font-size: 28px;
  height: calc(100vh - 60px);
  background-color: white;
  display: flex;
  flex-direction: column;
  align-items: center;
  transform: translateX(100%);
  transition: transform 0.3s ease-in-out;
}

.mobile-nav.is-active {
  transform: translateX(0);
}

.mobile-nav a {
  padding: 1rem 0;
  font-size: 1.25rem;
  color: #333;
  text-decoration: none;
}

.mobile-nav a:hover {
    color: #C09FCA;
}

@media (min-width: 768px) {
  .navbar {
    padding: 1rem 2rem;
    max-width: 100%;
    margin: 0 auto;
  }
  
  .logo img {
    height: 40px; 
  }

  .navbar-links {
    display: flex;
    gap: 40px;
    list-style: none;
    margin: 0;
    padding: 0;
  }

  .navbar-links a {
    color: #3D3A3A;
    text-decoration: none;
    font-family: 'Poppins', sans-serif;
    font-size: 24px;
    font-weight: 500;
    transition: color 0.2s;
  }
  
  .navbar-links a:hover {
    color: #C09FCA;
  }
  
  .hamburger-menu {
    display: none;
  }
  
  .mobile-nav {
    display: none;
  }
}
</style>