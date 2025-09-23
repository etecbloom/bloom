<template>
  <div class="background-flowers">
    <!-- Mais flores foram adicionadas para um visual mais completo -->
    <img src="/GreenFlower.png" alt="Flor decorativa" class="flower flower-1" />
    <img src="/PurpleFlower.png" alt="Flor decorativa" class="flower flower-2" />
    <img src="/GreenFlower.png" alt="Flor decorativa" class="flower flower-3" />
    <img src="/PurpleFlower.png" alt="Flor decorativa" class="flower flower-4" />
    <img src="/PurpleFlower.png" alt="Flor decorativa" class="flower flower-5" />
    <img src="/GreenFlower.png" alt="Flor decorativa" class="flower flower-6" />
    <img src="/GreenFlower.png" alt="Flor decorativa" class="flower flower-8" />
    <img src="/PurpleFlower.png" alt="Flor decorativa" class="flower flower-9" />
    <img src="/PurpleFlower.png" alt="Flor decorativa" class="flower flower-10" />
    <img src="/PurpleFlower.png" alt="Flor decorativa" class="flower flower-11" />
  </div>
</template>

<style scoped>
.background-flowers {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  overflow: hidden; /* Garante que as flores não "vazem" da tela */
  z-index: 0;
  pointer-events: none;
}

.flower {
  position: absolute;
}

/* Posições ajustadas para replicar a imagem de referência */
.flower-1 {
  top: 15%;
  left: 25%;
  transform: scale(0.8) rotate(15deg);
}

.flower-2 {
  top: 8%;
  left: 5%;
  transform: scale(0.7) rotate(-10deg);
}

.flower-3 {
  top: 50%;
  left: 30%;
  transform: scale(0.6) rotate(30deg);
}

.flower-4 {
  top: 50%;
  left: 48%;
  transform: scale(0.4) rotate(-20deg);
}

.flower-5 {
  top: 10%;
  right: 25%;
  transform: scale(0.65) rotate(25deg);
}

.flower-6 {
  bottom: 20%;
  right: 25%;
  transform: scale(0.9) rotate(-15deg);
}

.flower-8 {
  bottom: 5%;
  left: 8%;
  transform: scale(0.6) rotate(-25deg);
}

.flower-9 {
  bottom: 40%;
  right: 50%;
  transform: scale(0.7) rotate(5deg);
}

.flower-10 {
  top: 70%;
  left: 30%;
  transform: scale(0.8) rotate(20deg);
}

.flower-11 {
  top: 75%;
  right: 30%;
  transform: scale(0.5) rotate(-30deg);
}
</style>