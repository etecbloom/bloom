<template>
  <div class="background-flowers">
    <img
      v-for="(flower, index) in flowers"
      :key="index"
      :src="flower.src"
      :alt="`Flor decorativa ${index + 1}`"
      class="flower"
      :class="`flower-${index}`"
      :style="{
        top: flower.top,
        left: flower.left,
        right: flower.right,
        bottom: flower.bottom,
        transform: `scale(${flower.scale}) rotate(${flower.rotate}deg)`
      }"
    />
  </div>
</template>

<script setup>
defineProps({
  flowers: {
    type: Array,
    default: () => []
  }
})
</script>

<style scoped>
.background-flowers {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
  z-index: 1;
  pointer-events: none;
}

.flower {
  position: absolute;
  max-width: min(120px, 15vw);
  height: auto;
  transition: opacity 0.3s ease;
}

@media (max-width: 768px) {
  .flower {
    max-width: min(80px, 12vw);
    opacity: 0.7;
  }
}

@media (max-width: 480px) {
  .flower {
    max-width: min(60px, 10vw);
    opacity: 0.6;
  }
}

.flower {
  will-change: transform;
  backface-visibility: hidden;
}
</style>