<template>
    <div class="hero-section">
        <h1>Conectando mães com suporte real desde o primeiro dia</h1>
        <button class="cta-button">Descubra o Bloom hoje!</button>
    </div>
</template>

<script setup>
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700&display=swap');

/*
  Usamos `scoped` para que os estilos CSS aqui
  afetem apenas este componente, evitando conflitos
  com outras partes da sua aplicação.
*/
.hero-section {
  flex: 1;
  text-align: left;
  max-width: 490px;
  margin-top: -160px;
}

h1 {
    font-family: 'Montserrat', sans-serif;
    /* Define o tamanho da fonte para o título */
    font-size: 45px;
    /* Torna o texto em negrito */
    font-weight: 700;
    /* Define a altura da linha para um melhor espaçamento vertical */
    line-height: 1.2;
    /* Adiciona uma margem inferior para separar do botão */
    margin-bottom: 1.5rem;
    /* Garante que a cor do texto seja preta */
    color: #000;
}

.cta-button {
    /*
    Aplica o gradiente de cores especificado na imagem.
    O `to right` faz o gradiente ir da esquerda para a direita.
    As cores e suas paradas (`0%` e `65%`) seguem o que foi mostrado no painel.
  */
    background-image: linear-gradient(to right, #957FEF 0%, #C09FCA 65%);
    width: 480px;
    height: 100px;
    /* Remove a borda padrão do botão */
    border: none;
    /* Cor do texto do botão */
    color: white;
    /* Adiciona espaçamento interno para o botão ficar maior */
    padding: 1.25rem 2.5rem;
    /* Torna o botão em formato de pílula */
    font-family: 'Montserrat', sans-serif;
    border-radius: 9999px;
    /* Um valor grande cria um formato de pílula */
    /* Tamanho da fonte do botão */
    font-size: 32px;
    /* Deixa o texto do botão em negrito */
    font-weight: 400;
    /* Adiciona uma sombra para dar um efeito de profundidade */
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    /* Muda o cursor do mouse para indicar que é clicável */
    cursor: pointer;
    /* Adiciona transição suave para efeitos de hover */
    transition: transform 0.2s ease-in-out;
}

.cta-button:hover {
    /* Efeito de escala no hover para o botão se destacar */
    transform: scale(1.05);
}

</style>