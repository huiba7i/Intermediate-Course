<template>
  <div>
    <div class="row row-margin">
      <div class="col-md-6 col-md-offset-3">
        <form action role="form">
          <div class="form-group">
            <label for="name">姓名</label>
            <input type="text" id="name" class="form-control" placeholder="请输入姓名">
          </div>
          <div class="form-group">
            <label for="pwd">密码</label>
            <input type="text" id="pwd" class="form-control" placeholder="请输入密码">
          </div>
          <input type="button" class="btn btn-success btn-black" value="登录">
          <a href="#!/user/reg" class="btn btn-link btn-black">注册</a>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
.row-margin {
  margin: 0;
}
</style>