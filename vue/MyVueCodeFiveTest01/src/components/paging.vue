<template>
  <div>
    <el-table border :data="getData.dataList">
      <el-table-column prop="id" label="ID"></el-table-column>
      <el-table-column prop="name" label="Name"></el-table-column>
      <el-table-column prop="province" label="Province"></el-table-column>
      <el-table-column prop="city" label="City"></el-table-column>
      <el-table-column prop="address" label="Address"></el-table-column>
      <el-table-column prop="date" label="Date"></el-table-column>
      <el-table-column prop="zip" label="Zip"></el-table-column>
    </el-table>
    <div class="pagin-center">
      <el-pagination
        background
        layout="prev,pager,next,jumper"
        :total="getData.total"
        :page-size="getData.pageSize"
        :page-count="getData.pageCount"
        :current-page="getData.currentPage"
        @current-change="currentPageNumber"
      ></el-pagination>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      getData: []
    };
  },
  created() {
    this.$axios
      .get("/sys/user/page")
      .then(resp => {
         console.log(resp.data);
        this.getData = resp.data;
      })
      .catch(error => {
        console.log(error);
      });
  },
  methods: {
    // 当前页
    currentPageNumber(page){
      this.$axios.get("/sys/user/page?currentPage="+page).then(resp=>{
        this.getData = resp.data;
      }).catch(error=>{
        console.log(error);
      });
    }
  }
};
</script>

<style scoped>
.pagin-center{
  padding: 20px 0;
  text-align: center;
}
</style>

