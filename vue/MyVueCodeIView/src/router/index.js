import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/app/home'
import Login from '@/app/login'
import Reg from '@/app/register'
import Classify from '@/app/classify'
import Form from '@/app/form'
import Table from '@/app/table'
import Details from '@/app/details'
import ZH from '@/app/zhihu'
import ZHDetails from '@/app/zhDetails'

import BackstageLogin from '@/backstage/backstageLogin'

Vue.use(Router)

export default new Router({
  routes: [
    // 首页
    {
      path: '/', components: {
        defaultHome: Home,
      },
      meta: {
        index: 0,
        showContent: true,
      },
      children: [
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
        },
        // 详情页面
        {
          path: '/details/:id',
          components: {
            showFoodDetails: Details
          },
          meta: {
            index: 1,
            showContent: false
          }
        },

      ]
    },// 知乎日报
    {
      path: '/zh', components: {
        defaultHome: ZH
      },
      meta: {
        index: 1,
        showContent: true,
      },
      children: [
        {
          path: '/zhdetails/:id', components: {
            zhihuDetails: ZHDetails
          }
        }
      ]
    },
    // 前台登录
    {
      path: '/login', components: {
        defaultHome: Login,
      }
    },
    // 前台注册
    {
      path: '/reg', components: {
        defaultHome: Reg,
      }
    },
    // 后台路由
    {
      path: '/backstageLogin', components: {
        defaultHome: BackstageLogin,
      }
    },

  ]
})
