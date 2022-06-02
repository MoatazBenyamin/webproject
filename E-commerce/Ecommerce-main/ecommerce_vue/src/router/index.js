import { createRouter, createWebHistory } from 'vue-router'
import store from '../store' 
import HomeView from '../views/HomeView.vue'
import ProductView from '../views/ProductView.vue'
import Category from '../views/CategoryView.vue'
import Search from '../views/SearchView.vue'
import Cart from '../views/CartView.vue'

import LogIn from '../views/LogInView.vue'
import MyAccount from '../views/MyAccount.vue'
import Checkout from '../views/Checkout.vue'
import Success from '../views/Success.vue'
import forgot from '../views/forgot.vue'
import Reset from '../views/rest.vue'

const routes = [
  {
    path: '/',
    name: 'HomeView',
    component: HomeView
  },
  {
    path: '/reset-password/:token',
    name: 'Reset',
    component: Reset
  },
  {
    path: '/forget-password',
    name: 'forgot',
    component: forgot
  },
  {
    path: '/cart/success',
    name: 'Success',
    component: Success
  },
  {
    path: '/my-account',
    name: 'MyAccount',
    component: MyAccount,
    meta: {
        requireLogin: true
    }
  },

  {
    path: '/search',
    name: 'Search',
    component: Search
  },
  {
    path: '/log-in',
    name: 'LogIn',
    component: LogIn
  },
  {
    path: '/cart',
    name: 'Caret',
    component: Cart
  },
  {
    path: '/cart/checkout',
    name: 'Checkout',
    component: Checkout,
    meta: {
        requireLogin: true
    }
  },
  {
    path: '/about',
    name: 'about',
    component: () => import( '../views/AboutView.vue')
  },
  {
    path: '/:category_slug/:product_slug',
    name: 'ProductView',
    component: ProductView
  },
   {
    path: '/:category_slug',
    name: 'Category',
    component: Category
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})
router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next({ name: 'LogIn', query: { to: to.path } });
  } else {
    next()
  }
})
export default router
