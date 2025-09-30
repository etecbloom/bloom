<template>
  <div class="feature-card">
    <div class="icon-wrap">
      <img :src="icon" :alt="title" class="icon" />
    </div>
    <div class="content">
      <h3>{{ title }}</h3>
      <p>{{ description }}</p>
    </div>
    <img v-if="flower" :src="flower" alt="flower decoration" class="card-flower" />
  </div>
</template>

<script setup>
defineProps({
  icon: String,
  title: String,
  description: String,
  flower: String
})
</script>

<style scoped>
.feature-card {
  position: relative;
  display: flex;
  align-items: center;
  gap: 1.5rem;
  background: #F6F1FF;
  padding: 2.5rem 2rem;
  border-radius: 18px;
  box-shadow: 0 10px 30px rgba(27,31,35,0.06);
  height: 120px;
  width: 100%;
  max-width: 810px;
  box-sizing: border-box;
  margin: 0 auto;
}

.icon-wrap {
  flex: 0 0 auto;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100px;
  height: 100px;
}

.icon {
  width: 100%;
  max-width: 80px;
  height: auto;
  display: block;
}

.content {
  flex: 1;
}

.content h3 {
  font-family: 'Poppins', sans-serif;
  font-weight: 600;
  font-size: 1.5rem;
  margin: 0 0 1rem 0;
  color: #222;
  line-height: 1.3;
}

.content p {
  font-family: 'Poppins', sans-serif;
  font-weight: 400;
  font-size: 1rem;
  margin: 0;
  line-height: 1.5;
  color: #5d5858;
}

.card-flower {
  position: absolute;
  right: 20px;
  bottom: 20px;
  width: 32px;
  height: auto;
  pointer-events: none;
}

@media (max-width: 1024px) {
  .feature-card {
    min-height: 300px;
    padding: 2rem 1.5rem;
    max-width: 100%;
    gap: 1.25rem;
  }
  
  .icon-wrap {
    width: 90px;
    height: 90px;
  }
  
  .icon {
    max-width: 70px;
  }
  
  .content h3 {
    font-size: 1.375rem;
  }
}

@media (max-width: 768px) {
  .feature-card {
    min-height: 250px;
    padding: 1.75rem 1.5rem;
    flex-direction: column;
    text-align: center;
    gap: 1rem;
  }
  
  .icon-wrap {
    width: 80px;
    height: 80px;
    margin-bottom: 0.5rem;
  }
  
  .icon {
    max-width: 60px;
  }
  
  .content h3 {
    font-size: 1.25rem;
    margin-bottom: 0.75rem;
  }
  
  .content p {
    font-size: 0.9rem;
  }
  
  .card-flower {
    width: 28px;
    right: 15px;
    bottom: 15px;
  }
}

@media (max-width: 480px) {
  .feature-card {
    min-height: 220px;
    padding: 1.5rem 1.25rem;
  }
  
  .icon-wrap {
    width: 70px;
    height: 70px;
  }
  
  .icon {
    max-width: 50px;
  }
  
  .content h3 {
    font-size: 1.125rem;
  }
  
  .content p {
    font-size: 0.875rem;
  }
}
</style>