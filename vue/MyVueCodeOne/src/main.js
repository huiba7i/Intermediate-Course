import Vue from 'vue'
import $ from 'jquery'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.js'

// 阻止启动生产消息，常用作指令。
Vue.config.productionTip = false

var vm = new Vue({
  el: '#app',
  data: {
    all: false,
    username: '',
    userage: '',
    userData: []
  },
  methods: {
    submit(){
      vm.userData.push({ "name":this.username, "age":this.userage });
      this.username = '';
      this.userage = '';
    },
    del(){
      $('#myModal').modal('show');
    },
    confirm(event){
      if ( vm.all == true )
      {
        vm.userData = [];
        vm.all = false;
      }
      else
      {
        this.userData.splice(event.index, 1);
      }
      $('#myModal').modal('hide');
    },
    delAll(){
      $('#myModal').modal('show');
      vm.all = true;
    }
  }
})
