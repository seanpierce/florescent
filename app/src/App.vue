<template>
  <div id="app">
    <Menu v-show="showMenu" />
    <router-view/>
  </div>
</template>

<script>
import Menu from '@/components/Menu.vue';

export default {
  components: {
    Menu
  },
  computed: {
    showMenu() {
      return this.$route.name !== 'Home'
    }
  },
  created() {
    this.$store.dispatch('getGalleryImages');
  }
}
</script>
