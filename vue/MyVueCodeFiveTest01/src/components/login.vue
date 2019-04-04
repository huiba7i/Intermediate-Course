<template>
  <div>
    <div class="row row-margin">
      <div class="col-md-6 col-md-offset-3">
        <form role="form" @submit.prevent>
          <div class="form-group">
            <label for="name">姓名</label>
            <input type="text" id="name" class="form-control" placeholder="请输入姓名" v-model="user.name">
          </div>
          <div class="form-group">
            <label for="pwd">密码</label>
            <input type="password" id="pwd" class="form-control" placeholder="请输入密码" v-model="user.pwd">
          </div>
          <input type="button" class="btn btn-success btn-black" value="登录" @click="login">
          <router-link to="/reg" class="btn btn-success btn-black">注册</router-link>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data(){
    return{
      user: { "name": '', "pwd": '' }
    }
  },
  methods: { 
    login(){
      this.$store.dispatch({
        type: 'getData',
        userName: this.user.name,
        userPwd: this.user.pwd
      })
    }
  }
}
</script>

<style scoped>
.row-margin {
  margin: 0;
}
</style>