<template>
  <el-row class="row">
    <el-col :span="24" class="col">
      <div class="img-box">
        <img
          :src="'/static/imgs/imgs/'+getDate['question-title-src']"
          :title="getDate.title"
          class="det-img"
        >
        <p>{{ getDate.title }}</p>
      </div>
      <div class="content-box">
        <div class="title">
          <img :src="'/static/imgs/imgs/'+getDate.image" :alt="getDate.title" class="title-img">
          <span class="author">{{ getDate.author }}</span>
        </div>
        <div class="content" v-html="getDate.content"></div>
        <hr class="hr">
        <div class="reference">
          <p v-for="(item, i) in getDate.schema" :key="i">{{item}}</p>
        </div>

        <div class="botton-img">
          <img v-for="(imgs, i) in getDate.images" :key="i" :src="'/static/imgs/imgs/'+imgs">
        </div>

        <div class="interlocution">
          <div v-for="(item, i) in getDate.questions" :key="i">
            <ul>
              <li>
                <h1>{{ item['question-title'] }}</h1>
              </li>
              <li>
                  <img :src="'/static/imgs/imgs/'+item['question-title-src']">
                  <b>{{ item.author }},</b>
                  <span>{{ item.bio }}</span>
              </li>
              <li>
                  <p class="item-content" v-html="item.content"></p>
              </li>
              <li>
                  <a :href="item['view-more']">查看知乎原文评论</a>
              </li>
            </ul>
          </div>
        </div>

        <div class="comment">
          <span class="comment-title" @click="viewComments">查看知乎评论</span>
        </div>
        <div class="comment-box" v-show="showComment">
          <span>评论({{number}})</span>
          <div class="comment-info" v-for="item in getCommentDate.comments" :key="item.id">
            <ul>
              <li>{{ item.author }}</li>
              <li>{{ (parseInt(Number(item.time)/1000/60/60/24)+'天前') }}</li>
              <li>{{ item.content }}</li>
            </ul>
          </div>
        </div>
      </div>
    </el-col>
  </el-row>
</template>

<script>
export default {
  data() {
    return {
      getDate: {},
      getCommentDate: [],
      showComment: false
    };
  },
  methods: {
    getzhDate(name) {
      this.$axios
        .get(`/static/data/${this.$route.params.id}-${name}.json`)
        .then(resp => {
          if (name == "news") {
            this.getDate = resp.data;
          } else {
            this.getCommentDate = resp.data;
          }
        })
        .catch(error => {
          console.log(error);
        });
    },
    viewComments() {
      if (this.showComment == false) {
        this.showComment = true;
        this.getzhDate("comment");
      } else {
        this.showComment = false;
      }
    }
  },
  beforeMount() {
    this.getzhDate("news");
  },
  computed: {
    number: function() {
      let number = 0;
      if (this.getCommentDate != "") {
        number = this.getCommentDate.comments.length;
      }
      return number;
    }
  },
  watch: {
    $route: function(val, oldVal) {
      if (val != oldVal) {
        this.getzhDate("news");
        this.showComment = false;
      }
    }
  }
};
</script>

<style scoped>
.content-box {
  margin: 20px;
}
.row {
  margin-left: 25%;
}
.col {
  width: 65%;
  height: 30%;
  background-color: white;
}
.img-box {
  position: relative;
  text-align: center;
}
.img-box p {
  width: 100%;
  text-align: center;
  font-size: 30px;
  font-family: "黑体";
  font-weight: 900;
  color: white;
  position: absolute;
  left: auto;
  bottom: 30px;
}
.det-img {
  width: 100%;
  height: 100%;
}
.title {
  text-align: left;
}
.author {
  font-size: 16px;
  font-weight: 600;
}
.title-img {
  vertical-align: middle;
}
.content {
  font-size: 16px;
  line-height: 30px;
  text-align: start;
}
.hr {
  margin: 20px 0;
}
.reference {
  text-align: start;
}
.reference p {
  font-size: 15px;
}
.comment {
  width: 100%;
  height: 30px;
  background-color: #f4f6f8;
  text-align: center;
  margin: 10px 0;
}
.comment-title {
  font-size: 16px;
  line-height: 30px;
  color: #6e788a;
  cursor: pointer;
}
.comment-box {
  text-align: start;
}
.comment-box span {
  display: block;
  margin: 20px 10px;
}
.comment-info ul {
  margin-bottom: 20px;
  border-bottom: 1px solid #ddd;
}
.comment-info ul li {
  font-size: 16px;
  list-style-type: none;
  margin: 10px 0 10px 20px;
}
.comment-info ul li:nth-child(2) {
  font-size: 12px;
  color: #ccc;
  margin-top: 0;
}
.botton-img {
  width: 100%;
  height: 100%;
}
.botton-img img {
  width: 100%;
  height: 100%;
}
.interlocution {
  margin-bottom: 10px;
}
.interlocution ul {
  margin-bottom: 50px;
  margin-left: 20px;
}
.interlocution ul li {
  list-style-type: none;
  text-align: start;
  margin: 15px 0;
}
.interlocution ul li:nth-child(2){
    font-size: 14px;
}
.interlocution ul li:nth-child(2) img{
    height: 20px;
    width: 20px;
    vertical-align: bottom;
}
.item-content{
    font-size: 18px;
}
.interlocution ul li:last-child{
    text-align: right;
}
</style>
