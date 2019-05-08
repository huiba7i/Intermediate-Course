<template>
  <div class="img-box">
    <Upload
      :on-format-error="handleFormatError"
      :on-exceeded-size="handleMaxSize"
      :show-upload-list="false"
      :format="['jpg','jpeg','png']"
      :max-size="2048"
      :before-upload="BeforeUploadImg"
      type="drag"
      action
      style="display: inline-block;width:100px;"
    >
      <div style="width: 100px;height:100px;line-height: 100px;">
        <Icon type="plus-round"></Icon>
      </div>
    </Upload>

    <div class="img-box" v-for="(s, index) in uploadList" :key="index" v-if="uploadList!=''">
      <img :src="s">
    </div>
  </div>
</template>


<script>
export default {
  data() {
    return {
      imgs: [],
      isUploadImg: false,
      uploadList: []
    };
  },
  watch: {
    isUploadImg: function(val) {
      console.log(this.imgs);
      if (val) {
        let reader = new FileReader();
        reader.readAsDataURL(this.imgs[0]);
        reader.onerror = function(e) {
          // console.log("读取文件出错！");
        };
        reader.onload = function(e) {
          // console.log("读文件结束");
        };
        reader.onloadend = e => {
          // console.log("读文件成功");
          // console.log(reader);

          this.uploadList.push(reader.result);

          console.log(this.uploadList);
          this.$http
            .post(
              "/cgi-bin/uploadImg.py",
              {
                imgData: reader.result,
                name: this.imgs[0].name,
                time: this.dateFormat(new Date())
              },
              {
                emulateJSON: true
              }
            )
            .then(resp => {
              console.log(resp);
              if (resp.data == "success") {
                this.$Message.success("上传成功");
              } else {
                this.$Message.error("上传失败");
              }
            })
            .catch(error => {
              console.log(error);
            });
          this.isUploadImg = false;
        };
      }
    }
  },
  methods: {
    BeforeUploadImg(file) {
      this.imgs.push(file);
      this.isUploadImg = true;
      return false;
    },
    handleFormatError(file) {
      this.$Notice.warning({
        title: "文件格式不正确",
        desc:
          "文件 " + file.name + " 格式不正确，请上传 jpg 或 png 格式的图片。"
      });
    },
    handleMaxSize(file) {
      this.$Notice.warning({
        title: "超出文件大小限制",
        desc: "文件 " + file.name + " 太大，不能超过 2M。"
      });
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
  }
};
</script>

<style scoped>
.img-box {
  padding: 40px 20px;
}
</style>
