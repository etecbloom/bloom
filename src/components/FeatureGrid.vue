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
  gap: clamp(1.5rem, 3vw, 2rem);
  margin-bottom: clamp(2rem, 4vw, 4rem);
  padding: 0 1rem;
}

/* RESPONSIVIDADE MELHORADA */
@media (max-width: 1024px) {
  .feature-grid {
    gap: 1.5rem;
    margin-bottom: 3rem;
  }
}

@media (max-width: 980px) {
  .feature-grid {
    grid-template-columns: 1fr;
    gap: 1.25rem;
    margin-bottom: 2.5rem;
  }
}

@media (max-width: 768px) {
  .feature-grid {
    gap: 1rem;
    margin-bottom: 2rem;
    padding: 0 0.5rem;
  }
}

@media (max-width: 480px) {
  .feature-grid {
    gap: 0.875rem;
    margin-bottom: 1.5rem;
  }
}
</style>