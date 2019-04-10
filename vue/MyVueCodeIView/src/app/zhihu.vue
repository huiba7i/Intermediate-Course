<template>
  <div class="zh-content">
    <el-row>
      <!-- 左 -->
      <el-col :xs="24" :sm="24" :md="6" :lg="4" :xl="4">
        <el-menu
          :default-active="activeIndex"
          class="el-menu-demo"
          mode="vertical"
          background-color="#F4F6F8"
        >
          <el-menu-item index="1">每日推荐</el-menu-item>
          <el-menu-item index="2">主题日报</el-menu-item>
        </el-menu>
      </el-col>
      <!-- 中 -->
      <el-col :xs="8" :sm="8" :md="8" :lg="6" :xl="6">
        <el-menu mode="vertical" :default-active="newListIndex" class="center-menu">
          <h2>{{ newList.date }}</h2>
          <el-menu-item
            class="no-active"
            v-for="item in newList.stories"
            :index="'i'+item.id"
            :key="item.id"
            :style="{ paddingLeft: '0px' }"
          >
            <el-row>
              <el-col :xs="24" :sm="24" :md="8" :lg="8" :xl="8">
                <img :src="'../static/imgs/imgs/'+item.images" :alt="item.title" class="menu-img">
              </el-col>
              <el-col :xs="24" :sm="24" :md="16" :lg="16" :xl="16" class="title">
                <router-link :to="'/zhdetails/'+item.id" :title="item.title">{{ item.title }}</router-link>
              </el-col>
            </el-row>
          </el-menu-item>
        </el-menu>
      </el-col>
      <!-- 右 -->
      <el-col :xs="16" :sm="16" :md="10" :lg="14" :xl="14" class="col-right">
        <router-view name="zhihuDetails"></router-view>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  data() {
    return {
      activeIndex: "1",
      newListIndex: "1",
      newList: []
    };
  },
  methods: {
    getDate() {
      this.$axios
        .get("../static/data/news.json")
        .then(resp => {
          this.newList = resp.data;
        })
        .catch(error => {
          console.log(error);
        });
    }
  },
  created() {
    this.getDate();
  }
};
</script>

<style scoped>
.zh-content {
  margin-top: 1px;
}
.el-menu-item {
  box-sizing: border-box;
}
.el-menu-item.is-active {
  color: #409eff;
  border-bottom: 2px solid;
  box-sizing: border-box;
}
.no-active {
  border: none;
  height: 100%;
  margin: 10px 20px;
  padding: 0;
  box-sizing: border-box;
}
.menu-img {
  width: 100px;
  height: 100px;
  margin: 10px;
}
.title {
  text-align: left;
  text-overflow: ellipsis;
  overflow: hidden;
}
.center-menu {
  box-sizing: border-box;
}
.col-right {
  background-color: #f5f5f5;
}
</style>
