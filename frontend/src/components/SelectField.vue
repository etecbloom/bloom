<template>
  <div class="select-field">
    <label>{{ label }}</label>
    <select :value="modelValue" @input="$emit('update:modelValue', $event.target.value)">
      <option v-for="opt in options" :key="opt" :value="opt">{{ opt }}</option>
    </select>
  </div>
</template>

<script setup>
defineProps({
  label: String,
  options: { type: Array, default: () => [] },
  modelValue: { type: String, default: '' }
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500&display=swap');

.select-field {
  display: flex;
  flex-direction: column;
  width: 500px;
  box-sizing: border-box;
}

.select-field label {
  font-family: 'Poppins', sans-serif;
  font-size: 14px;
  color: #5d5858;
  margin-bottom: 8px;
}

.select-field select {
  width: 100%;
  height: 64px;
  border: 1px solid #e6dfe9;
  border-radius: 12px;
  padding: 0 42px 0 16px; /* espaço para a seta à direita */
  font-size: 16px;
  font-family: 'Poppins', sans-serif;
  background: white;
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  background-image: url("data:image/svg+xml;charset=UTF-8,%3Csvg width='12' height='8' viewBox='0 0 12 8' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M1 1l5 5 5-5' stroke='%23999' stroke-width='2' fill='none' fill-rule='evenodd' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 14px center;
  background-size: 12px;
}

/* foco */
.select-field select:focus {
  border-color: #c9a2d6;
  box-shadow: 0 4px 18px rgba(192,157,201,0.12);
}
</style>
