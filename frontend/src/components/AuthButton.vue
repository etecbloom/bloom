<template>
  <button class="auth-button" type="submit">{{ text }}</button>
</template>

<script setup>
defineProps({
  text: String
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@500;600&display=swap');

.auth-button {
  width: 500px;
  height: 70px;
  border-radius: 12px;
  border: none;
  background: #C09DC9;
  color: #fff;
  font-family: 'Poppins', sans-serif;
  font-size: 20px;
  font-weight: 600;
  cursor: pointer;
  box-shadow: 0 12px 30px rgba(150, 103, 190, 0.12);
  transition: transform .12s ease, box-shadow .12s ease;
}

.auth-button:hover {
  transform: translateY(-3px);
  box-shadow: 0 18px 40px rgba(150, 103, 190, 0.16);
}
</style>
