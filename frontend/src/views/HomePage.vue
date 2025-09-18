<template>
    <Navbar />
    <div class="hero-container">
        <HomePageHeroSection />
        <PregnantMomImage />
    </div>
</template>

<script setup>
import Navbar from '../components/Navbar.vue';
import HomePageHeroSection from '../components/HomePageHeroSection.vue';
import PregnantMomImage from '../components/PregnantMomImage.vue';
</script>

<style scoped>
.hero-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 6rem;
  height: 100vh;
  box-sizing: border-box;
}
</style>