<template>
    <div id="gallery-images">
        <GalleryImage v-for="galleryImage in galleryImages" 
            :key="galleryImage.id" 
            :gallery-image="galleryImage" />
    </div>
</template>

<script>
import GalleryImage from './GalleryImage.vue';

export default {
    components: {
        GalleryImage
    },
    computed: {
        galleryImages() {
            return this.$store.state.galleryImages;
        }
    }
}
</script>