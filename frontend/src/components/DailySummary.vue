<script setup>
// State placeholder for data fetching
</script>

<template>
  <div class="summary-card">
    <h3 class="card-title">Resumo do dia</h3>
    <div class="week-indicator-container">
        <span class="week-label">Semana 27</span>
    </div>
    <ul class="summary-list">
      <li class="summary-item">
        <span class="bullet-dot">
            <img src="/check_icon.png" alt="Check" class="check-icon">
        </span>
        Coma saudável
      </li>
      <li class="summary-item">
        <span class="bullet-plus">+5</span>
        tópicos nos grupos
      </li>
    </ul>
  </div>
</template>

<style scoped>
:root {
  --primary-accent: #B7A1C5;
  --text-dark: #3D3A3A;
}

.summary-card {
  background-color: white;
  border-radius: 12px;
  padding: 20px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
}

.card-title {
  font-family: 'Poppins', sans-serif;
  font-weight: 700 !important;
  font-size: 24px !important;
  color: var(--text-dark);
  margin-top: 0;
  margin-bottom: 20px;
}

.week-indicator-container {
    padding: 5px 0;
    margin-bottom: 15px;
    font-weight: 700;
}

.week-label {
    font-size: 24px !important; 
    color: var(--text-dark);
}

.summary-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.summary-item {
  /* Alinhamento dos itens */
  display: flex;
  align-items: center;
  font-family: 'Poppins', sans-serif;
  font-weight: 700 !important; 
  font-size: 24px !important; 
  color: var(--text-dark);
}

.bullet-dot {
    /* Define o container para a imagem */
    display: flex;
    align-items: center;
    justify-content: center;
    margin-right: 10px;
    height: 20px; /* Garante que o alinhamento vertical funcione */
}

/* NOVO ESTILO: Garante que a imagem tenha 20x20px */
.check-icon {
    width: 20px !important;
    height: 20px !important;
    vertical-align: middle;
}

.bullet-plus {
    /* Ajusta o +5 para ficar consistente */
    font-weight: 900;
    color: var(--text-dark);
    font-size: 20px; /* Mantém o tamanho do "símbolo" */
    margin-right: 10px;
}
</style>