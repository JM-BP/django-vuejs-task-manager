import { createRouter, createWebHistory } from 'vue-router'
import Login from '../components/Login.vue'
import Dashboard from '../components/Dashboard.vue'
import BoardView from '../components/BoardView.vue'

const routes = [
  { path: '/', component: Login },
  { path: '/dashboard', component: Dashboard },
  { path: '/board/:id', component: BoardView },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
