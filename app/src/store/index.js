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
    INSERT_GALLERY_IMAGES: (store, images) => {
      store.galleryImages = store.galleryImages.concat(images);
    }
  },
  actions: {
    getGalleryImages: context => {
      axios.get(settings.API_BASE_URL + 'api/gallery/images/')
        .then(res => {
          context.commit('INSERT_GALLERY_IMAGES', res.data.results);
        })
    }
  },
  getters: {
    getGalleryImageById: state => id => {
      return state.galleryImages.find(image => image.id == id);
    } 
  }
})
