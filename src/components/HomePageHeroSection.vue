<template>
    <div class="hero-section">
        <h1>Conectando mães com suporte real desde o primeiro dia</h1>
        <button class="cta-button" @click="$router.push('/details')">
            Descubra o Bloom hoje!
        </button>
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
    margin-top: 0;
    z-index: 1;
}

h1 {
    font-family: 'Montserrat', sans-serif;
    font-size: clamp(1.75rem, 5vw, 2.8rem);
    font-weight: 700;
    line-height: 1.2;
    margin-bottom: 1.5rem;
    color: #000;
}

.cta-button {
    background-image: linear-gradient(to right, #957FEF 0%, #C09FCA 65%);
    width: 100%;
    max-width: 480px;
    height: auto;
    min-height: 60px;
    border: none;
    color: white;
    padding: 1rem 2rem;
    font-family: 'Montserrat', sans-serif;
    border-radius: 9999px;
    font-size: clamp(1.125rem, 3vw, 1.75rem);
    font-weight: 600;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    cursor: pointer;
    transition: all 0.3s ease;
}

.cta-button:hover {
    transform: scale(1.05);
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
}

/* RESPONSIVIDADE ADICIONADA */
@media (max-width: 1024px) {
    .hero-section {
        text-align: center;
        max-width: 100%;
        margin: 0 auto;
    }
    
    h1 {
        font-size: clamp(1.5rem, 4vw, 2.5rem);
    }
}

@media (max-width: 768px) {
    .hero-section {
        padding: 0 1rem;
    }
    
    .cta-button {
        min-height: 55px;
        padding: 0.875rem 1.5rem;
        font-size: clamp(1rem, 4vw, 1.25rem);
    }
}

@media (max-width: 480px) {
    h1 {
        font-size: clamp(1.25rem, 5vw, 1.75rem);
        margin-bottom: 1rem;
    }
    
    .cta-button {
        min-height: 50px;
        padding: 0.75rem 1.25rem;
    }
}
</style>