<template>
  <section class="details-page">
    <div class="logo">
      <img src="/logo_bloom.png" alt="Bloom" class="logo-image">
    </div>
    <SectionHeader 
      title="Tudo o que você precisa" 
      subtitle="em um só lugar!"
    />
    
    <FeatureGrid :features="features" />
    
    <CallToAction 
      text="Comece agora!" 
      link="/sign-up"
    />
  </section>
</template>

<script setup>
import SectionHeader from '../components/SectionHeader.vue'
import FeatureGrid from '../components/FeatureGrid.vue'
import CallToAction from '../components/CallToAction.vue'

const shapes = [
  {
    src: "/ShapeDetailsPage.png",
    top: "5%",
    right: "5%",
    scale: 1.2,
    rotate: 0,
    opacity: 0.7
  },
  {
    src: "/ShapeDetailsPage2.png",
    bottom: "5%",
    left: "5%",
    scale: 1,
    rotate: 0,
    opacity: 0.7
  },
  {
    src: "/ShapeDetailsPage3.png",
    top: "35%",
    left: "10%",
    scale: 0.9,
    rotate: 0,
    opacity: 0.5
  },
  {
    src: "/ShapeDetailsPage4.png",
    bottom: "20%",
    right: "15%",
    scale: 0.8,
    rotate: 0,
    opacity: 0.5
  }
]

const features = [
  {
    icon: '/IconPsychologist.png',
    title: 'Conversa com psicóloga',
    description: 'Converse com psicólogas em tempo real'
  },
  {
    icon: '/IconMother.png',
    title: 'Discussões entre mães',
    description: 'Fórum para mães trocarem experiências e dicas da maternidade'
  },
  {
    icon: '/IconCalendar.png', 
    title: 'Agendamento',
    description: 'Agende suas consultas com facilidade, receba lembrete automático'
  },
  {
    icon: '/IconAlerts.png',
    title: 'Alerta e Dicas',
    description: 'Receba lembretes diários, dicas práticas e bem-estar'
  }
]

const flowers = [
  {
    src: '/GreenFlower.png',
    top: '5%',
    left: '27%',
    scale: 0.8,
    rotate: 15
  },
  {
    src: '/PurpleFlower.png',
    top: '7%',
    left: '5%',
    scale: 0.7,
    rotate: -10
  },
  {
    src: '/PurpleFlower.png',
    top: '75%',
    left: '25%',
    scale: 1.0,
    rotate: 30
  },
  {
    src: '/GreenFlower.png',
    top: '75%',
    right: '25%',
    scale: 0.6,
    rotate: -20
  },
  {
    src: '/PurpleFlower.png',
    top: '5%',
    right: '10%',
    scale: 0.9,
    rotate: -20
  },
]
</script>

<style scoped>
.details-page {
  position: relative;
  padding: clamp(2rem, 4vw, 4rem) clamp(1rem, 3vw, 2rem);
  overflow: hidden;
  background: #fff;
  min-height: 100vh;
  box-sizing: border-box;
}

.logo {
  position: absolute;
  top: clamp(1rem, 3vw, 1.25rem);
  left: clamp(1rem, 3vw, 1.5rem);
  z-index: 20;
}

.logo-image {
  height: 40px;
  width: auto;
  display: block;
}

@media (max-width: 980px) {
  .details-page {
    padding: 3rem 1.5rem;
  }
}

@media (max-width: 768px) {
  .details-page {
    padding: 2rem 1rem;
  }
  
  .logo {
    position: relative;
    top: 0;
    left: 0;
    margin-bottom: 1rem;
    text-align: center;
  }
  
  .logo-image {
    margin: 0 auto;
    height: 35px;
  }
}

@media (max-width: 480px) {
  .details-page {
    padding: 1.5rem 0.75rem;
  }
  
  .logo-image {
    height: 30px;
  }
}

@media (min-width: 1440px) {
  .details-page {
    padding: 5rem 3rem;
  }
  
  .logo-image {
    height: 45px;
  }
}
</style>