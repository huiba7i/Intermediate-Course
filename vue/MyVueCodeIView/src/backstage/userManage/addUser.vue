<template>
  <div class="add-box">
    <h1 :style="{ 'text-align': 'left', 'padding': '20px' }">新增用户</h1>
    <Card class="add-card">
      <Form :model="user" :ref="user" :label-width="100" :style="{ 'margin': '20px 30%' }">
        <FormItem label="用户名">
          <Input v-model="user.name" placeholder="请输入用户名"></Input>
        </FormItem>
        <FormItem label="省份/城市">
          <Cascader
            @on-change="handleChange"
            :data="ascaderData"
            trigger="hover"
            placeholder="请选择省份"
            :value.sync="ascaderValue"
          ></Cascader>
        </FormItem>
        <FormItem label="详细住址">
          <Input v-model="user.address" placeholder="请输入住址"></Input>
        </FormItem>
        <FormItem label="邮编">
          <Input v-model="user.zip" placeholder="请输入邮编"></Input>
        </FormItem>
        <FormItem label="出生日期" :style="{'text-align': 'left'}">
          <Date-picker type="date" v-model="user.date" placeholder="请选择出生日期" style="width: 260px"></Date-picker>
        </FormItem>
        <FormItem>
          <Button type="primary" @click="add(user)">提交</Button>
          <Button style="margin-left: 8px" type="text" @click="rest">重置</Button>
        </FormItem>
      </Form>
    </Card>
  </div>
</template>

<script>
import cascader from "./Cascader.vue";
export default {
  data() {
    return {
      user: {
        name: "",
        address: "",
        zip: "",
        date: ""
      },
      rules: {
        name: [
          { required: true, message: "用户名不能为空", trigger: "blur" },
          {
            pattern: /^[\u4E00-\u9FA50-9a-zA-Z_]{3,10}$/,
            message: "必须 3-10个中文字符、英文字母、数字及下划线",
            trigger: "blur"
          }
        ],
        address: [
          { required: true, message: "必须 住址不能为空", trigger: "blur" }
        ],
        zip: [
          { required: true, message: "必须 邮编不能为空", trigger: "blur" },
          {
            pattern: /^[0-9]{6}$/,
            message: "必须 6位数数字",
            trigger: "blur"
          }
        ]
      },
      ascaderData: cascader,
      ascaderValue: [],
      selectedValue: []
    };
  },
  methods: {
    rest() {
      this.user = {};
      this.ascaderValue = [];
      this.selectedValue = [];
    },
    handleChange(value, selectedData) {
      this.selectedValue = selectedData;
    },
    add(e) {
      if (e.name === "") {
        this.$Message.warning("必须用户名不能为空");
        return;
      } else if (!/^[\u4E00-\u9FA50-9a-zA-Z_]{3,10}$/.test(e.name)) {
        this.$Message.warning("必须 3-10个中文字符、英文字母、数字及下划线");
        return;
      } else if (this.selectedValue.length === 0) {
        this.$Message.warning("必须 请选择省市");
        return;
      } else if (e.address === "") {
        this.$Message.warning("必须 请填写住址");
        return;
      } else if (!/^[0-9]{6}$/.test(e.zip)) {
        this.$Message.warning("必须 请填写6位数邮编");
        return;
      } else if (e.date === "") {
        this.$Message.warning("必须 请选择出生日期");
        return;
      } else {
        this.$http
          .post(
            "http://127.0.0.1:1111/cgi-bin/user_insert.py",
            {
              name: e.name,
              province: this.selectedValue[0].label,
              city: this.selectedValue[1].label,
              address: e.address,
              zip: e.zip,
              date: this.dateFormat(e.date)
            },
            {
              emulateJSON: true
            }
          )
          .then(resp => {
            // console.log(resp);
            if (resp.data == "success") {
              this.$Message.success("添加成功");
              this.$router.push("/dish");
            }
          })
          .catch(error => {
            console.log(error);
          });
      }
    },
    dateFormat: function(time) {
      var date = new Date(time);
      var year = date.getFullYear();
      var month =
        date.getMonth() + 1 < 10
          ? "0" + (date.getMonth() + 1)
          : date.getMonth() + 1;
      var day = date.getDate() < 10 ? "0" + date.getDate() : date.getDate();
      return year + "-" + month + "-" + day;
    }
  }
};
</script>

<style scoped>
.add-box {
  padding: 40px 20px;
}
</style>
