import Vue from 'vue'
import Router from 'vue-router'
import Index from '../components/index'
import Info from '../components/info'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      component: Index
    },
    {
      path: '/info/:id',
      component: Info
    }
  ]
})
