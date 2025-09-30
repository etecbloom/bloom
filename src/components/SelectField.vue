<template>
  <div class="select-field">
    <label class="select-label">{{ label }}</label>
    <select
      :value="modelValue"
      @change="$emit('update:modelValue', $event.target.value)"
      class="select-element"
    >
      <option 
        v-for="option in options" 
        :key="option" 
        :value="option"
      >
        {{ option }}
      </option>
    </select>
  </div>
</template>

<script setup>
defineProps({
  label: String,
  modelValue: String,
  options: {
    type: Array,
    default: () => []
  }
})

defineEmits(['update:modelValue'])
</script>

<style scoped>
.select-field {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.select-label {
  font-family: 'Poppins', sans-serif;
  font-size: 14px;
  font-weight: 500;
  color: #333;
  margin-bottom: 2px;
}

.select-element {
  width: 100%;
  padding: 14px 16px;
  border: 2px solid #e8e4f1;
  border-radius: 12px;
  font-family: 'Poppins', sans-serif;
  font-size: 15px;
  background: white;
  transition: all 0.3s ease;
  box-sizing: border-box;
  cursor: pointer;
  appearance: none;
  background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23333' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
  background-repeat: no-repeat;
  background-position: right 16px center;
  background-size: 16px;
}

.select-element:focus {
  outline: none;
  border-color: #c09dc9;
  box-shadow: 0 0 0 3px rgba(192, 157, 201, 0.1);
}

@media (max-width: 768px) {
  .select-element {
    padding: 12px 14px;
    font-size: 14px;
  }
  
  .select-label {
    font-size: 13px;
  }
}
</style>