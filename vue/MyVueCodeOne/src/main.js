import Vue from 'vue'
import $ from 'jquery'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.js'
import './css/style.css'

// 阻止启动生产消息，常用作指令。
Vue.config.productionTip = false

var vm = new Vue({
  el: '#app',
  data: {
    delIndex: 0,
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
    del(index){
      $('#myModal').modal('show');
      vm.delIndex = index;
    },
    delAll(){
      $('#myModal').modal('show');
      vm.all = true;
    },
    confirm(){
      if ( vm.all == true )
      {
        vm.userData = [];
        vm.all = false;
      }
      else
      {
        vm.userData.splice(vm.delIndex, 1);
      }
      $('#myModal').modal('hide');
    }
  },
  filters: {
    charAt: function(value){
      return value.charAt(0);
    },
    toFixed: function(value, size){
      return value.toFixed(size);
    },
    concat: function(value){
      return value.concat('岁');
    }
  },
  directives: {
    focus: {
      inserted: function(el, binding){
        el.focus();
      }
    }
  }
})
