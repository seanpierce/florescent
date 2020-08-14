import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home.vue'

Vue.use(VueRouter)

  const routes = [
  {
    name: 'Home',
    path: '/',
    component: Home
  },
  {
    name: 'Gallery',
    path: '/gallery',
    component: () => import('@/views/Gallery.vue')
  },
  {
    name: 'Gallery Detail',
    path: '/gallery/:id',
    props: true,
    component: () => import('@/views/GalleryDetail.vue')
  },
  {
    name: 'Shop',
    path: '/shop',
    component: () => import('@/views/Shop.vue')
  },
  {
    name: 'Contact',
    path: '/contact',
    component: () => import('@/views/Contact.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
