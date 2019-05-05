<template>
  <div class="login-box">
    <Form class="form" :ref="userData" :model="userData" :rules="rules">
      <FormItem prop="name">
        <Input type="text" v-model="userData.name" placeholder="Username">
          <Icon type="ios-person-outline" slot="prepend"></Icon>
        </Input>
      </FormItem>
      <FormItem prop="pwd">
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
      },
      rules: {
        name: [{ required: true, message: "用户名不能为空", trigger: "blur" }],
        pwd: [{ required: true, message: "用户密码不能为空", trigger: "blur" }]
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
      this.$refs[n].validate(valid => {
        if (valid) {
          this.$http
            .post(
              "http://127.0.0.1:1111/cgi-bin/login.py",
              {
                name: n.name,
                pwd: n.pwd
              },
              { emulateJSON: true }
            )
            .then(resp => {
              console.log(resp)
              if (resp.data.isOk == "success") {
                this.$store.dispatch({
                  type: "authenticateUser",
                  userName: resp.data.name
                });
                this.$Message.success("登录成功");
                this.$router.push("/");
              } else {
                this.$Message.error('登录名或密码错误');
              }
            })
            .catch(error => {
              console.log(error);
            });
        } else {
          this.$Message.success("登录失败");
          this.$router.push("/login");
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
