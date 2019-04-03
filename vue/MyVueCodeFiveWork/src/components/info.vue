<template>
  <div>
    <ul v-for="info in dataInfo" :key="info.id">
      <li>
        <span>ID</span>
        {{ info.id }}
      </li>
      <li>
        <span>姓名</span>
        {{ info.name }}
      </li>
      <li>
        <span>省</span>
        {{ info.province }}
      </li>
      <li>
        <span>市</span>
        {{ info.city }}
      </li>
      <li>
        <span>地址</span>
        {{ info.address }}
      </li>
      <li>
        <span>邮编</span>
        {{ info.zip }}
      </li>
      <li>
        <span>日期</span>
        {{ info.date }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      dataInfo: {}
    };
  },
  methods: {
    getDataInfo() {
      this.$axios
        .get(`/sys/user/select/${this.$route.params.id}`)
        .then(resp => {
          this.dataInfo = resp.data;
        })
        .catch(error => {
          console.error(error);
        });
    }
  }
};
</script>

<style scoped>
ul li{
    list-style: none;
}
</style>

