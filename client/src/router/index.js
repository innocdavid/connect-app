import { createRouter, createWebHistory } from 'vue-router';
import HomeViewVue from '@/views/HomeView.vue';
import SignupViewVue from '@/views/SignupView.vue';
import LoginViewVue from '@/views/LoginView.vue';
import FeedViewVue from '@/views/FeedView.vue';
import MessageView from '@/views/MessageView.vue';
import SearchView from '@/views/SearchView.vue';


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeViewVue
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignupViewVue
    },
    {
      path: '/login',
      name: 'login',
      component: LoginViewVue
    },
    {
      path: '/feed',
      name: 'feed',
      component: FeedViewVue
    },
    {
      path: '/message',
      name: 'message',
      component: MessageView
    },
    {
      path: '/search',
      name: 'search',
      component: SearchView
    }
  ]
})

export default router
