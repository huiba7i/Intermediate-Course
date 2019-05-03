<template>
  <div class="reg-box">
    <Form class="form" :ref="user" :model="user" :label-width="70" :rules="rules">
      <FormItem label="账号" prop="account">
        <Input v-model="user.account" placeholder="昵称/手机号/邮箱"/>
      </FormItem>
      <FormItem label="密码" prop="password">
        <Input type="password" v-model="user.password" placeholder="密码"/>
      </FormItem>
      <FormItem label="确认密码" prop="confirmPass">
        <Input type="password" v-model="user.confirmPass" placeholder="密码"/>
      </FormItem>
      <FormItem label="手机号" prop="phone">
        <Input v-model="user.phone" placeholder="手机号码"/>
      </FormItem>
      <FormItem label="性别" prop="sex" class="left">
        <RadioGroup v-model="user.sex">
          <Radio label="男"></Radio>
          <Radio label="女"></Radio>
        </RadioGroup>
      </FormItem>
      <FormItem label="爱好" prop="favor">
        <CheckboxGroup v-model="user.favor" class="left">
          <Checkbox label="休闲"></Checkbox>
          <Checkbox label="娱乐"></Checkbox>
          <Checkbox label="美食"></Checkbox>
          <Checkbox label="购物"></Checkbox>
        </CheckboxGroup>
      </FormItem>
      <FormItem style="text-align:center">
        <Button type="primary" @click="registe('user')">注册</Button>
        <Button type="info" style="margin-left:20px" @click="rest">重置</Button>
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
    const accountDup = (rule, value, callback) => {
      if (value == "") {
        callback("账号不能为空");
      } else if (value.length < 3) {
        callback("长度至少为3");
      }
      this.$axios
        .get("/sys/user/select?id=" + value)
        .then(resp => {
          if (resp.data) {
            callback("账号已经被注册了");
          } else {
            callback();
          }
        })
        .catch(error => {
          callback(error);
        });
    };
    const cpwd = (rule, value, callback) => {
      if (value == "") {
        callback("内容不能为空");
      } else if (value != this.user.password) {
        console.log(value);
        console.log(this.user.password);
        callback("密码不一致");
      } else {
        callback();
      }
    };
    return {
      user: {
        account: "",
        password: "",
        confirmPass: "",
        sex: "",
        favor: [],
        phone: ""
      },
      rules: {
        account: { validator: accountDup, trigger: "blur" },
        password: [
          { required: true, message: "密码不能为空", trigger: "blur" },
          { pattern: /^\w{6,}$/, message: "密码不合法", trigger: "blur" }
        ],
        confirmPass: { validator: cpwd, trigger: "blur" },
        phone: [
          { required: true, message: "手机号码不能为空", trigger: "blur" },
          {
            pattern: /^1[3578]\d{9}$/,
            message: "手机号码不合法",
            trigger: "blur"
          }
        ],
        sex: { required: true, message: "性别是必选项", trigger: "change" },
        favor: {
          required: true,
          type: "array",
          min: 1,
          message: "爱好至少有一个",
          trigger: "change"
        }
      }
    };
  },
  methods: {
    registe(name) {
      this.$refs[name].validate(valid => {
        if (valid) {
          this.$Message.success("注册成功");
          this.user = {};
        } else {
          this.$Message.error("注册失败");
        }
      });
    },
    rest() {
      this.user = {};
    },
    home() {
      this.$router.push("/");
    }
  }
};
</script>

<style scoped>
.reg-box {
  background-color: red;
  background-image: url("/static/imgs/home/login.jpg");
  background-size: 100% 100%;
  position: fixed;
  height: 100%;
  width: 100%;
}
.form {
  width: 40%;
  background-color: rgba(240, 240, 240, 0.4);
  margin: 100px auto;
  padding: 20px 20px 0;
  border-radius: 5px;
}
.left {
  text-align: left;
}
.bottom-home {
  text-align: right;
}
</style>
