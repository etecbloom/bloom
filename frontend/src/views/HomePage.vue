<script setup>
import Navbar from '../components/Navbar.vue';
</script>

<template>
  <div class="home-page">
    <Navbar />
    <main class="main-content">
      <section class="hero-section">
        <div class="hero-text">
          <h1>Conectando mães com suporte real desde o primeiro dia</h1>
          <div class="button-group">
            <button class="cta-button" @click="$router.push('/details')">Descubra o Bloom hoje!</button>
          </div>
        </div>

        <div class="hero-image">
          <img src="/mom.png" alt="Ilustração de uma mulher grávida com a mão na barriga" loading="lazy" />
        </div>
      </section>
    </main>
    <div class="background-shapes">
      <img src="/shape.png" class="bg-shape">
    </div>
  </div>
</template>

<style scoped>
.home-page {
  position: relative;
  overflow-y: hidden;
}

.hero-section {
  display: flex;
  flex-direction: column;
  padding: 2 1.5rem 3rem;
  text-align: center;
  max-width: 350px;
  position: relative;
  margin: 0 auto;
}

.hero-image {
  order: 2;
  display: block;
  width: 100%;
  z-index: 5;
}

.hero-image img {
  width: 62%;
  max-width: 400px;
  height: auto;
  display: block;
  margin: 0 auto;
}

.hero-text {
  order: 1;
  padding-top: 1rem;
  z-index: 6;
  margin-bottom: 0;
}

.hero-text h1 {
  font-family: 'Montserrat', sans-serif;
  font-size: 20px;
  font-weight: 700;
  color: #3D3A3A;
  margin-bottom: 1rem;
}


.button-group {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0;
  position: absolute;
  bottom: 50px;
  left: 50%;
  transform: translateX(-50%);
  width: 90%;
  max-width: 300px;
  z-index: 10;
}

.cta-button {
  width: 100%;
  max-width: 350px;
  padding: 1rem 1.5rem;
  font-size: 20px;
  font-weight: semibold;
  color: white;
  background: linear-gradient(90deg, #957FEF 0%, #C09FCA 65%);
  border: none;
  border-radius: 50px;
  cursor: pointer;
  transition: transform 0.2s ease;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  font-family: 'Montserrat', sans-serif;

  z-index: 10;
  max-width: none;
}

.cta-button:hover {
  transform: scale(0.98);
}

.background-shapes {
  display: none;
}

@media (min-width: 768px) {
  .hero-section {
    flex-direction: row;
    align-items: flex-start;
    justify-content: space-between;
    text-align: left;
    max-width: 100%;
    padding-top: 7rem;
    padding-left: 10rem;
    position: static;
  }

  .hero-image {
    display: block;
    flex: 0 0 450px;
    max-width: 450px;
    order: 2;
    margin-left: auto;
    margin-bottom: 0;
    z-index: 10;
  }

  .hero-text {
    flex: 1;
    max-width: 530px;
    order: 1;
    margin-top: 3rem;
  }

  .hero-text h1 {
    font-size: 45px;
    margin-bottom: 2rem;
  }

  .button-group {
    width: auto;
    height: auto;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    gap: 0.5rem;
    position: absolute;
    bottom: auto;
    left: auto;
    transform: none;
    z-index: auto;
  }

  .cta-button {
    padding: 1rem 2.5rem;
    font-family: 'Montserrat', sans-serif;
    font-weight: 500;
    font-size: 32px;
    width: auto;
    max-width: none;
    white-space: nowrap;
  }

  .cta-button:hover {
    transform: scale(0.98);
  }

  .hero-image {
    display: block;
    flex: 0 0 450px;
    max-width: 450px;
    order: 2;
    margin-left: auto;
  }

  .hero-image img {
    width: 360px;
    margin-left: 0;
    display: block;
  }

  .background-shapes {
    display: block;
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: -1;
  }

  .bg-shape {
    position: absolute;
    bottom: 0;
    right: 0;
    width: 740px;
    max-width: 880px;
    height: auto;
  }

}
</style>