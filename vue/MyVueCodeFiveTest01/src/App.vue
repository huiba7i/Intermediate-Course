<template>
  <div id="app">
    <div class="row row-margin">
      <div class="col-md-12 col-md-offset-0">
        <mymenu/>
        <!-- 定义路由导航 -->
        <!-- <router-link to="log" class="btn btn-default">登录</router-link>
        <router-link to="reg" class="btn btn-default">注册</router-link> -->
      </div>
    </div>
    <!-- 当路由匹配组件时，将组件渲染到该标记中 -->
    <router-view></router-view>
  </div>
</template>

<script>
import Menu from './components/menu'

export default {
  name: "App",
  components: {
    mymenu: Menu
  }
};
</script>

<style scoped>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-left: auto;
  margin-right: auto;
}
.row-margin{
  margin: 0 0 40px 0;
}
</style>
