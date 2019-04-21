<template>
  <el-main>
    <el-row v-show="$route.meta.singleDetails">
      <el-col class="col-card-box" :span="5" v-for="(sin,index) in singleDish.data" :key="index">
        <el-card class="card-box">
          <img :src="sin.albums[0]" :alt="sin.title" class="card-picture">
          <div style="padding: 14px;">
            <router-link class="card-title" :to="'/singleDetails/'+sin.id">{{ sin.title }}</router-link>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </el-main>
</template>

<script>
export default {
  data() {
    return {
      singleDish: []
    };
  },
  methods: {
    getSingleDetails() {
      this.$axios
        .get(
          `/cook/index?cid=${
            this.$route.params.id
          }&key=${"7515e14ef149b000386b01f808e5d9f6"}`
        )
        .then(resp => {
          this.singleDish = resp.data.result;
        })
        .catch(error => {
          console.error(error);
        });
    }
  },
  mounted() {
    this.getSingleDetails();
  },
  watch: {
    $route: function(before, after) {
      if (before != after) this.getSingleDetails();
    }
  }
};
</script>

<style scoped>
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
</style>
