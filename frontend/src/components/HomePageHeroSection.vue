<template>
    <div class="hero-section">
        <h1>Conectando mães com suporte real desde o primeiro dia</h1>
        <button class="cta-button" href="/details">Descubra o Bloom hoje!</button>
    </div>
</template>

<script setup>
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700&display=swap');
.hero-section {
  flex: 1;
  text-align: left;
  max-width: 490px;
  margin-top: -160px;
  z-index: 1;
}

h1 {
    font-family: 'Montserrat', sans-serif;
    font-size: 45px;
    font-weight: 700;

    line-height: 1.2;
    margin-bottom: 1.5rem;

    color: #000;
}

.cta-button {
    background-image: linear-gradient(to right, #957FEF 0%, #C09FCA 65%);
    width: 480px;
    height: 100px;

    border: none;

    color: white;

    padding: 1.25rem 2.5rem;

    font-family: 'Montserrat', sans-serif;
    border-radius: 9999px;

    font-size: 32px;
    font-weight: 400;

    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);

    cursor: pointer;

    transition: transform 0.2s ease-in-out;
}

.cta-button:hover {
    transform: scale(1.05);
}

</style>