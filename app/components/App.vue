<template>
    <div>
        <Home v-if="route === 'home'" />
        <Gallery v-if="route === 'gallery'" />
    </div>
</template>

<script>
import Home from './Home';
import Gallery from './Gallery';

export default {
    components: {
        Home,
        Gallery
    },
    computed: {
        route() {
            return this.$root.route;
        }
    }
}
</script>