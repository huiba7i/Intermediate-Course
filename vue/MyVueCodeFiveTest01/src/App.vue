<template>
  <div id="app">
    <el-container>
      <el-header>
        <mymenu/>
      </el-header>
      <el-container class="main-width">
        <el-main>
          <router-view></router-view>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import Menu from "./components/menu";

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
.row-margin {
  margin: 0 0 40px 0;
}
.main-width{
  width: 80%;
  margin: auto;
}
</style>
