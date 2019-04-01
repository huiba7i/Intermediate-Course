import Vue from 'vue'

Vue.config.productionTip = false

let vm = new Vue({
  el: '#app',
  data: {
    msg: 'Vue',
    food: [
      {name: "黄焖熊鸡", price: 20, num: 1 },
      {name: "黄焖熊鸡", price: 20, num: 2 },
      {name: "黄焖熊鸡", price: 20, num: 3 },
      {name: "黄焖熊鸡", price: 30, num: 4 }
    ]
  },
  watch: {
    msg: function(newVal, oldVal){
      console.log('msg更新之前值为:',newVal, ',更新之后值为:', oldVal);
    }
  },
  methods: {
    destroyVue: function(){
      this.$destroy(); // 手动销毁Vue实例
    }
  },
  computed: {
    totalPrice: function(){
      let result = 0;
      for ( let f of this.food ){
        result += f.price*f.num;
      }
      return result;
    }
  },
  beforeCreate(){
    console.error('创建之前');
    console.log('data选项属性: ', this.$data);
    console.log('挂载的el属性: ', this.$el)
    console.log('监听: ', this.$options.watch);
    console.log('methods事件处理器: ', this.$options.methods);
  },
  created(){
    console.error('创建之后');
    console.log('data选项属性: ', this.$data);
    console.log('挂载的el属性: ', this.$el)
    console.log('监听: ', this.$options.watch);
    console.log('methods事件处理器: ', this.$options.methods);
  },
  beforeMount(){
    console.error('渲染之前');
    console.log('data选项属性: ', this.$data);
    console.log('挂载的el属性: ', this.$el)
    console.log('监听: ', this.$options.watch);
    console.log('methods事件处理器: ', this.$options.methods);
  },
  mounted(){
    console.error('渲染之后');
    console.log('data选项属性: ', this.$data);
    console.log('挂载的el属性: ', this.$el)
    console.log('监听: ', this.$options.watch);
    console.log('methods事件处理器: ', this.$options.methods);
  },
  beforeUpdate(){
    console.error('更新之前');
    console.log('data选项属性: ', this.$data);
    console.log('挂载的el属性: ', this.$el)
    console.log('监听: ', this.$options.watch);
    console.log('methods事件处理器: ', this.$options.methods);
  },
  updated(){
    console.error('更新之后');
    console.log('data选项属性: ', this.$data);
    console.log('挂载的el属性: ', this.$el)
    console.log('监听: ', this.$options.watch);
    console.log('methods事件处理器: ', this.$options.methods);
  },
  befordDestroy(){
    console.error('销毁之前');
    console.log('data选项属性: ', this.$data);
    console.log('挂载的el属性: ', this.$el)
    console.log('监听: ', this.$options.watch);
    console.log('methods事件处理器: ', this.$options.methods);
  },
  destroyed(){
    console.error('销毁之后');
    console.log('data选项属性: ', this.$data);
    console.log('挂载的el属性: ', this.$el)
    console.log('监听: ', this.$options.watch);
    console.log('methods事件处理器: ', this.$options.methods);
  }
})
