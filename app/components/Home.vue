<template>
    <div id="home" @click="enter()">
        <img id="logo" src="assets/images/angels.png" alt="Florescent logo">
    </div>
</template>

<script>
export default {
    methods: {
        enter() {
            window.location.pathname = '/gallery'
        }
    }
}
</script>