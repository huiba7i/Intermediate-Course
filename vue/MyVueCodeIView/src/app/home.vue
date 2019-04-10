<template>
  <el-container>
    <el-header>
      <mymenu></mymenu>
    </el-header>

    <div class="showOrHide">
      <div class="content">
        <div class="breadcrumb">
          <el-breadcrumb separator="|">
            <el-breadcrumb-item>当季</el-breadcrumb-item>
            <el-breadcrumb-item>全部</el-breadcrumb-item>
          </el-breadcrumb>
        </div>

        <div class="carousel">
          <el-carousel :interval="3000" type="card" height="300px">
            <el-carousel-item v-for="(item,i) in pictures" :key="i">
              <!-- 走马灯可以根据图片的id，转到相应的详情页面 -->
              <router-link :to="'/details/'+item.id">
                <img :src="item.src" :alt="item.alt" class="picture-size">
              </router-link>
            </el-carousel-item>
          </el-carousel>
        </div>

        <el-container class="con-conteainer">
          <el-aside width="20%">
            <el-collapse v-model="food" accordion @change="foodList">
              <el-collapse-item
                v-for="item in fourSeasons"
                :key="item.id"
                :title="item.seasons"
                :name="item.id"
              >
                <el-tag
                  class="tag-dishName"
                  type="success"
                  size="small"
                  v-for="(item,i) in dishName"
                  :key="i"
                  v-show="dishName.length>0"
                >
                  <router-link
                    :to="'/details/'+item.name"
                    class="tag-dishName-color"
                  >{{ item.name }}</router-link>
                </el-tag>
              </el-collapse-item>
            </el-collapse>
          </el-aside>
          <el-main>
            <el-row v-show="$route.meta.showContent">
              <el-col
                class="col-card-box"
                :span="5"
                v-for="(p,index) in pictureDishes"
                :key="index"
              >
                <el-card class="card-box">
                  <img :src="p.src" :alt="p.title" class="card-picture">
                  <div style="padding: 14px;">
                    <router-link class="card-title" :to="'/details/'+p.title">{{ p.title }}</router-link>
                    <time>{{ p.time }}</time>
                  </div>
                </el-card>
              </el-col>
            </el-row>
            <router-view name="showFoodDetails"></router-view>
          </el-main>
        </el-container>
      </div>
    </div>

    <el-footer>
      <nav class="fooder-nav">
        <a>Element</a>
        <a>Element</a>
        <a>Element</a>
        <a>Element</a>
        <router-link to="backstageLogin">后台登录</router-link>
      </nav>
    </el-footer>
  </el-container>
</template>

<script>
import menu from "./menu";
export default {
  data() {
    return {
      food: "",
      dishName: [],
      pictures: [
        { src: "../static/imgs/home/1.jpg", alt: "picture", id: 1 },
        { src: "../static/imgs/home/2.jpg", alt: "picture", id: 2 },
        { src: "../static/imgs/home/3.jpg", alt: "picture", id: 3 },
        { src: "../static/imgs/home/4.jpg", alt: "picture", id: 4 },
        { src: "../static/imgs/home/5.jpg", alt: "picture", id: 5 },
        { src: "../static/imgs/home/6.jpg", alt: "picture", id: 6 }
      ],
      fourSeasons: [
        { id: 1, seasons: "春" },
        { id: 2, seasons: "夏" },
        { id: 3, seasons: "秋" },
        { id: 4, seasons: "冬" }
      ],
      listOfSeasons: [
        {
          id: 1,
          food: [
            { name: "春季菜品1" },
            { name: "春季菜品2" },
            { name: "春季菜品3" },
            { name: "春季菜品1" },
            { name: "春季菜品2" },
            { name: "春季菜品3" },
            { name: "春季菜品1" },
            { name: "春季菜品2" },
            { name: "春季菜品3" },
            { name: "春季菜品1" },
            { name: "春季菜品2" },
            { name: "春季菜品3" }
          ]
        },
        {
          id: 2,
          food: [
            { name: "夏季菜品1" },
            { name: "夏季菜品2" },
            { name: "夏季菜品3" }
          ]
        },
        {
          id: 3,
          food: [
            { name: "秋季菜品1" },
            { name: "秋季菜品2" },
            { name: "秋季菜品3" }
          ]
        },
        {
          id: 4,
          food: [
            { name: "冬季菜品1" },
            { name: "冬季菜品2" },
            { name: "冬季菜品3" }
          ]
        }
      ],
      pictureDishes: [
        {
          src: "../static/imgs/home/296974.jpg",
          title: "美味汉堡",
          time: "2019-04-09"
        },
        {
          src: "../static/imgs/home/296974.jpg",
          title: "美味汉堡",
          time: "2019-04-09"
        },
        {
          src: "../static/imgs/home/296974.jpg",
          title: "美味汉堡",
          time: "2019-04-09"
        },
        {
          src: "../static/imgs/home/296974.jpg",
          title: "美味汉堡",
          time: "2019-04-09"
        },
        {
          src: "../static/imgs/home/296974.jpg",
          title: "美味汉堡",
          time: "2019-04-09"
        },
        {
          src: "../static/imgs/home/296974.jpg",
          title: "美味汉堡",
          time: "2019-04-09"
        },
        {
          src: "../static/imgs/home/296974.jpg",
          title: "美味汉堡",
          time: "2019-04-09"
        },
        {
          src: "../static/imgs/home/296974.jpg",
          title: "美味汉堡",
          time: "2019-04-09"
        },
        {
          src: "../static/imgs/home/296974.jpg",
          title: "美味汉堡",
          time: "2019-04-09"
        },
        {
          src: "../static/imgs/home/296974.jpg",
          title: "美味汉堡",
          time: "2019-04-09"
        },
        {
          src: "../static/imgs/home/296974.jpg",
          title: "美味汉堡",
          time: "2019-04-09"
        },
        {
          src: "../static/imgs/home/296974.jpg",
          title: "美味汉堡",
          time: "2019-04-09"
        },
        {
          src: "../static/imgs/home/296974.jpg",
          title: "美味汉堡",
          time: "2019-04-09"
        },
        {
          src: "../static/imgs/home/296974.jpg",
          title: "美味汉堡",
          time: "2019-04-09"
        },
        {
          src: "../static/imgs/home/296974.jpg",
          title: "美味汉堡",
          time: "2019-04-09"
        },
        {
          src: "../static/imgs/home/296974.jpg",
          title: "美味汉堡",
          time: "2019-04-09"
        }
      ]
    };
  },
  methods: {
    foodList(e) {
      if (this.listOfSeasons[e - 1].id == e) {
        this.dishName = this.listOfSeasons[e - 1].food;
      }
    }
  },
  components: {
    mymenu: menu
  }
};
</script>

<style scoped>
.breadcrumb,
.carousel,
.con-conteainer {
  padding: 20px 0;
}
.picture-size {
  width: 100%;
  height: 100%;
}
.tag-dishName {
  margin: 5px;
}
.tag-dishName-color {
  color: #67c23a;
}
.card-picture {
  width: 100%;
  display: block;
}
.col-card-box {
  margin: 0 20px 30px;
}
.card-title {
  display: block;
  font-size: 16px;
  margin: 10px;
}
.inside-container {
  padding: 20px 100px 0;
}
.main {
  padding: 0;
}
.fooder-nav {
  font-size: 14px;
  margin: 20px 0;
}
.fooder-nav a {
  margin: 0 20px;
}
.content {
  margin: 20px 100px;
}
</style>