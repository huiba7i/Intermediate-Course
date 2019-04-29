import Vue from 'vue'
import App from './App'
import router from './router'

import iView from 'iview'
import 'iview/dist/styles/iview.css'
Vue.use(iView);

import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
Vue.use(ElementUI)

import axios from 'axios'
Vue.prototype.$axios = axios

import store from './store/index'

import echarts from 'echarts'
Vue.prototype.$echarts = echarts

import  VueResource  from 'vue-resource'
Vue.prototype.$http = VueResource
Vue.use(VueResource) 

import $ from 'jquery'
Vue.prototype.$ = $

Vue.config.productionTip = false

new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
