<template>
  <div class="update-box">
    <h1 :style="{ 'text-align': 'left', 'padding': '20px' }">修改用户</h1>
    <Card class="update-card">
      <Form :model="user" :ref="user" :label-width="100" :style="{ 'margin': '20px 30%' }">
        <FormItem label="用户名">
          <Input v-model="user.name" placeholder="请输入用户名"></Input>
        </FormItem>
        <FormItem label="省份/城市">
          <Cascader
            :clearable="clearable"
            @on-change="handleChange"
            :value.sync="ascaderValue"
            :data="ascaderData"
            trigger="hover"
            aria-placeholder="请选择省市"
          ></Cascader>
        </FormItem>
        <FormItem label="住址">
          <Input v-model="user.address" placeholder="请输入住址"></Input>
        </FormItem>
        <FormItem label="邮编">
          <Input v-model="user.zip" placeholder="请输入邮编"></Input>
        </FormItem>
        <FormItem label="出生日期" :style="{'text-align': 'left'}">
          <Date-picker
            :clearable="clearable"
            type="date"
            v-model="user.date"
            placeholder="请选择出生日期"
            style="width: 260px"
          ></Date-picker>
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
import cascader from "./Cascader.vue";
export default {
  data() {
    return {
      clearable: false, // 是否清楚省市连级选项框
      selectedValue: [], // 省市连级改变值
      ascaderValue: [], // 省市连级初始值
      ascaderData: cascader, // 省市连级数据
      userInfo: {}, // 用户信息
      user: {
        name: "",
        address: "",
        zip: "",
        date: "",
        province: "",
        city: ""
      },
      rules: {
        name: [
          { required: true, message: "用户名不能为空", trigger: "blur" },
          {
            pattern: /[\u4E00-\u9FA50-9a-zA-Z_]{3,6}/,
            message: "必须 3-10个中文字符、英文字母、数字及下划线",
            trigger: "blur"
          }
        ],
        address: [
          { required: true, message: "必须 住址不能为空", trigger: "blur" }
        ],
        zip: [
          // { required: true, message: "必须 邮编不能为空", trigger: "blur" },
          {
            pattern: /[0-9]{6}/,
            message: "必须 6位数数字",
            trigger: "blur"
          }
        ]
      },
      id: this.$route.params.id // 用户id
    };
  },
  methods: {
    handleChange(value, selectedData) {
      this.selectedValue = selectedData;
    },
    // 更新信息
    update(e) {
      if (e.name === "") {
        this.$Message.warning("必须用户名不能为空");
        return;
      } else if (!/^[\u4E00-\u9FA50-9a-zA-Z_]{3,10}$/.test(e.name)) {
        this.$Message.warning("必须 3-10个中文字符、英文字母、数字及下划线");
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
      } else if (this.dateFormat(e.date) == "NaN-NaN-NaN") {
        this.$Message.warning("请选择出生日期");
        return;
      } else {
        this.$http
          .post(
            "http://127.0.0.1:1111/cgi-bin/user_update.py",
            {
              name: e.name,
              province:
                this.selectedValue.length === 0
                  ? this.user.province
                  : this.selectedValue[0].label,
              city:
                this.selectedValue.length === 0
                  ? this.user.city
                  : this.selectedValue[1].label,
              address: e.address,
              zip: e.zip,
              date: this.dateFormat(e.date),
              id: this.id
            },
            {
              emulateJSON: true
            }
          )
          .then(resp => {
            // console.log(resp);
            if (resp.data == "success") {
              this.$Message.success("修改成功");
              this.$router.push("/dish");
            } else {
              this.$Message.error("修改失败");
            }
          })
          .catch(error => {
            this.$Message.error("修改失败");
            console.log(error);
          });
      }
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
          this.userInfo = resp.data[0];
          this.user.name = resp.data[0].name;
          this.user.province = resp.data[0].province;
          this.user.city = resp.data[0].city;
          this.user.address = resp.data[0].address;
          this.user.zip = resp.data[0].zip;
          this.user.date = resp.data[0].date;

          for (let c of this.ascaderData) {
            if (c.label == resp.data[0].province) {
              this.ascaderValue.push(c.value);
            }
            for (let children of c.children) {
              if (children.label == resp.data[0].city) {
                this.ascaderValue.push(children.value);
              }
            }
          }
        })
        .catch(error => {
          console.log(error);
        });
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
  },
  mounted() {
    this.getSingleData(this.id);
  }
};
</script>

<style scoped>
.update-box {
  padding: 40px 20px;
}
</style>