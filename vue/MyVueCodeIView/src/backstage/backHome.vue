<template>
  <div class="layout-box">
    <!-- 页眉 -->
    <header class="header">
      <div class="logo">
        <img src="https://file.iviewui.com/dist/e1cf12c07bf6458992569e67927d767e.png">
      </div>
      <ul>
        <li>
          <Icon type="ios-chatboxes-outline" size="20"/>
          <span class="msg">消息</span>
        </li>
        <li>
          <span>
            欢迎
            <span class="user-name">{{ backName }}</span>登录
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
        <Menu :theme="theme2" :open-names="['2']" class="menu-background-color" accordion>
          <MenuItem name="1">
            <Icon type="ios-home"/>
            <span class="home" @click="()=>{$router.push('/homeCharts')}">首页</span>
          </MenuItem>
          <Submenu name="2">
            <template slot="title">
              <Icon type="ios-paper"/>内容管理
            </template>
            <MenuItem name="1-1">
              <span @click="()=>{$router.push('/dish')}">信息管理</span>
            </MenuItem>
            <MenuItem name="1-2">
              <span @click="()=>{$router.push('/comment')}">评论管理</span>
            </MenuItem>
          </Submenu>
          <Submenu name="3">
            <template slot="title">
              <Icon type="ios-people"/>用户管理
            </template>
            <MenuItem name="2-1">
              <span @click="()=>{$router.push('/addUser')}">新增用户</span>
            </MenuItem>
            <MenuItem name="2-2">
            <span @click="()=>{$router.push('/dish')}">修改用户</span>
            </MenuItem>
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
          <Submenu name='5'>
            <template slot="title">
              <Icon type="ios-paper"/>文章管理
            </template>
            <MenuItem name="5-1">
              <span @click="()=>{$router.push('uploadFile')}">新增文件</span>
            </MenuItem>
            <MenuItem name="5-2">
              <span @click="()=>{$router.push('uploadImg')}">新增图片</span>
            </MenuItem>
            <MenuItem name="5-3">
              <span @click="()=>{$router.push('uploadCon')}">新增内容</span>
            </MenuItem>
          </Submenu>
        </Menu>
      </div>
    </article>
    <!-- 主题内容 -->
    <div class="content-layout" id="content-layout" ref="page">
      <router-view name="backContent"></router-view>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      screenHeight: document.documentElement.clientHeight, // 屏幕高度
      backName: sessionStorage.getItem("bName"),
      theme2: "light"
    };
  },
  methods: {
    signOut() {
      this.$router.push("/");
      sessionStorage.clear();
    },
    // 改变高度
    changeFixed(screenHeight) {
      if (this.$refs.page) {
        this.$refs.page.style.minHeight = screenHeight + "px";
      }
    }
  },
  watch: {
    screenHeight() {
      this.changeFixed(this.screenHeight);
    }
  },
  mounted() {
    this.$router.push("/homeCharts");
    
    let that = this;
    window.onresize = function() {
      this.screenHeight = `${document.documentElement.clientHeight}`;
      if (that.$refs.page) {
        that.$refs.page.style.minHeight = screenHeight + "px";
      }
    };
  }
};
</script>

<style scoped>
/* 整体 */
.layout-box {
  height: 100%;
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
  z-index: 100;
}
.logo {
  width: 115px;
  height: 50px;
  margin-top: 15px;
  float: left;
  margin-left: 100px;
  color: blue;
}
.logo img {
  width: 100%;
  height: 100%;
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
  z-index: 100;
}
.home {
  letter-spacing: 25px;
}
.menu-background-color {
  margin: 40px 20px 0;
  background-color: white;
}
.sider-box {
  margin-left: 30px;
}

/* 内容 */
.content-layout {
  background-color: #e9ecf3;
  padding: 80px 0 250px 300px;
  z-index: 1;
}
</style>
