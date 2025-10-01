<template>
  <header class="section-header">
    <h2>{{ title }}</h2>
    <p>{{ subtitle }}</p>
  </header>
</template>

<script setup>
defineProps({
  title: String,
  subtitle: String
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap');

.section-header {
  text-align: center;
  margin: 1.2rem 0 2rem;
  z-index: 5;
  padding: 0 1rem;
}

h2 {
  font-size: clamp(2rem, 6vw, 3.5rem);
  font-family: 'Poppins', sans-serif;
  font-weight: 600;
  line-height: 1.1;
  color: #504D4D;
  margin: 0;
}

p {
  font-size: clamp(1.5rem, 4vw, 3rem);
  font-family: 'Poppins', sans-serif;
  font-weight: 600;
  color: #C09FCA;
  margin: 0.5rem 0 0;
  line-height: 1.2;
}

/* RESPONSIVIDADE ADICIONADA */
@media (max-width: 1024px) {
  .section-header {
    margin: 1rem 0 1.5rem;
  }
  
  h2 {
    font-size: clamp(1.75rem, 5vw, 2.5rem);
  }
  
  p {
    font-size: clamp(1.25rem, 3.5vw, 2rem);
  }
}

@media (max-width: 768px) {
  .section-header {
    margin: 0.75rem 0 1.25rem;
  }
  
  h2 {
    font-size: clamp(1.5rem, 6vw, 2rem);
    line-height: 1.15;
  }
  
  p {
    font-size: clamp(1.125rem, 4vw, 1.5rem);
    margin-top: 0.25rem;
  }
}

@media (max-width: 480px) {
  .section-header {
    margin: 0.5rem 0 1rem;
  }
  
  h2 {
    font-size: clamp(1.25rem, 7vw, 1.75rem);
  }
  
  p {
    font-size: clamp(1rem, 5vw, 1.25rem);
  }
}
</style>