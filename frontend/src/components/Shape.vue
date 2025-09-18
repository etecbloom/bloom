<template>
  <div class="hero-shape-container">
    <div class="hero-shape"></div>
  </div>
</template>

<script setup>
// Sem script
</script>

<style scoped>
.hero-shape-container {
  /* Fixa o elemento na tela, ignorando o fluxo normal */
  position: absolute;

  /*
    Posiciona o elemento no meio da altura da tela (50% do viewport height).
    Ele vai do meio para baixo.
  */
  top: 50vh;

  /* Cola o componente no canto direito da tela */
  right: 0;

  /* Define a largura como 50% da largura da tela */
  width: 50vw;

  /* Define a altura como 50% da altura da tela (do meio até o fim) */
  height: 50vh;
  
  /* Garante que o conteúdo que ultrapassa os limites seja cortado */
  overflow: hidden;

  /*
    Ajusta a opacidade para 40%. Se a imagem da mulher grávida e as flores
    também ficarem com essa opacidade, mova esta linha para a classe .hero-shape.
  */
  opacity: 0.4;
}

.hero-shape {
  /* Define a cor de fundo da forma roxa */
  background-color: #e0d0f2;
  
  /* Faz com que a forma ocupe todo o contêiner */
  width: 100%;
  height: 100%;

  /* Cria a curva no canto inferior esquerdo, fazendo a forma parecer que está encostando */
  border-bottom-left-radius: 50% 100%;
}
</style>