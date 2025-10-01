<script setup>
import DashboardNav from '../components/DashboardNav.vue';
import DailySummary from '../components/DailySummary.vue';
import NotificationsCard from '../components/NotificationsCard.vue';
import QuickAction from '../components/QuickAction.vue';
</script>

<template>
  <div class="dashboard-page">

    <DashboardNav />

    <div class="dashboard-content-wrapper">

      <div class="welcome-section">
        <h1>Oi, User! Estamos aqui com você nessa jornada.</h1>
      </div>

      <div class="main-layout-grid">

        <div class="quick-actions-container-with-flowers">

          <div class="background-flowers">
            <img src="/FOGreenFlower.png" class="flowers first-card-flowers-1" />
            <img src="/FOPurpleFlower.png" class="flowers first-card-flowers-2" />
          </div>

          <div class="quick-actions-column">
            <QuickAction icon-type="forum" title="Acessar fórum Bloom" route="/forum" />
            <QuickAction icon-type="chat" title="Acessar chat com psicóloga" route="/chat" />
            <QuickAction icon-type="groups" title="Grupos de apoio" route="/group" />
            <QuickAction icon-type="diary" title="Meu diário de gravidez" route="/diary" />
          </div>

        </div>

        <div class="sidebar-column">
          <DailySummary />
          <NotificationsCard />
        </div>

      </div>

    </div>

    <div class="illustration">

      <div class="pregnant-illustration-container">
        <img src="/pregnant_woman_illustration.png" alt="Mulher grávida" class="pregnant-illustration">
      </div>

    </div>

    <div class="background-shapes">
      <img src="/left_shape_purple.png" class="shape left-shape-1" />
      <img src="/left_shape_green.png" class="shape left-shape-2" />
      <img src="/right_shape_purple.png" class="shape right-shape-1" />
      <img src="/right_shape_green.png" class="shape right-shape-2" />
    </div>

  </div>
</template>

<style scoped>
:root {
  --primary-accent: #B7A1C5;

  --text-dark: !important;
}

.dashboard-page {
  min-height: 100vh;
  background-color: #FFF9EB;
  padding-top: 80px;
  font-family: 'Poppins', sans-serif;
  overflow-x: hidden;
}

.dashboard-content-wrapper {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 5%;
}

.welcome-section {
  padding: 20px 0 30px;
}

.welcome-section h1 {
  font-weight: 600 !important;
  font-size: 30px;
  color: #3D3A3A;
  margin: 0;
}

.main-layout-grid {
  display: flex;
  flex-direction: column;
  gap: 30px;
  padding-bottom: 50px;
}

.quick-actions-container-with-flowers {
  position: relative;
}

.quick-actions-column {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
}

.background-flowers {
  position: absolute;
  top: -25px;
  left: -25px;
  width: 50%;
  height: 50%;
  pointer-events: none;
  z-index: 10;
}

.flowers {
  position: absolute;
  width: 40px;
  height: auto;
}

.first-card-flowers-1 {
  top: 15px;
  left: 20px;
  z-index: 2;
  transform: rotate(-10deg);
}

.first-card-flowers-2 {
  top: 25px;
  left: 10px;
  z-index: 1;
  transform: rotate(5deg);
  opacity: 0.8;
}

.sidebar-column {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.illustration {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
}

.background-shapes {
  display: none;
}

.pregnant-illustration-container {
  width: 60%;
  max-width: 250px;
  margin: 20px auto 10px;
}

.pregnant-illustration {
  width: 100%;
  height: auto;
}

.motivational-quote {
  text-align: center;
  padding: 0 10px;
}

.motivational-quote p {
  font-weight: 700 !important;

  font-size: 18px;
  color: var(--text-dark);
  margin: 0;
}

@media (min-width: 992px) {

  .welcome-section h1 {
    font-size: 40px !important;
    padding-top: 25px;
    font-weight: 500;
  }

  .main-layout-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 50px;
  }

  .quick-actions-container-with-flowers {
    grid-column: 1;
    position: relative;
  }

  .background-flowers {
    top: -30px;
    left: -30px;
    width: auto;
    height: auto;
  }

  .flowers {
    width: 40px;
  }

  .first-card-flowers-1 {
    top: 5px;
    left: 15px;
    z-index: 2;
    transform: rotate(0deg);
  }

  .first-card-flowers-2 {
    top: 20px;
    left: 5px;
    z-index: 1;
    opacity: 0.8;
    transform: rotate(10deg);
  }

  .quick-actions-column {
    grid-template-columns: repeat(2, 1fr);
    gap: 30px;
  }

  .sidebar-column {
    gap: 20px;
    position: relative;
  }

  .illustration {
    position: absolute;
    top: 27%;
    right: 12%;
    width: 100%;
    flex-direction: column;
    align-items: flex-end;
  }

  .background-shapes {
    display: block;
    ;
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    max-width: 200;
  }

  .shape {
    position: absolute;
    width: 300px;
  }

  .left-shape-1 {
    bottom: 0;
    left: 0;
  }

  .left-shape-2 {
    bottom: 0;
    left: 0;
  }

  .right-shape-1 {
    bottom: 0;
    right: 0;
  }

  .right-shape-2 {
    bottom: 0;
    right: 0;
  }

  .pregnant-illustration-container {
    width: 250px;
    margin: 0;
  }
}
</style>