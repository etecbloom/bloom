<script setup>
  import { defineProps, computed } from 'vue';

  const props = defineProps({
    iconType: {
      type: String,
      required: true,
    },
    title: {
      type: String,
      required: true,
    },
    route: {
      type: String,
      required: true,
    },
  });

  const getIconPath = computed(() => {
    const iconMap = {
      forum: '/forum_icon.png',
      chat: '/chat_icon.png',
      groups: '/groups_icon.png',
      diary: '/diary_icon.png',
    };
    return iconMap[props.iconType] || '';
  });

  const onClick = () => {
    console.log(`Action clicked: ${props.title}`);
  };
</script>

  <template>
    <button class="quick-action-btn" @click="$router.push(route)">
      <div class="icon-wrapper">
        <img :src="getIconPath" class="action-icon" />
      </div>
      <span class="action-title">{{ title }}</span>
    </button>
  </template>

<style scoped>

.quick-action-btn {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 15px;
  background-color: white;
  border: none;
  border-radius: 12px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
  cursor: pointer;
  min-height: 160px;
}

.icon-wrapper {
  position: relative;
  width: 90px;
  height: 90px;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: rgba(183, 161, 197, 0.1);
  border-radius: 50%;
  margin-bottom: 10px;
}

.action-icon {
  width: 40px;
  height: 40px;
  object-fit: contain;
  display: block;
  opacity: 1;
  z-index: 2;
}

.action-title {
  font-family: 'Poppins', sans-serif;
  font-weight: 700;
  font-size: 20px;
  color: #3D3A3A;
  text-align: center;
  line-height: 1.2;
}

@media (min-width: 768px) {
  .action-title {
    font-size: 24px !important;
  }
}
</style>