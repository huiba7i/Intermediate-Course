import Vue from 'vue'
import axios from 'axios'
import qs from 'querystring'
import $ from 'jquery'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.js'

Vue.config.productionTip = false

let vm = new Vue({
  el: '#app',
  data: {
    all: false,         // 记录删除单条或全部的数据状态
    delIndex: 0,        // 表格下标
    delStuid: 0,        // 后台数据字段下标
    items: [],          // 存储本地数据数组
    backstageData: [],   // 存储后端数据数组
    name: '',
    sex: '',
    age: ''
  },
  created(){
    console.log('创建');
    // 后端数据
    axios.get('/deal/data').then((resp)=>{ 
      // console.log('封装了整个响应对象的结果：', resp);
      vm.backstageData = resp.data;
    }).catch((error)=>{
      console.error('请求失败：', error);
    });
  },
  methods: {
    visit(){
      axios.get('/deal/data').then((resp)=>{
        // console.log('封装了整个响应对象的结果：', resp);
        vm.backstageData = resp.data;
      }).catch((error)=>{
        console.error('请求失败：', error);
      });
    },
    // 提交数据
    submit(){
      axios.post('/deal/add', qs.stringify({
        name: vm.name,
        sex: vm.sex,
        age: vm.age
      })).then((resp)=>{
        this.visit();
        vm.name = '';
        vm.sex = '';
        vm.age = '';
        console.log(resp);
      }).catch((error)=>{
        console.error('请求失败：', error);
      });
    },
    // 删除单条数据按钮
    del(index, stuid){
      $('#myModal').modal('show');
      vm.delIndex = index;
      vm.delStuid = stuid; 
    },
    // 删除全部数据按钮
    delAll(){
      $('#myModal').modal('show');
      vm.all = true;
    },
    // 确认按钮
    confirm(){
      // vm.all状态未true删除全部数据，false删除单挑数据
      if ( vm.all == true )
      {
        // 全部删除待定
        vm.all = false;
      }
      else
      {
        axios.get('/deal/delete?stuid='+vm.delStuid).then((resp)=>{
          vm.backstageData.splice(vm.delIndex, 1);
        }).catch((error)=>{
          console.error('请求失败：', error);
        });
      }
      $('#myModal').modal('hide');
    },
    // 本地数据
    test(){
      axios.get('/static/1.txt').then((resp)=>{
        console.log('封装了整个响应对象的结果：', resp);
        vm.items = resp.data;
      }).catch((error)=>{
        console.error('请求失败：', error);
      });
    }
  }
})
