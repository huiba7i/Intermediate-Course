<template>
  <div>
    <div :style="styDiv">
      <router-link :style="styA" :to="'info'+d.id">{{ d.id }}</router-link>
      <span :style="stySpan">{{ d.name }}</span>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      data: {},
      styDiv: {
        width: "50%",
        margin: "20px auto"
      },
      styA: {
        float: "right"
      },
      strSpan: {
        float: "right"
      }
    };
  },
  methods: {
    getData() {
      this.$axios
        .get("/sys/user/all")
        .then(resp => {
          this.data = resp.data;
        })
        .catch(error => {
          console.log(error);
        });
    }
  },
  created() {
    this.getData();
  }
};
</script>

<style scoped>
</style>


