import Vue from 'vue'
import App from './App'
import 'bootstrap/dist/css/bootstrap.min.css'
import router from './router/index'
import store from './store/index'
import qs from 'querystring'

import axios from 'axios'
Vue.prototype.$axios = axios;

Vue.config.productionTip = false

new Vue({
  el: '#app',
  components: { App },
  template: '<App/>',
  router: router,
  store: store
})
