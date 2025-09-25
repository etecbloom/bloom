import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import DetailsPage from '../views/DetailsPage.vue'
import SignUpPage from '../views/SignUpPage.vue'

const routes = [
  {
    path: '/',
    name: 'HomePage',
    component: HomePage
  },
  {
    path: '/details',
    name: 'DetailsPage',
    component: DetailsPage
  },
  {
    path: '/sign-up',
    name: 'SignUpPage',
    component: SignUpPage
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
