import Vue from 'vue'
import HelloWorld from './components/HelloWorld.vue'

Vue.config.productionTip = false

// // 全局组件
// Vue.components('myHTML', {
//   template: "<h1>全局组件<hr><ol><li>heheheh</li></ol></h1>"
// });

// 局部组件
let myComponet = {
  template: "<div><h1>局部组件<hr><ul><li>{{ msg }}</li></ul></h1></div>",
  data() {
    return {
      msg: "局部组件里的data必须是个函数"
    }
  }
}
let myNumber = {
  data() {
    return {
      count: 0
    }
  },
  template: "<button @click='count++'>点我哦！{{ count }}</button>"
}
let blogPost = {
  data() {
    return {
      posts: [
        { id: 1, title: 'My journey with Vue' },
        { id: 2, title: 'Blogging with Vue' },
        { id: 3, title: 'Why Vue is so fun' }
      ],
      s: {
        backgroundColor: '#eee',
        color: 'black'
      }
    }
  },
  template: "<div v-bind:style='s'><h3 v-for='post in posts' v-bind:key='post.id' v-bind:title='post.title'>{{post.title}}</h3></div>"
}

new Vue({
  el: '#app',
  data: {

  },
  components: {
    'my-componet': myComponet,
    'my-number': myNumber,
    'blog-post': blogPost,
    'hello-world': HelloWorld
  },
  template:  '<hello-world/>' 
})
