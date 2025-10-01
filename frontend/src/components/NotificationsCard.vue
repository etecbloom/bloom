<script setup>

</script>

<template>
  <div class="notifications-card">
    <h3 class="card-title">Notificações</h3>
    <div class="notification-item">
      <div class="notification-badge-wrapper">
        <span class="notification-badge">+9 mensagens no grupo</span>
      </div>
    </div>
  </div>
</template>

<style scoped>
:root {
  --primary-accent: #;
  --text-dark: #3D3A3A;
}

.notifications-card {
  background-color: white;
  border-radius: 12px;
  padding: 20px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
}

.card-title {
  font-family: 'Poppins', sans-serif;
  font-weight: 700 !important;
  font-size: 24px !important;
  color: var(--text-dark); /* CRITICAL FIX 1: Text Color */
  margin-top: 0;
  margin-bottom: 20px;
}

.notification-item {
  /* CRITICAL FIX 2: Unified structure for the whole line */
  display: flex;
  align-items: center;
  gap: 15px;
  font-family: 'Poppins', sans-serif;
  font-weight: 700 !important;
  font-size: 24px !important; 
  color: #555;
}

.notification-badge-wrapper {
  background-color: #B7A1C5;
  border-radius: 8px;
  padding: 5px 10px;
  display: inline-block;
}

.notification-badge {
  color: #FFFFFF;
  font-family: 'Poppins', sans-serif;
  font-weight: 400 !important;
  font-size: 20px !important;
}
</style>