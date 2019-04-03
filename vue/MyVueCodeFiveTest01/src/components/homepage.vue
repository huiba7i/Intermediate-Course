<template>
  <div class="row row-margin">
    <div class="col-xs-12 col-sm-12 col-md-2 col-md-offset-1">
      <div class="input-group input-margin">
        <label for="txt">Search:</label>
        <input type="text" id="txt" class="form-control" v-model="searchPhone">
      </div>
      <span>Sort by:</span>
      <select class="selectpicker" v-model="sort">
        <option value="name">ABC</option>
        <option value="age">Newest</option>
      </select>
    </div>

    <ul class="col-xs-12 col-sm-12 col-md-9 list-group">
      <li class="list-group-item" id="item-margin" v-for="phone in items" :key="phone.age">
        <img alt="phone" :src="phone.imageUrl" class="pageImage">
        <div class="info">
          <router-link :to="'det/'+phone.id">{{ phone.name }}</router-link>
          <p>{{ phone.snippet }}</p>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      phoneData: [],
      searchPhone: "a",
      sort: 'a'
    }
  },
  beforeCreate() {
    this.$axios
      .get("/static/phones/phones.json")
      .then(resp => {
        this.phoneData = resp.data;
      })
      .catch(error => {
        console.error(error);
      })
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
.row-margin {
  margin: 0;
}
img {
  vertical-align: top;
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