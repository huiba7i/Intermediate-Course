<template>
  <div class="con-box">
    <Form :model="formItem" :label-width="100" :style="{'width':'70%','margin':'40px'}">
      <FormItem label="主标题">
        <Input v-model="formItem.mainTitle" placeholder="请输入主标题"></Input>
      </FormItem>
      <FormItem label="父标题">
        <Input v-model="formItem.subTitle" placeholder="请输入父标题"></Input>
      </FormItem>
      <FormItem label="内容">
        <div id="we" :style="{'width':'100%','height':'100%'}"></div>
      </FormItem>
      <Form-item>
        <i-button type="primary" @click="add">提交</i-button>
        <i-button type="text" style="margin-left: 8px">取消</i-button>
      </Form-item>
    </Form>
  </div>
</template>

<script>
import wangEditor from "wangeditor";

export default {
  data() {
    return {
      con: "",
      editor: null,
      formItem: {
        mainTitle: "",
        subTitle: "",
        content: "",
        releaseTime: "",
        momodificationTime: ""
      }
    };
  },
  methods: {
    add() {
      let conJson = this.editor.txt.getJSON();
      let conJsonStr = JSON.stringify(conJson);

      this.$http
        .post(
          "/cgi-bin/thematicdaily_insert.py",
          {
            mainTitle: this.formItem.mainTitle,
            subTitle: this.formItem.subTitle,
            content: conJsonStr,
            releaseTime: this.dateFormat(new Date()),
            momodificationTime: this.formItem.momodificationTime
          },
          {
            emulateJSON: true
          }
        )
        .then(resp => {
          console.log(resp);
          if (resp.data == "success") {
            this.$Message.success("提交成功");
            this.formItem = {};
            this.editor.txt.html("");
          } else {
            this.$Message.error("提交失败");
          }
        })
        .catch(error => {
          console.log(error);
        });
    },
    getContent() {
      let conHtml = this.editor.txt.html();
      let conJson = this.editor.txt.getJSON();
      let conJsonStr = JSON.stringify(conJson);

      console.log("HTML====>", conHtml, typeof conHtml);
      console.log("JSON====>", conJson, typeof conJson);
      console.log("JSONSTR====>", conJsonStr, typeof conJsonStr);
    },
    dateFormat: function(time) {
      var date = new Date(time);
      var year = date.getFullYear();
      /* 在日期格式中，月份是从0开始的，因此要加0
       * 使用三元表达式在小于10的前面加0，以达到格式统一  如 09:11:05
       * */
      var month =
        date.getMonth() + 1 < 10
          ? "0" + (date.getMonth() + 1)
          : date.getMonth() + 1;
      var day = date.getDate() < 10 ? "0" + date.getDate() : date.getDate();
      var hours =
        date.getHours() < 10 ? "0" + date.getHours() : date.getHours();
      var minutes =
        date.getMinutes() < 10 ? "0" + date.getMinutes() : date.getMinutes();
      var seconds =
        date.getSeconds() < 10 ? "0" + date.getSeconds() : date.getSeconds();
      // 拼接
      return (
        year +
        "-" +
        month +
        "-" +
        day +
        " " +
        hours +
        ":" +
        minutes +
        ":" +
        seconds
      );
    }
  },
  mounted() {
    this.editor = new wangEditor(document.getElementById("we"));
    this.editor.create();
  }
};
</script>

<style scoped>
.con-box {
  margin-top: 40px;
  padding: 40px 20px;
  background-color: white;
}
</style>
