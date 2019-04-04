<template>
  <div class="container">
    <table class="table">
      <caption class="text-center"><h3>用户列表</h3></caption>
      <thead>
        <tr>
          <th>ID</th>
          <th>姓名</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="d in data" :key="d.id">
          <td><router-link :to="'userInfo/'+d.id">{{ d.id }}</router-link></td>
          <td>{{ d.name }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      data: {}
    };
  },
  methods: {
    getData() {
      this.$axios
        .get("/sys/user/all")
        .then(resp => {
          this.data = resp.data;
          // console.log(this.data);
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

