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
}

h2 {
  font-size: 56px;
  font-family: 'Poppins', sans-serif;
  font-weight: 600;
  line-height: 1.02;
  color: #504D4D;
  margin: 0;
}

p {
  font-size: 48px;
  font-family: 'Poppins', sans-serif;
  font-weight: 600;
  color: #C09FCA;
  margin: 8px 0 0;
}
</style>
