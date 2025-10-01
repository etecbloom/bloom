<script setup>
// Assuming /logo_bloom.png is available in the public assets folder.
</script>

<template>
  <nav class="dashboard-nav">
    <div class="background-flowers">
      <img src="/FOGreenFlower.png" class="flowers first-card-flowers-1" />
      <img src="/FOPurpleFlower.png" class="flowers first-card-flowers-2" />
    </div>
    <div class="nav-logo">
      <img src="/logo_bloom.png" alt="Bloom" class="logo-image">
    </div>
    <ul class="nav-links">
      <li><a href="/feed" class="nav-link active">Feed</a></li>
      <li><a href="/forum" class="nav-link">Forum</a></li>
      <li><a href="/chat" class="nav-link">Chat</a></li>
    </ul>
  </nav>
</template>

<style scoped>
:root {
  --primary-accent: #B7A1C5;
  --text-dark: #3D3A3A;
}

.dashboard-nav {
  position: fixed;
  top: 1%;
  left: 5%;
  width: 90%;
  height: 80px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 20px;
  background-color: white;
  box-shadow: rgba(50, 50, 93, 0.25) 0px 6px 12px -2px, rgba(0, 0, 0, 0.3) 0px 3px 7px -3px;
  ;
  border-radius: 80px;
  z-index: 1000;
}

.background-flowers {
  position: absolute;
  top: -25px;
  left: -25px;
  width: 50%;
  height: 50%;
  pointer-events: none;
  z-index: 10;
}

.flowers {
  position: absolute;
  width: 40px;
  height: auto;
}

.first-card-flowers-1 {
  top: 15px;
  left: 20px;
  z-index: 2;
  transform: rotate(-10deg);
}

.first-card-flowers-2 {
  top: 25px;
  left: 10px;
  z-index: 1;
  transform: rotate(5deg);
  opacity: 0.8;
}

.nav-logo {
  margin-right: auto;
  padding-left: 10px;
}

.logo-image {
  height: 20px;
}

.nav-links {
  list-style: none;
  display: flex;
  gap: 20px;
  padding: 0;
}

.nav-link {
  text-decoration: none;
  color: var(--text-dark);
  font-family: 'Poppins', sans-serif;
  font-weight: 700 !important;
  font-size: 18px;
  transition: color 0.3s;
}

.nav-link:hover,
.nav-link.active {
  color: var(--primary-accent);
}

@media (min-width: 768px) {
  .nav-link {
    font-size: 24px !important;
  }

  .nav-links {
    margin-right: 50px;
    gap: 50px;
  }

  .nav-logo {
    padding-left: 20px;
  }

  .logo-image {
    height: 40px;
  }

}
</style>