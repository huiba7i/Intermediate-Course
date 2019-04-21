<template>
  <div>
    <h1>{{ $route.params.cid }}</h1>
    <span v-for="(sig, i) in cidDetails" :key="i">{{ sig }}</span>
  </div>
</template>

<script>
export default {
  data() {
    return {
      cidDetails: []
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
          console.log(resp.data);
          this.cidDetails = resp.data.result;
          console.log(this.cidDetails);
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
</style>
