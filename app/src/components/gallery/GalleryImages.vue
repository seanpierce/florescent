<template>
    <div id="gallery=images">
    </div>
</template>

<script>
export default {
    computed: {
        galleryImages() {
            return this.$store.state.galleryImages;
        }
    },
    mounted() {
        console.log(this.$store.state)
    }
}
</script>