<template>
  <div id="home">
    <router-link to="/gallery">
      <img :src="require('@/assets/angels-logo.png')" 
        id="logo"
        alt="Logo">
    </router-link>
  </div>
</template>

<script>

export default {
  name: 'Home',
}
</script>
