<template>
  <el-row>
    <el-col :offset="6" :xs="18" :sm="12" :md="12" :lg="12" :xl="12">
      <el-form
        :label-position="labelPosition"
        label-width="80px"
        :model="user"
        @submit.native.prevent
      >
        <el-form-item label="姓名">
          <el-input v-model="user.name" placeholder="请输入姓名"></el-input>
        </el-form-item>
        <el-form-item label="密码">
          <el-input type="password" v-model="user.pwd" placeholder="请输入密码"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="login">登录</el-button>
          <router-link to="/reg" class="el-button">注册</router-link>
        </el-form-item>
      </el-form>
    </el-col>
  </el-row>
</template>
 
<script>
export default {
  data() {
    return {
      labelPosition: "right",
      user: { name: "", pwd: "" }
    };
  },
  methods: {
    login() {
      if (this.user.name == "" || this.user.pwd == "") {
        this.$message.error("请输入姓名和密码");
      } else {
        this.$store
          .dispatch({
            type: "getData",
            userName: this.user.name,
            userPwd: this.user.pwd
          })
          .then(resp => {
            this.$router.push("/");
          });
      }
    }
  }
};
</script>

<style scoped>
.row-margin {
  margin: 0;
}
.input-center {
  margin: 20px auto;
}
</style>