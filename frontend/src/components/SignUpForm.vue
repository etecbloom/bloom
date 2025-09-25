<template>
  <form class="signup-form" @submit.prevent="onSubmit">
    <InputField label="Usuário" type="text" v-model="form.username" />
    <SelectField label="Gênero" :options="['Masculino','Feminino','Prefiro não dizer','Outro']" v-model="form.gender" />
    <InputField label="E-mail" type="email" v-model="form.email" />
    <InputField label="Senha" type="password" v-model="form.password" />
    <InputField label="Confirmar senha" type="password" v-model="form.confirmPassword" />

    <AuthButton :text="'Criar'" />
  </form>
</template>

<script setup>
import { reactive } from 'vue'
import InputField from "../components/InputField.vue"
import SelectField from "../components/SelectField.vue"
import AuthButton from "../components/AuthButton.vue"

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
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 18px; /* espaçamento vertical consistente */
  margin-top: 6px;
}
</style>
