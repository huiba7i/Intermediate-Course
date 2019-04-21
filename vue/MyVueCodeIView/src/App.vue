<template>
  <div id="app">
    <transition :name="transitionName">
      <router-view name="defaultHome"/>
    </transition>
  </div>
</template>

<script>
export default {
  name: "App",
  data(){
    return{
      transitionName: 'slide-left'
    }
  },
  beforeRouteUpdate(){
    const toDepth = to.path.split('/').length
    const fromDepth = from.path.split('/').length
    this.transitionName = toDepth < fromDepth ? 'slide-right' : 'slide-left'
    next()
  }
};
</script>

<style>
body,html,#app{
  height: 100%;
}
#app {
  font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB",
    "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
p{
    margin: 20px 0;
}
</style>
