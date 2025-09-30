<template>
    <div class="pregnant-mom-image-container">
        <img src="/mom.png" alt="Uma mulher grávida sorrindo" class="pregnant-mom-image">
    </div>
</template>

<script setup>
// Componente de apresentação - script setup moderno
</script>

<style scoped>
.pregnant-mom-image-container {
  flex: 1;
  display: flex;
  justify-content: flex-end;
  align-items: flex-start;
  transform: translateY(0);
  margin-left: auto;
  padding: 1rem;
}

.pregnant-mom-image {
  position: relative;
  z-index: 2;
  width: 100%;
  max-width: min(380px, 40vw);
  height: auto;
  display: block;
}

/* RESPONSIVIDADE MELHORADA */
@media (max-width: 1024px) {
  .pregnant-mom-image-container {
    justify-content: center;
    margin-left: 0;
    padding: 0.5rem;
  }
  
  .pregnant-mom-image {
    max-width: min(320px, 45vw);
  }
}

@media (max-width: 768px) {
  .pregnant-mom-image-container {
    justify-content: center;
    margin-left: 0;
    transform: none;
    flex: initial;
    width: 100%;
    padding: 1rem 0;
  }
  
  .pregnant-mom-image {
    max-width: min(280px, 60vw);
  }
}

@media (max-width: 480px) {
  .pregnant-mom-image {
    max-width: 250px;
  }
}

@media (min-width: 1440px) {
  .pregnant-mom-image {
    max-width: 420px;
  }
}
</style>