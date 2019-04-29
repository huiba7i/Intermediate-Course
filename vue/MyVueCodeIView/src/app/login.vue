<template>
  <div class="login-box">
    <Form class="form" ref="userData" :model="userData">
      <FormItem prop="user">
        <Input type="text" v-model="userData.name" placeholder="Username">
          <Icon type="ios-person-outline" slot="prepend"></Icon>
        </Input>
      </FormItem>
      <FormItem prop="password">
        <Input type="password" v-model="userData.pwd" placeholder="Password">
          <Icon type="ios-lock-outline" slot="prepend"></Icon>
        </Input>
      </FormItem>
      <FormItem>
        <Button type="primary" @click="handleSubmit(userData)">登录</Button>
        <Button type="default" ghost @click="cancel" :style="{marginLeft: '20px'}">注册</Button>
      </FormItem>
      <div class="bottom-home">
        <Button type="text" ghost @click="home">返回首页</Button>
      </div>
    </Form>
  </div>
</template>

<script>
import qs from "querystring";

export default {
  data() {
    return {
      userData: {
        name: "",
        pwd: ""
      }
    };
  },
  methods: {
    cancel() {
      this.$router.push("/reg");
    },
    home() {
      this.$router.push("/");
    },
    handleSubmit(n) {
      let reg = /^\s*$/;
      if (reg.test(n.anme) || reg.test(n.pwd)) {
        this.$Message.success("请填写完整信息");
        return;
      }
      console.log(n.name, n.pwd);
      this.$.post("http://localhost:1111/cgi-bin/login.py", { name: n.name, pwd: n.pwd }, function(data) {
        if (data == "success") {
          console.log(data);
        } else {
          $("#info").text("用户名不存在或者密码错误");
        }
      });
    }
  }
};
</script>

<style scoped>
.login-box {
  background-image: url("/static/imgs/home/login.jpg");
  background-size: 100% 100%;
  position: fixed;
  height: 100%;
  width: 100%;
}
.form {
  width: 20%;
  background-color: rgba(240, 240, 240, 0.4);
  margin: 200px auto;
  padding: 20px 20px 0;
  border-radius: 5px;
  position: relative;
}
.bottom-home {
  text-align: right;
}
</style>
