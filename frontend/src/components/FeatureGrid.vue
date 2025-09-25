<template>
  <div class="feature-grid">
    <FeatureCard 
      v-for="(feature, i) in features" 
      :key="i" 
      :icon="feature.icon" 
      :title="feature.title" 
      :description="feature.description" 
    />
  </div>
</template>

<script setup>
import FeatureCard from './FeatureCard.vue'

defineProps({
  features: Array
})
</script>

<style scoped>
.feature-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
  margin-bottom: 4rem;
}

@media (max-width: 980px) {
  .feature-grid {
    grid-template-columns: 1fr;
    gap: 1.25rem;
  }
}
</style>
