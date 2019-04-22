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

    <el-menu-item class="search">
      <el-input
        size="small"
        v-model="search"
        placeholder="请输入菜品名称"
        suffix-icon="el-icon-search"
        @change="searchInfo"
      ></el-input>
    </el-menu-item>

    <el-menu-item class="user" v-if="userName!=null">
      欢迎
      <span>{{ userName }}</span>登录
    </el-menu-item>
  </el-menu>
</template>

<script>
export default {
  data() {
    return {
      search: "",
      userName: sessionStorage.getItem("uName"),
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
        { name: "/reg", navItem: "注册" },
        { name: "/zh", navItem: "知乎日报" }
      ]
    };
  },
  methods: {
    searchInfo(event) {
      this.$emit('getSearchData', event);
    }
  }
};
</script>


<style scoped>
.el-menu-item.is-active {
  color: #409eff;
  border-right: none;
}
.user {
  float: right;
  color: #555;
  margin-right: 20px;
}
.search {
  float: right;
  margin-right: 50px;
}
</style>
