<template>
  <div class="hero-shape-container">
    <img src="/shape.png" alt="Forma decorativa" class="hero-shape" />
  </div>
</template>

<style scoped>
.hero-shape-container {
  position: absolute;
  top: 0;
  right: 0;
  width: 55vw;
  height: 100vh;
  overflow: hidden;
  z-index: -1;
}

.hero-shape {
  width: 100%;
  height: 100%;
  object-fit: cover;

  opacity: 0.7;
  
  transform: scale(0.80);
  transform-origin: bottom right;
}

@media (max-width: 768px) {
  .hero-shape-container {
    display: none;
  }
}
</style>
