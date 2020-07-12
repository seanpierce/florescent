<template>
    <div>
        <div>Gallery</div>
        <div id="gallery-images">
            <div class="gallery-image" v-for="image in images" :key="image.id">
                <v-lazy-image :src="'media/' + image.image"
                    src-placeholder="https://cdn-images-1.medium.com/max/80/1*xjGrvQSXvj72W4zD6IWzfg.jpeg" />
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import VLazyImage from "v-lazy-image";

export default {
    components: {
        VLazyImage
    },
    data() {
        return {
            images: null
        }
    },
    methods: {
        getImages() {
            axios.get('/api/gallery/images')
                .then(response => {
                    this.images = response.data;
                })
        }
    },
    mounted() {
        this.getImages();
    }
}
</script>