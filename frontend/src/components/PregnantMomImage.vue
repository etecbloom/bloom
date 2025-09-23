<template>
    <div class="pregnant-mom-image-container">
        <img src="/mom.png" alt="Uma mulher grávida" class="pregnant-mom-image">
    </div>
</template>

<script>
export default {
    name: 'PregnantMomImage',
};
</script>

<style scoped>
.pregnant-mom-image-container {
  flex: 1;
  display: flex;
  justify-content: flex-end;
  align-items: flex-start;
  transform: translateY(-12px);
  margin-left: 20%;
}

.pregnant-mom-image {
  z-index: 2;
  max-width: 380px;
  max-height: 800px;
}

/* --- REGRAS PARA TELAS MENORES --- */
@media (max-width: 768px) {
  .pregnant-mom-image-container {
    margin-left: 0; /* Remove a margem */
    justify-content: center; /* Centraliza a imagem */
    transform: none; /* Remove o deslocamento */
    flex: initial; /* Reseta a propriedade flex */
    width: 100%;
  }
  .pregnant-mom-image {
    max-width: 280px; /* Diminui o tamanho da imagem */
  }
}
</style>