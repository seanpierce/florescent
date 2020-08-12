import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import settings from '@/settings.js'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    galleryImages: []
  },
  mutations: {
    ADD_GALLERY_IMAGES: (store, galleryImages) => {
      store.galleryImages = store.galleryImages.concat(galleryImages);
    }
  },
  actions: {
    getGalleryImages(context) {
      axios.get(settings.API_BASE_URL + 'gallery/images')
        .then(resposne => {
          context.commit('ADD_GALLERY_IMAGES', resposne.data);
        })
    }
  },
  modules: {
  }
})
