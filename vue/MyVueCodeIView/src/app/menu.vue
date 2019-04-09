<template>
  <el-menu :default-active="this.$route.path" router class="el-menu-demo" mode="horizontal">
    <el-menu-item
      v-for="(item,k) in navList"
      :key="'single'+k"
      v-show="!item.second"
      :index="item.name"
    >{{ item.navItem }}</el-menu-item>
    <el-submenu v-for="(item,i) in navList" :key="i" v-show="item.second" :index="item.name">
      <template slot="title">{{ item.navItem }}</template>
      <el-menu-item v-for="(sec,j) in item.second" :key="j" :index="sec.name">{{ sec.navItem }}</el-menu-item>
    </el-submenu>
  </el-menu>
</template>

<script>
export default {
  data() {
    return {
      navList: [
        { name: "/", navItem: "首页" },
        {
          name: "/classify",
          navItem: "分类",
          second: [
            { name: "/form", navItem: "表单" },
            { name: "/table", navItem: "表格" }
          ]
        },
        { name: "/login", navItem: "登录" },
        { name: "/reg", navItem: "注册" }
      ]
    };
  }
};
</script>
