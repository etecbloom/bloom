<template>
  <div class="signup-card">
    <div class="card-header">
      <h2 class="card-title">Crie sua conta</h2>
    </div>
    
    <div class="card-content">
      <SignUpForm />
    </div>

    <p class="login-link">
      Já tem um login? <a href="/login" class="login-btn">Entre agora!</a>
    </p>
  </div>
</template>

<script setup>
import SignUpForm from "../components/SignUpForm.vue"
</script>

<style scoped>
.signup-card {
  width: 100%;
  max-width: 450px;
  background: #FAF5FF;
  border-radius: 20px;
  padding: 3rem 2.5rem;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  position: relative;
  z-index: 15;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.1);
  border: 1px solid #f0f0f0;
}

.card-header {
  text-align: center;
  margin-bottom: 2.5rem;
}

.card-title {
  font-family: 'Poppins', sans-serif;
  font-weight: 600;
  font-size: 2rem;
  color: #000;
  margin: 0;
  letter-spacing: -0.5px;
}

.card-content {
  width: 100%;
  margin-bottom: 2rem;
}

.login-link {
  font-family: 'Poppins', sans-serif;
  margin: 0;
  font-size: 0.95rem;
  color: #666;
  text-align: center;
  padding-top: 2rem;
  border-top: 1px solid #eee;
  width: 100%;
}

.login-btn {
  color: #c09dc9;
  margin-left: 0.25rem;
  text-decoration: none;
  font-weight: 600;
  transition: color 0.3s ease;
}

.login-btn:hover {
  color: #a87db3;
  text-decoration: underline;
}

@media (max-width: 768px) {
  .signup-card {
    padding: 2rem 1.5rem;
    max-width: 400px;
    margin: 1rem;
  }
  
  .logo-image {
    height: 45px;
    margin-bottom: 1.25rem;
  }
  
  .card-title {
    font-size: 1.75rem;
  }
}

@media (max-width: 480px) {
  .signup-card {
    padding: 1.5rem 1.25rem;
    border-radius: 16px;
  }
  
  .logo-image {
    height: 40px;
    margin-bottom: 1rem;
  }
  
  .card-title {
    font-size: 1.5rem;
  }
}
</style>