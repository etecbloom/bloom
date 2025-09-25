<template>
  <div class="cta">
    <a :href="link" class="cta-btn">{{ text }}</a>
  </div>
</template>

<script setup>
defineProps({
  text: String,
  link: String
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@500;600&display=swap');

.cta {
  display: flex;
  justify-content: center;
  margin-top: 2.8rem;
  z-index: 3;
}
.cta-btn {
  background: #C09DC9;
  color: white;
  font-family: 'Poppins', sans-serif;
  font-weight: 600;
  padding: 14px 36px;
  border-radius: 40px;
  text-decoration: none;
  box-shadow: 0 10px 24px rgba(27,31,35,0.08);
  display: inline-block;
}
.cta-btn:hover {
  transform: translateY(-2px);
}
</style>
