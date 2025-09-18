<template>
    <div class="pregnant-mom-image-container">
        <img src="/mom.png" alt="Uma mulher grávida" class="pregnant-mom-image">
    </div>
</template>

<script>
export default {
    name: 'PregnantMomImage',
};
</script>

<style scoped>
.pregnant-mom-image-container {
  flex: 1;
  display: flex;
  justify-content: flex-end;
  align-items: flex-start;
  margin-top: -20px;
  margin-left: 20%;
}

.pregnant-mom-image {
  max-width: 380px;
  max-height: 800px;
}
</style>