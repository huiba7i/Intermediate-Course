<template>
  <div>
    <div v-for="(cid, i) in cidDetails">
      <h1 class="cid-title margin-box">{{cid.title}}</h1>
      <div v-for="(cidSrc, i) in cid.albums" :key="i" class="cid-picture-box margin-box">
        <img :src="cidSrc" :alt="cid.title" class="cid-picture">
      </div>
      <div class="cid-imtro">
        <p>{{ cid.imtro }}</p>
      </div>
      <div class="cid-material">
        <p>用料</p>
        <ul class="cid-main-material margin-box">
          <span>主料</span>
          <li>{{ cid.ingredients }}</li>
        </ul>
        <ul class="cid-accessories margin-box">
          <span>辅料</span>
          <li>{{ cid.burden }}</li>
        </ul>
      </div>
      <div class="cid-steps margin-box">
        <ol type="1">
          <li v-for="(steps, i) in cid.steps" :key="i">
            <p>{{ steps.step }}</p>
            <img :src="steps.img" :alt="steps.step">
          </li>
        </ol>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      cidDetails: [],
      mainMaterial: []
    };
  },
  methods: {
    getCidDetails() {
      this.$axios
        .get(
          `/cook/queryid?id=${
            this.$route.params.cid
          }&key=${"7515e14ef149b000386b01f808e5d9f6"}`
        )
        .then(resp => {
          // console.log(resp.data);
          this.cidDetails = resp.data.result;
          this.cidDetails = this.cidDetails.data;

          // console.log(this.cidDetails);
        })
        .catch(error => {
          console.error(error);
        });
    }
  },
  mounted() {
    this.getCidDetails();
  },
  watch: {
    $route: function(before, after) {
      if (before != after) this.getCidDetails();
    }
  }
};
</script>

<style scoped>
.margin-box {
  margin-top: 20px;
}
.cid-picture-box {
  width: 100%;
  height: 350px;
  text-align: center;
}
.cid-picture {
  width: 35%;
  height: 100%;
}
.cid-imtro {
  position: relative;
}
.cid-imtro p {
  text-indent: 20px;
  font-size: 18px;
  line-height: 35px;
  padding: 10px 20px;
  text-align: left;
}
.cid-imtro p::before,
.cid-imtro p::after {
  content: "“";
  font-family: "黑体";
  font-size: 30px;
  color: #ccc;
}
.cid-imtro p::after {
  content: "”";
}
.cid-material {
  padding: 0 55px 20px;
  text-align: left;
  overflow: hidden;
}
.cid-material p:first-child {
  font-family: "黑体";
  font-size: 30px;
  color: black;
  font-weight: 600;
}
.cid-main-material,
.cid-accessories {
  border-bottom: 1px solid #ccc;
}
.cid-main-material li,
.cid-accessories li {
  display: inline-block;
  list-style: none;
  padding: 10px;
  font-size: 16px;
  letter-spacing: 1px;
}
.cid-main-material span:first-child,
.cid-accessories span:first-child {
  display: inline-block;
  padding: 5px 15px;
  text-align: center;
  background-color: #ff3232;
  color: white;
  border: transparent;
}
.cid-accessories span:first-child {
  background-color: #f5f5f5;
  color: #999999;
}
.cid-steps{
  width: 100%;
  padding: 0 55px 20px;
}
.cid-steps ol{
  width: 100%;
  text-align: left;
}
.cid-steps li{
  text-align: center;
  display: inline-block;
  list-style-type: none;
  width: 50%;
  padding: 20px;
}
.cid-steps li p{
  font-size: 15px;
  line-height: 25px;
}
.cid-steps li img{
  width: 50%;
  height: 240px;
}
</style>
