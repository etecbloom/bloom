<template>
  <div class="input-field">
    <label>{{ label }}</label>
    <input :type="type" :value="modelValue" @input="$emit('update:modelValue', $event.target.value)" />
  </div>
</template>

<script setup>
defineProps({
  label: String,
  type: { type: String, default: 'text' },
  modelValue: { type: [String, Number], default: '' }
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500&display=swap');

.input-field {
  display: flex;
  flex-direction: column;
  width: 500px; /* exatamente a largura do Figma */
  box-sizing: border-box;
}

.input-field label {
  font-family: 'Poppins', sans-serif;
  font-size: 14px;
  color: #5d5858;
  margin-bottom: 8px;
}

.input-field input {
  width: 100%;
  height: 64px;
  border: 1px solid #e6dfe9;
  border-radius: 12px;
  padding: 0 16px;
  font-size: 16px;
  font-family: 'Poppins', sans-serif;
  box-sizing: border-box;
  outline: none;
  background: #fff;
  transition: box-shadow .12s ease, border-color .12s ease;
}

/* efeito de foco */
.input-field input:focus {
  border-color: #c9a2d6;
  box-shadow: 0 4px 18px rgba(192,157,201,0.12);
}
</style>
