import { createRouter, createWebHistory } from 'vue-router'
import Index from '@/views/Index.vue'
import Vegetable from '@/views/Vegetable.vue'
import Recipe from '@/views/Recipe.vue'
import TestCarousel from '@/views/TestCarousel.vue'
import TestLoading from '@/views/TestLoading.vue'

const routes = [
  {
    path: '/',
    name: 'index',
    component: Index
  },
  {
    path: '/vegetable',
    name: 'vegetable',
    component: Vegetable
  },
  {
    path: '/recipe',
    name: 'recipe',
    component: Recipe
  },
  {
    path: '/carousel',
    name: 'carousel',
    component: TestCarousel
  },
  {
    path: '/loading',
    name: 'loading',
    component: TestLoading
  }

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
