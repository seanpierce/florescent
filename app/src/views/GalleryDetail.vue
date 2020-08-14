<template>
    <div id="gallery-detail">
        <img :src="galleryImage.image" alt="">
        <div class="gallery-image-detail-description">
            <em>{{ galleryImage.alt_text }}</em>
        </div>
    </div>
</template>

<script>
export default {
    props: ['id'],
    computed: {
        galleryImage () {
            return this.$store.getters.getGalleryImageById(this.id);
        }
    }
}
</script>