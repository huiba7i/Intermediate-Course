import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/app/home'
import Login from '@/app/login'
import Reg from '@/app/register'
import Classify from '@/app/classify'
import Form from '@/app/form'
import Table from '@/app/table'
import Details from '@/app/details'

import BackstageLogin from '@/backstage/backstageLogin'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/', component: Home,
      meta: {
        index: 0,
        showContent: true
      },
      children: [
        {
          path: 'login', component: Login,
          meta: {
            index: 1,
            showContent: false
          }
        },
        {
          path: 'reg', component: Reg,
          meta: {
            index: 1,
            showContent: false
          }
        },
        {
          path: 'classify', component: Classify,
          meta: {
            index: 1,
            showContent: false
          }
        },
        {
          path: 'form', component: Form,
          meta: {
            index: 1,
            showContent: false
          }
        },
        {
          path: 'table', component: Table,
          meta: {
            index: 1,
            showContent: false
          }
        },// 详情页面
        {
          path: 'details/:id', component: Details,
          meta: {
            index: 1,
            showContent: false
          }
        },
      ]
    },
    // 后台路由
    {
      path: 'backstageLogin', component: BackstageLogin
    },
    // 重定向
    {
      path: '/', redirect: '/'
    }
  ]
})
