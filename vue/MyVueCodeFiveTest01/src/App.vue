<template>
  <div id="app">
    <div class="row row-margin">
      <div class="col-md-12 col-md-offset-0">
        <mymenu/>
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
