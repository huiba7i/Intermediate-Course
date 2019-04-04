<template>
  <div>
    <ul class="nav nav-tabs">
      <li class="active">
        <router-link to="/">Home</router-link>
      </li>
      <li>
        <router-link to="/log">登录</router-link>
      </li>
      <li>
        <router-link to="/reg">注册</router-link>
      </li>
      <li>
        <router-link to="/one">One</router-link>
      </li>
      <li>
        <router-link to="/two">Two</router-link>
      </li>
      <li>
        <router-link to="/user">用户列表</router-link>
      </li>
      <li v-if="$store.state.uName!=''">
        <h4>{{ $store.state.uName欢迎登录 }}</h4>
      </li>
      <li class="pull-right">
        <a class="btn btn-black" @click="clear">注销</a>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: null
    };
  },
  methods: {
    clear() {
      let r = confirm(`确定注销${this.username}吗？`);

      if (r) {
        localStorage.clear();
        if (this.username == null) {
          this.$router.push("/");
        }
      }
    }
  },
  mounted() {
    this.username = localStorage.getItem("login_username");
    // console.log(this.username);
  }
};
</script>

<style>
</style>


