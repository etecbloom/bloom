<template>
  <div class="cta">
    <a :href="link" class="cta-btn">{{ text }}</a>
  </div>
</template>

<script setup>
defineProps({
  text: String,
  link: String
})
</script>

<style scoped>


.cta {
  display: flex;
  justify-content: center;
  margin-top: clamp(2rem, 4vw, 2.8rem);
  z-index: 3;
  padding: 0 1rem;
}

.cta-btn {
  background: linear-gradient(135deg, #c09dc9, #a87db3);
  color: white;
  font-family: 'Poppins', sans-serif;
  font-weight: 600;
  font-size: clamp(0.875rem, 2vw, 1rem);
  padding: clamp(0.75rem, 2vw, 0.875rem) clamp(1.5rem, 4vw, 2.25rem);
  border-radius: 40px;
  text-decoration: none;
  box-shadow: 0 10px 24px rgba(27,31,35,0.08);
  display: inline-block;
  transition: all 0.3s ease;
  text-align: center;
  min-width: 140px;
}

.cta-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 12px 28px rgba(27,31,35,0.12);
  background: linear-gradient(135deg, #a87db3, #9665a3);
}

/* RESPONSIVIDADE ADICIONADA */
@media (max-width: 768px) {
  .cta {
    margin-top: 1.5rem;
  }
  
  .cta-btn {
    min-width: 120px;
    padding: 0.875rem 2rem;
  }
}

@media (max-width: 480px) {
  .cta {
    margin-top: 1.25rem;
  }
  
  .cta-btn {
    width: 100%;
    max-width: 200px;
    min-width: auto;
    padding: 0.75rem 1.5rem;
  }
}
</style>