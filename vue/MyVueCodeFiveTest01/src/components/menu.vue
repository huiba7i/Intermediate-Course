<template>
  <div>
    <el-menu
      :default-active="this.$route.path"
      router
      @select="handleSelect"
      class="el-menu-demo"
      mode="horizontal"
    >
      <el-menu-item v-for="(item,i) in navList" :key="i" :index="item.name">
        {{ item.navItem }}
      </el-menu-item>
        <el-menu-item index="7">
          <a class="el-menu-item" @click="clear">注销</a>
        </el-menu-item>
    </el-menu>
  </div>
</template>

<script>
export default {
  data() {
    return {
      activeIndex: "1",
      username: null,
      navList: [
        { name: "/", navItem: "首页" },
        { name: "/log", navItem: "登录" },
        { name: "/reg", navItem: "注册" },
        { name: "/one", navItem: "One" },
        { name: "/two", navItem: "Two" },
        { name: "/user", navItem: "用户列表" },
        { name: '/paging', navItem: "分页" }
      ]
    };
  },
  methods: {
    clear() {
      let r = confirm(`确定注销${this.username}吗？`);

      if (r) {
        localStorage.clear();
        if (this.username == null) {
          this.$router.push("/");
        }
      }
    },
    handleSelect(key, keyPath) {
      // console.log(key, keyPath);
    }
  },
  mounted() {
    this.username = localStorage.getItem("login_username");
    // console.log(this.username);
  }
};
</script>

<style>
</style>


