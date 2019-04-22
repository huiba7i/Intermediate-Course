<template>
  <el-container>
    <el-header>
      <mymenu @getSearchData="getSearchInfo"></mymenu>
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
            <el-collapse v-model="food" accordion @change="seasonsDeatils">
              <el-collapse-item
                v-for="(item,i) in fourSeasons"
                :key="item.parentId"
                :title="item.name"
                :name="i"
              >
                <el-tag
                  class="tag-dishName"
                  type="success"
                  size="small"
                  v-for="(item,i) in singleDetails"
                  :key="i"
                  v-show="singleDetails.length>0"
                >
                  <router-link :to="'/details/'+item.id" class="tag-dishName-color">{{ item.name }}</router-link>
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
                  <img :src="p.albums" :alt="p.title" class="card-picture">
                  <div style="padding-top: 15px;" class="card-title-box">
                    <router-link class="card-title" :to="'/singleDetails/'+p.id">{{ p.title }}</router-link>
                  </div>
                </el-card>
              </el-col>
            </el-row>
            <transition :name="transitionName">
              <router-view name="showFoodDetails"></router-view>
            </transition>
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
      transitionName: "slide-left",
      food: "",
      pictures: [
        { src: "../static/imgs/home/1.jpg", alt: "picture", id: 1 },
        { src: "../static/imgs/home/2.jpg", alt: "picture", id: 2 },
        { src: "../static/imgs/home/3.jpg", alt: "picture", id: 3 },
        { src: "../static/imgs/home/4.jpg", alt: "picture", id: 4 },
        { src: "../static/imgs/home/5.jpg", alt: "picture", id: 5 },
        { src: "../static/imgs/home/6.jpg", alt: "picture", id: 6 }
      ],
      // 菜品分类标签列表
      fourSeasons: [],
      // 菜品分类总列表详情
      categoryDeatils: [],
      // 菜品分类单个列表详情
      singleDetails: [],
      // 首页菜品
      pictureDishes: []
    };
  },
  mounted() {
    this.getCategory();
  },
  methods: {
    seasonsDeatils(e) {
      this.singleDetails = this.categoryDeatils[e];
    },
    // 分类标签列表
    getCategory() {
      this.$axios
        .get("/cook/category?key=7515e14ef149b000386b01f808e5d9f6")
        .then(resp => {
          // console.log(resp);
          this.fourSeasons = resp.data.result;
          for (let f of this.fourSeasons) {
            this.categoryDeatils.push(f.list);
          }
          // console.log(this.categoryDeatils);
        })
        .catch(error => {
          console.error(error);
        });
    },
    getSearchInfo(msg) {
      this.$axios
        .get(
          `/cook/query?menu=${msg}&key=${"7515e14ef149b000386b01f808e5d9f6"}`
        )
        .then(resp => {
          // console.log(resp);
          this.pictureDishes = resp.data.result.data;
        })
        .catch(error => {
          console.error(error);
        });
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
  margin: 10px 10px 0;
}
.card-title-box {
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 1;
  padding-top: 15px;
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