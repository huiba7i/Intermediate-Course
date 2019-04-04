<template>
  <div class="container">
    <table class="table">
      <caption class="text-center">
        <h2>用户详细信息</h2>
      </caption>
      <thead>
        <tr>
          <th>ID</th>
          <th>Name</th>
          <th>Province</th>
          <th>City</th>
          <th>Address</th>
          <th>Date</th>
          <th>Zip</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>{{ dataInfo.id }}</td>
          <td>{{ dataInfo.name }}</td>
          <td>{{ dataInfo.province }}</td>
          <td>{{ dataInfo.city }}</td>
          <td>{{ dataInfo.address }}</td>
          <td>{{ dataInfo.date }}</td>
          <td>{{ dataInfo.zip }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      dataInfo: {}
    }
  },
  methods: {
    getDataInfo() {
      this.$axios
        .get("/sys/user/select?id="+this.$route.params.id)
        .then(resp => {
          this.dataInfo = resp.data;
          console.log(this.dataInfo);
        })
        .catch(error => {
          console.error(error);
        });
    }
  },
  created() {
    this.getDataInfo();
  }
};
</script>

<style scoped>
</style>

