<template>
  <div class="background-shapes">
    <img
      v-for="(shape, index) in shapes"
      :key="index"
      :src="shape.src"
      :alt="`Forma decorativa ${index + 1}`"
      class="shape"
      :style="{
        top: shape.top,
        left: shape.left,
        right: shape.right,
        bottom: shape.bottom,
        transform: `scale(${shape.scale}) rotate(${shape.rotate}deg)`,
        opacity: shape.opacity
      }"
    />
  </div>
</template>

<script setup>
defineProps({
  shapes: {
    type: Array,
    default: () => []
  }
})
</script>

<style scoped>
.background-shapes {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
  z-index: -1;
  pointer-events: none;
}

.shape {
  position: absolute;
  max-width: min(40%, 200px);
  height: auto;
  transition: opacity 0.3s ease;
}

/* RESPONSIVIDADE ADICIONADA */
@media (max-width: 1024px) {
  .shape {
    max-width: min(35%, 180px);
  }
}

@media (max-width: 768px) {
  .shape {
    max-width: min(30%, 150px);
    opacity: 0.8 !important;
  }
}

@media (max-width: 480px) {
  .shape {
    max-width: min(25%, 120px);
    opacity: 0.7 !important;
  }
}

.shape {
  will-change: transform;
  backface-visibility: hidden;
  transform-style: preserve-3d;
}
</style>