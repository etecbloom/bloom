<template>
  <div class="feature-card">
    <div class="icon-wrap">
      <img :src="icon" alt="" class="icon" />
    </div>
    <div class="content">
      <h3>{{ title }}</h3>
      <p>{{ description }}</p>
    </div>
    <img v-if="flower" :src="flower" alt="flower" class="card-flower" />
  </div>
</template>

<script setup>
defineProps({
  icon: String,
  title: String,
  description: String
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700;400&display=swap');

.feature-card {
  position: relative;
  display: flex;
  align-items: center;
  gap: 1rem;
  background: #F6F1FF;
  padding: 1.6rem 1.8rem;
  border-radius: 18px;
  box-shadow: 0 10px 30px rgba(27,31,35,0.06);
  min-height: 120px;
  overflow: visible;
}

.icon-wrap {
  flex: 0 0 auto;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 106px;
  height: 126px;
}
.icon {
  width: 84px;
  height: 90px;
  display: block;
}

.content {
  flex: 1;
}
.content h3 {
  font-family: 'Poppins', sans-serif;
  font-weight: 600;
  font-size: 20px;
  margin: 0 0 6px 0;
  color: #222;
}
.content p {
  font-family: 'MontSerrat', sans-serif;
  font-weight: 400;
  font-size: 15px;
  margin: 0;
  line-height: 1.45;
  color: #5d5858;
}

.card-flower {
  position: absolute;
  right: 14px;
  bottom: 12px;
  width: 36px;
  height: auto;
  pointer-events: none;
}
</style>
