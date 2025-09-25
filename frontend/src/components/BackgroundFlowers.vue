<template>
  <div class="background-flowers">
    <img
      v-for="(flower, index) in flowers"
      :key="index"
      :src="flower.src"
      alt="Decorative flower"
      class="flower"
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
  z-index: 0;
  pointer-events: none;
}

.flower {
  position: absolute;
}
</style>
