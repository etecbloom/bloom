<template>
  <nav class="navbar">
    <div class="navbar-logo">
      <img src="/logo_bloom.png" alt="Logo Bloom">
    </div>
    <ul :class="['navbar-links', { 'active': isMobileMenuOpen }]">
      <li><a href="#">Apresentação</a></li>
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

<script>
export default {
  name: 'Navbar',
  data() {
    return {
      isMobileMenuOpen: false
    };
  },
  methods: {
    toggleMobileMenu() {
      this.isMobileMenuOpen = !this.isMobileMenuOpen;
    }
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;700&display=swap');

.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #FFFFFF;
  color: white;
  width: 1920;
  height: 90;
}

.navbar-logo {
  color: white;
  width: 215px;
  height: 52px;
  padding-left: 25px;
}

.navbar-links {
  list-style: none;
  display: flex;
  margin-right: 50px;
  padding: 0;
}

.navbar-links li {
  margin-left: 5rem;
}

.navbar-links a {
  color: black;
  font-family: 'Poppins', sans-serif;
  font-weight: 700px;
  font-size: 24px;
  text-decoration: none;
  transition: color 0.3s ease;
}

.navbar-links a:hover {
  color: #ddd;
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
  margin: 4px 0;
  transition: transform 0.3s ease;
}

/* Responsividade para telas menores */
@media (max-width: 768px) {
  .navbar-links {
    display: none;
    flex-direction: column;
    width: 100%;
    background-color: #FFFFFF;
    position: absolute;
    top: 60px;
    left: 0;
    text-align: center;

  }

  .navbar-links.active {
    display: flex;
  }

  .navbar-links li {
    margin: 1rem 0;
  }

  .hamburger {
    display: flex;
  }
  
  .hamburger.active .bar:nth-child(2) {
    opacity: 0;
  }
  
  .hamburger.active .bar:nth-child(1) {
    transform: rotate(45deg) translate(5px, 5px);
  }
  
  .hamburger.active .bar:nth-child(3) {
    transform: rotate(-45deg) translate(5px, -5px);
  }
}
</style>