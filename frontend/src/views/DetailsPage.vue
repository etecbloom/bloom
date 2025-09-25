<template>
  <section class="details-page">
    <div class="logo">
      <img src="/logo_bloom.png">
    </div>
    <BackgroundFlowers />
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

const features = [
  {
    icon: '/IconPsychologist.png',
    title: 'Conversa com psicóloga',
    description: 'Converse com psicólogas em tempo real'
  },
  {
    icon: '/IconCalendar.png',
    title: 'Agendamento',
    description: 'Agende suas consultas com facilidade, receba lembrete automático'
  },
  {
    icon: '/IconMother.png',
    title: 'Discussões entre mães',
    description: 'Fórum para mães trocarem experiências e dicas da maternidade'
  },
  {
    icon: '/IconAlerts.png',
    title: 'Alerta e Dicas',
    description: 'Receba lembretes diários, dicas práticas e bem-estar'
  }
]
</script>

<style scoped>
.details-page {
  position: relative;
  padding: 4rem 2rem;
  overflow: hidden;
  background: #fff;
}

.logo {
  position: absolute;
  top: 20px;
  left: 24px;
  z-index: 20; 
}

@media (max-width: 980px) {
  .section-header h2 { font-size: 40px; }
  .section-header p { font-size: 22px; }
  .logo img { width: 100px; }
}
</style>
