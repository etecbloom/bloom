<template>
  <Navbar />
  <div class="hero-container">
    <HomePageHeroSection />
    <PregnantMomImage />
    <Shape />
    <BackgroundFlowers />
  </div>
</template>

<script setup>
import Navbar from '../components/Navbar.vue';
import HomePageHeroSection from '../components/HomePageHeroSection.vue';
import PregnantMomImage from '../components/PregnantMomImage.vue';
import Shape from '../components/Shape.vue';
import BackgroundFlowers from '../components/BackgroundFlowers.vue';
</script>

<style scoped>
.hero-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 100vh;
  padding: 0 6rem;
  box-sizing: border-box;
}
</style>