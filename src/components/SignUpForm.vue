<template>
  <form class="signup-form" @submit.prevent="onSubmit">
    <InputField 
      label="Usuário" 
      type="text" 
      v-model="form.username" 
      :required="true"
    />
    <SelectField 
      label="Gênero" 
      :options="genderOptions" 
      v-model="form.gender" 
    />
    <InputField 
      label="E-mail" 
      type="email" 
      v-model="form.email" 
      :required="true"
    />
    <InputField 
      label="Senha" 
      type="password" 
      v-model="form.password" 
      :required="true"
    />
    <InputField 
      label="Confirmar senha" 
      type="password" 
      v-model="form.confirmPassword" 
      :required="true"
    />

    <AuthButton :text="'Criar'" type="submit" />
  </form>
</template>

<script setup>
import { reactive } from 'vue'
import InputField from "../components/InputField.vue"
import SelectField from "../components/SelectField.vue"
import AuthButton from "../components/AuthButton.vue"

const genderOptions = [
  'Masculino',
  'Feminino', 
  'Prefiro não dizer',
  'Outro'
]

const form = reactive({
  username: '',
  gender: 'Masculino',
  email: '',
  password: '',
  confirmPassword: ''
})

function onSubmit() {
  if (!form.username || !form.email || !form.password) {
    alert('Por favor preencha os campos obrigatórios.')
    return
  }
  if (form.password !== form.confirmPassword) {
    alert('As senhas não coincidem.')
    return
  }
  console.log('form', form)
}
</script>

<style scoped>
.signup-form {
  width: 100%;
  max-width: 400px;
  display: flex;
  flex-direction: column;
  overflow-y: hidden;
  align-items: center;
  gap: 20px;
  margin-top: 10px;
}

@media (max-width: 768px) {
  .signup-form {
    gap: 18px;
    max-width: 100%;
  }
}

@media (max-width: 480px) {
  .signup-form {
    gap: 16px;
  }
}
</style>