<template>
  <div class="input-field">
    <label class="input-label">{{ label }}</label>
    <input
      :type="type"
      :value="modelValue"
      @input="$emit('update:modelValue', $event.target.value)"
      class="input-element"
      :required="required"
    />
  </div>
</template>

<script setup>
defineProps({
  label: String,
  type: {
    type: String,
    default: 'text'
  },
  modelValue: String,
  required: {
    type: Boolean,
    default: false
  }
})

defineEmits(['update:modelValue'])
</script>

<style scoped>
.input-field {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.input-label {
  font-family: 'Poppins', sans-serif;
  font-size: 14px;
  font-weight: 500;
  color: #333;
  margin-bottom: 2px;
}

.input-element {
  width: 100%;
  padding: 14px 16px;
  border: 2px solid #e8e4f1;
  border-radius: 12px;
  font-family: 'Poppins', sans-serif;
  font-size: 15px;
  background: white;
  transition: all 0.3s ease;
  box-sizing: border-box;
}

.input-element:focus {
  outline: none;
  border-color: #c09dc9;
  box-shadow: 0 0 0 3px rgba(192, 157, 201, 0.1);
}

.input-element::placeholder {
  color: #999;
}

@media (max-width: 768px) {
  .input-element {
    padding: 12px 14px;
    font-size: 14px;
  }
  
  .input-label {
    font-size: 13px;
  }
}
</style>