<template>
  <div class="layout-box">
    <!-- 页眉 -->
    <header class="header">
      <div class="logo">Logo</div>
      <ul>
        <li>
          <Icon type="ios-chatboxes-outline" size="20"/>
          <span class="msg">消息</span>
        </li>
        <li>
          <span>
            欢迎<span class="user-name">{{ backName }}</span>登录
          </span>
        </li>
        <li>
          <Icon :style="{cursor:'pointer'}" @click="signOut" type="ios-log-out" size="20"/>
        </li>
      </ul>
    </header>
    <!-- 侧边栏 -->
    <article class="sider">
      <div class="sider-box">
        <Menu :theme="theme2" :open-names="['2']" class="menu-background-color">
          <MenuItem name="1">
            <Icon type="ios-home"/>
            <span class="home" @click="home">首页</span>
          </MenuItem>
          <Submenu name="2">
            <template slot="title">
              <Icon type="ios-paper"/>内容管理
            </template>
            <MenuItem name="1-1">文章管理</MenuItem>
            <MenuItem name="1-2">评论管理</MenuItem>
            <MenuItem name="1-3">举报管理</MenuItem>
          </Submenu>
          <Submenu name="3">
            <template slot="title">
              <Icon type="ios-people"/>用户管理
            </template>
            <MenuItem name="2-1">新增用户</MenuItem>
            <MenuItem name="2-2">活跃用户</MenuItem>
          </Submenu>
          <Submenu name="4">
            <template slot="title">
              <Icon type="ios-stats"/>统计分析
            </template>
            <MenuGroup title="使用">
              <MenuItem name="3-1">新增和启动</MenuItem>
              <MenuItem name="3-2">活跃分析</MenuItem>
              <MenuItem name="3-3">时段分析</MenuItem>
            </MenuGroup>
            <MenuGroup title="留存">
              <MenuItem name="3-4">用户留存</MenuItem>
              <MenuItem name="3-5">流失用户</MenuItem>
            </MenuGroup>
          </Submenu>
        </Menu>
      </div>
    </article>
    <!-- 主题内容 -->
    <div class="content-layout">
      <router-view name="backContent"></router-view>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      backName: sessionStorage.getItem("bName"),
      theme2: "light"
    };
  },
  methods: {
    home(){
      this.$router.push('/homeCharts');
    },
    signOut(){
      this.$router.push('/');
      sessionStorage.clear();
    }
  },
  mounted(){
    this.$router.push('/homeCharts');
  }
};
</script>

<style scoped>
/* 整体 */
.layout-box {
  position: relative;
  background-color: white;
}
/* 页眉 */
.header {
  background-color: white;
  width: 100%;
  height: 80px;
  line-height: 80px;
  position: fixed;
  top: 0;
  left: 0;
}
.logo {
  float: left;
  margin-left: 100px;
  color: blue;
}
.header ul {
  float: right;
}
.header ul li {
  list-style-type: none;
  float: left;
  width: 120px;
  height: 80px;
  line-height: 80px;
  color: #aaa;
  font-size: 14px;
}
.msg {
  margin-left: 5px;
}
.user-name {
  margin: 0 5px;
  color: #5cadff;
}

/* 侧边栏 */
.sider {
  width: 300px;
  position: fixed;
  top: 80px;
  left: 0;
}
.home {
  letter-spacing: 25px;
}
.menu-background-color{
  margin: 40px 20px 0;
  background-color: white;
}

/* 内容 */
.content-layout {
  background-color: rgb(246, 248, 255);
  padding: 80px 0 0 300px;
}
</style>
