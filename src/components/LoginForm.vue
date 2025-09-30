<template>
  <form class="login-form" @submit.prevent="handleLogin">
    <InputField 
      label="Usuário" 
      v-model="credentials.username" 
      id="username-input"
      type="text"
    />

    <InputField 
      label="Senha" 
      v-model="credentials.password" 
      id="password-input"
      type="password"
    />

    <AuthButton text="Entrar" type="submit" />

    <a href="#" class="recovery-link">Esqueceu a senha?</a>

    <div class="signup-text">
      Não tem uma conta? 
      <a href="/sign-up" class="create-account-link">Crie uma agora!</a>
    </div>
  </form>
</template>

<script setup>
import { ref } from 'vue';
import InputField from '../components/InputField.vue'; 
import AuthButton from '../components/AuthButton.vue'; 

const credentials = ref({
  username: '',
  password: ''
});

const handleLogin = () => {
  console.log('Login Attempt:', credentials.value);
  alert(`Login successful (simulated) for user: ${credentials.value.username}`);
};
</script>

<style scoped>
.login-form {
  font-family: 'Poppins', sans-serif; 
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.recovery-link {
  text-align: center;
  color: #A87DB3;
  font-weight: 500;
  text-decoration: none;
  font-size: 0.9rem;
  margin-top: -5px; 
}

.recovery-link:hover {
  text-decoration: underline;
}

.signup-text {
  text-align: center;
  font-size: 0.9rem;
  color: #555;
  margin-top: 10px;
}

.create-account-link {
  color: #A87DB3;
  font-weight: 600;
  text-decoration: none;
  font-style: italic; 
}

.create-account-link:hover {
  text-decoration: underline;
}
</style>