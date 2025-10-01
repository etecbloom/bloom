<template>
  <Navbar />
  <div class="hero-container">
    <HomePageHeroSection />
    <PregnantMomImage />
    <Shape :shapes="shapes"/>
    <BackgroundFlowers :flowers="flowers" />
  </div>
</template>

<script setup>
import Navbar from '../components/Navbar.vue';
import HomePageHeroSection from '../components/HomePageHeroSection.vue';
import PregnantMomImage from '../components/PregnantMomImage.vue';

import BackgroundFlowers from '../components/BackgroundFlowers.vue';

const shapes = [
  {
    src: "/shape.png",
    top: "27%",
    right: "-5%",
    bottom: "auto",
    scale: 0.8,
    rotate: 0,
    opacity: 0.7
  },
]

const flowers = [
  {
    src: '/GreenFlower.png',
    top: '15%',
    left: '25%',
    scale: 0.8,
    rotate: 15
  },
  {
    src: '/PurpleFlower.png',
    top: '8%',
    left: '5%',
    scale: 0.7,
    rotate: -10
  },
  {
    src: '/GreenFlower.png',
    top: '50%',
    left: '30%',
    scale: 0.6,
    rotate: 30
  },
  {
    src: '/PurpleFlower.png',
    top: '50%',
    left: '48%',
    scale: 0.4,
    rotate: -20
  },
  {
    src: '/PurpleFlower.png',
    top: '10%',
    right: '25%',
    scale: 0.65,
    rotate: 25
  },
  {
    src: '/GreenFlower.png',
    bottom: '20%',
    right: '25%',
    scale: 0.9,
    rotate: -15
  },
  {
    src: '/GreenFlower.png',
    bottom: '5%',
    left: '8%',
    scale: 0.6,
    rotate: -25
  },
  {
    src: '/PurpleFlower.png',
    bottom: '40%',
    right: '50%',
    scale: 0.7,
    rotate: 5
  },
  {
    src: '/PurpleFlower.png',
    top: '70%',
    left: '30%',
    scale: 0.8,
    rotate: 20
  },
  {
    src: '/PurpleFlower.png',
    top: '75%',
    right: '30%',
    scale: 0.5,
    rotate: -30
  }
]
</script>

<style scoped>
.hero-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  min-height: 80vh;
  height: auto;
  padding: clamp(1rem, 3vw, 2rem) clamp(2rem, 6vw, 6rem);
  box-sizing: border-box;
  position: relative;
  gap: clamp(1rem, 3vw, 2rem);
}

@media (max-width: 1024px) {
  .hero-container {
    padding: 1.5rem 3rem;
    gap: 1.5rem;
  }
}

@media (max-width: 768px) {
  .hero-container {
    flex-direction: column;
    padding: 1rem 1.5rem;
    gap: 1rem;
    min-height: auto;
    text-align: center;
  }
}

@media (max-width: 480px) {
  .hero-container {
    padding: 0.75rem 1rem;
    gap: 0.75rem;
  }
}

@media (min-width: 1440px) {
  .hero-container {
    padding: 3rem 8rem;
    min-height: 85vh;
  }
}

@media (min-width: 1920px) {
  .hero-container {
    max-width: 1800px;
    margin: 0 auto;
  }
}
</style>