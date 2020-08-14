<template>
  <div id="app">
    <Menu />
    <router-view/>
  </div>
</template>

<script>
import Menu from '@/components/Menu.vue';

export default {
  components: {
    Menu
  },
  created() {
    this.$store.dispatch('getGalleryImages');
  }
}
</script>
