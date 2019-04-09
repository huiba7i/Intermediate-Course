<template>
  <div>
    <el-row>
      <el-col :xs="24" :sm="24" :md="5" :lg="5" :xl="3" :offset="1" class="input-bottom">
        <div class="demo-input-suffix">
          <el-input placeholder="请输入内容" v-model="searchPhone">
            <i slot="prefix" class="el-input__icon el-icon-search"></i>
          </el-input>
        </div>
      </el-col>
      <el-col :xs="24" :sm="24" :md="18" :lg="18" :xl="20">
        <el-row v-for="phone in items" :key="phone.age" class="info-border">
          <el-col :xs="24" :sm="7" :md="5" :lg="5" :xl="5" :offset="1" class="img-tenger">
            <img alt="phone" :src="phone.imageUrl" class="pageImage">
          </el-col>
          <el-col :xs="24" :sm="16" :md="18" :lg="18" :xl="18">
            <router-link :to="'det/'+phone.id" class="title-fontSize">{{ phone.name }}</router-link>
            <p>{{ phone.snippet }}</p>
          </el-col>
        </el-row>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  data() {
    return {
      phoneData: [],
      searchPhone: "a"
    };
  },
  beforeCreate() {
    this.$axios
      .get("/static/phones/phones.json")
      .then(resp => {
        this.phoneData = resp.data;
      })
      .catch(error => {
        console.error(error);
      });
  },
  computed: {
    //过滤方法
    items: function() {
      var _search = this.searchPhone;
      if (_search) {
        //不区分大小写处理
        var reg = new RegExp(_search, "ig");
        //es6 filter过滤匹配，有则返回当前，无则返回所有
        return this.phoneData.filter(function(e) {
          //匹配所有字段
          return Object.keys(e).some(function(key) {
            return e.name.match(reg);
          });
        });
      }
      return this.phoneData;
    }
  }
};
</script>

<style scoped>
.input-bottom{
  margin-bottom: 10px;
}
.title-fontSize{
  font-size: 18px;
  line-height: 1.7;
}
.info-border{
  margin: 0 40px 20px;
  padding: 10px;
  border-radius: 5px;
  border: 1px solid #ccc;
}
img {
  vertical-align: top;
}
.img-tenger{
  text-align: center;
}
.pageImage {
  width: 100px;
  height: 80px;
}
.info {
  width: 85%;
  padding: 5px;
  display: inline-block;
}
.info p {
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 2;
}
#item-margin {
  margin: 10px 0;
  border-radius: 5px;
}
.input-margin {
  margin-bottom: 10px;
}
</style>