<template>
    <div class="gallery-image">
        <router-link :to="'/gallery/' + galleryImage.id">
            <img :src="galleryImage.image" 
                :alt="galleryImage.alt_text">
        </router-link>
    </div>
</template>

<script>
import settings from '@/settings.js';

export default {
    data: () => {
        return {
            media_root: settings.MEDIA_ROOT
        }
    },
    props: {
        galleryImage: Object
    },
}
</script>