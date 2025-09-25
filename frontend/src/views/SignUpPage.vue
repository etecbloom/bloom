<template>
  <div class="logo">
    <img src="/logo_bloom.png">
  </div>
  <div class="signup-page">
    <BackgroundFlowers :flowers="flowersConfig" />
    <SignUpCard />
  </div>
</template>

<script setup>
import SignUpCard from "../components/SignUpCard.vue"

const flowersConfig = [
  { src: "/GreenFlower.png", top: "15%", left: "25%", scale: 0.8, rotate: 15 },
  { src: "/PurpleFlower.png", top: "8%", left: "5%", scale: 0.7, rotate: -10 },
  { src: "/GreenFlower.png", top: "50%", left: "30%", scale: 0.6, rotate: 30 },
  { src: "/PurpleFlower.png", top: "50%", left: "48%", scale: 0.4, rotate: -20 },
  { src: "/PurpleFlower.png", top: "10%", right: "25%", scale: 0.65, rotate: 25 },
  { src: "/GreenFlower.png", bottom: "20%", right: "25%", scale: 0.9, rotate: -15 },
  { src: "/GreenFlower.png", bottom: "5%", left: "8%", scale: 0.6, rotate: -25 },
  { src: "/PurpleFlower.png", bottom: "40%", right: "50%", scale: 0.7, rotate: 5 },
  { src: "/PurpleFlower.png", top: "70%", left: "30%", scale: 0.8, rotate: 20 },
  { src: "/PurpleFlower.png", top: "75%", right: "30%", scale: 0.5, rotate: -30 }
]
</script>

<style scoped>
.logo {
  position: absolute;
  top: 20px;
  left: 24px;
  z-index: 20; 
}

.signup-page {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: white;
  position: relative;
  overflow: hidden;
}
</style>
