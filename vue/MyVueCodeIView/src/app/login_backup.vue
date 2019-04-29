<template>
  <div class="login-box">
    <Form class="form" ref="userData" :model="userData" :rules="ruleInline">
      <FormItem prop="user">
        <Input type="text" v-model="userData.user" placeholder="Username">
          <Icon type="ios-person-outline" slot="prepend"></Icon>
        </Input>
      </FormItem>
      <FormItem prop="password">
        <Input type="password" v-model="userData.password" placeholder="Password">
          <Icon type="ios-lock-outline" slot="prepend"></Icon>
        </Input>
      </FormItem>
      <FormItem>
        <Button type="primary" @click="handleSubmit('userData')">登录</Button>
        <Button type="default" ghost @click="cancel" :style="{marginLeft: '20px'}">注册</Button>
      </FormItem>
      <div class="bottom-home">
        <Button type="text" ghost @click="home">返回首页</Button>
      </div>
    </Form>
  </div>
</template>

<script>
export default {
  data() {
    const verUser = (rule, value, callback) => {
      if (value == "") {
        callback("用户名不能为空");
      } else if (value == "admin") {
        callback();
        this.$store.dispatch({
          type: "authenticateUser",
          userName: value
        });
      } else {
        callback("账户名错误");
      }
    };
    const verPwd = (rule, value, callback) => {
      if (value == "") {
        callback("密码不能为空");
      } else if (value == "123") {
        callback();
      } else {
        callback("密码错误");
      }
    };
    return {
      userData: {
        user: "",
        password: ""
      },
      ruleInline: {
        user: [
          {
            validator: verUser,
            trigger: "blur"
          }
        ],
        password: [
          {
            validator: verPwd,
            trigger: "blur"
          }
        ]
      }
    };
  },
  methods: {
    handleSubmit(name) {
      this.$refs[name].validate(valid => {
        if (valid) {
          console.log(valid);
          this.$Message.success("登录成功");
          this.$router.push("/");
        } else {
          this.$Message.error("登录失败");
        }
      });
    },
    cancel() {
      this.$router.push("/reg");
    },
    home() {
      this.$router.push("/");
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
