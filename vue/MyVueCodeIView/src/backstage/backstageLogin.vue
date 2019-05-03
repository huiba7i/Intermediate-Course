<template>
  <div class="back-box">
    <Form class="form" :ref="userData" :model="userData" :rules="ruleInline">
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
    return {
      userData: {
        name: "",
        pwd: ""
      },
      ruleInline: {
        name: [{ required: true, message: "用户名不能为空", trigger: "blur" }],
        pwd: [{ required: true, message: "用户密码不能为空", trigger: "blur" }]
      }
    };
  },
  methods: {
    handleSubmit(n) {
      this.$refs[n].validate(valid => {
        if (valid) {
          this.$http
            .post(
              "http://127.0.0.1:1111/cgi-bin/backstage_login.py",
              {
                name: n.name,
                pwd: n.pwd
              },
              { emulateJSON: true }
            )
            .then(resp => {
              console.log(resp);
              if (resp.data.ok == "success") {
                this.$store.dispatch({
                  type: "authenticateUser",
                  backName: resp.data.name
                });
                this.$Message.success("登录成功");
                this.$router.push("/backHome");
              }
            })
            .catch(error => {
              console.log(error);
            });
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
.back-box {
  background-image: url("/static/imgs/back/background.jpg");
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