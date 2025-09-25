<template>
  <div class="signup-card">
    <div class="card-inner">
      <h2 class="card-title">Crie sua conta</h2>

      <SignUpForm />
    </div>

    <p class="login-link">
      Já tem um login?
      <a href="/login">Entre agora!</a>
    </p>
  </div>
</template>

<script setup>
import SignUpForm from "../components/SignUpForm.vue"
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap');

.signup-card {
  width: 585px;
  height: 790px;
  background: #faf7ff;
  border-radius: 24px;
  padding: 32px;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
}

.card-inner {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.card-title {
  font-family: 'Poppins', sans-serif;
  font-weight: 600;
  font-size: 35px; 
  color: #333;
  margin: 6px 0 18px 0;
  text-align: center;
}

.login-link {
  font-family: 'Poppins', sans-serif;
  margin: 12px 0 4px 0;
  font-size: 15px;
  color: #666;
  text-align: center;
}

.login-link a {
  color: #c09dc9;
  margin-left: 6px;
  text-decoration: none;
  font-weight: 600;
}
</style>
