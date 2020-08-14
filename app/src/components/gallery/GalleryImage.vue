<template>
    <div class="gallery-image">
        <a :href="galleryImage.image">
            <img :src="galleryImage.image" 
                :alt="galleryImage.alt_text">
        </a>
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
    }
}
</script>