<template>
  <div class="update-box">
    <h1 :style="{ 'text-align': 'left', 'padding': '20px' }">修改用户</h1>
    <Card class="update-card">
      <Form
        :model="user"
        :ref="user"
        :rules="rules"
        :label-width="100"
        :style="{ 'margin': '20px 30%' }"
      >
        <FormItem label="用户名" prop="name">
          <Input v-model="user.name" placeholder="请输入用户名"></Input>
        </FormItem>
        <FormItem label="省份" prop="province">
          <Input v-model="user.province" placeholder="请输入省市"></Input>
        </FormItem>
        <FormItem label="城市" prop="city">
          <Input v-model="user.city" placeholder="请输入城市"></Input>
        </FormItem>
        <FormItem label="住址" prop="address">
          <Input v-model="user.address" placeholder="请输入住址"></Input>
        </FormItem>
        <FormItem label="邮编" prop="zip">
          <Input v-model="user.zip" placeholder="请输入邮编"></Input>
        </FormItem>
        <FormItem label="出生日期" prop="date">
          <Input type="date" v-model="user.date" placeholder="请输入出生日期"></Input>
        </FormItem>
        <FormItem>
          <Button type="primary" @click="update(user)">修改</Button>
          <Button style="margin-left: 8px" type="text" @click="()=>{$router.push('/dish')}">取消</Button>
        </FormItem>
      </Form>
    </Card>
  </div>
</template>


<script>
export default {
  data() {
    return {
      user: {
        name: "",
        province: "",
        city: "",
        address: "",
        zip: "",
        date: ""
      },
      rules: {
        name: [
          { required: true, message: "用户名不能为空", trigger: "blur" },
          {
            pattern: /^[\u4E00-\u9FA50-9a-zA-Z_]{3,6}$/,
            message: "必须 3-10个中文字符、英文字母、数字及下划线",
            trigger: "blur"
          }
        ],
        province: [
          { required: true, message: "必须 省份不能为空", trigger: "blur" }
        ],
        city: [
          { required: true, message: "必须 城市不能为空", trigger: "blur" }
        ],
        address: [
          { required: true, message: "必须 住址不能为空", trigger: "blur" }
        ],
        zip: [
          { required: true, message: "必须 邮编不能为空", trigger: "blur" },
          {
            pattern: /[0-9]{6}/,
            message: "必须 6位数数字",
            trigger: "blur"
          }
        ],
        date: [
          { required: true, message: "必填 出生日期不能为空", trigger: "blur" },
          {
            pattern: /(\d{4}-\d{2}-\d{2})/,
            message: "必须 格式yyyy-mm-dd",
            trigger: "blur"
          }
        ]
      },
      id: this.$route.params.id
    };
  },
  methods: {
    // 更新信息
    update(e) {
      this.$refs[e].validate(valid => {
        if (valid) {
          this.$http
            .post(
              "http://127.0.0.1:1111/cgi-bin/user_update.py",
              {
                name: e.name,
                province: e.province,
                city: e.city,
                address: e.address,
                zip: e.zip,
                date: e.date,
                id: this.id
              },
              {
                emulateJSON: true
              }
            )
            .then(resp => {
              console.log(resp);
              if (resp.data == "success") {
                this.$Message.success("修改成功");
                this.$router.push("/dish");
              }
            })
            .catch(error => {
              console.log(error);
            });
        } else {
          this.$Message.error("修改失败");
        }
      });
    },
    //根据id，获取个人用户信息
    getSingleData(id) {
      this.$http
        .post(
          "http://127.0.0.1:1111/cgi-bin/user_conditional_data.py",
          { id: id },
          { emulateJSON: true }
        )
        .then(resp => {
          // console.log(resp);
          this.user.name = resp.data[0].name
          this.user.province = resp.data[0].province
          this.user.city = resp.data[0].city
          this.user.address = resp.data[0].address
          this.user.zip = resp.data[0].zip
          this.user.date = resp.data[0].date
        })
        .catch(error => {
          console.log(error);
        });
    }
  },
  mounted() {
    this.getSingleData(this.id);
  },
 
};
</script>

<style scoped>
.update-box {
  padding: 40px 20px;
}
</style>