<template>
  <div>
    <el-row>
      <el-col :offset="6" :xs="24" :sm="24" :md="12" :lg="12" :xl="12">
        <el-form :label-position="labelPosition" label-width="130px" @submit.native.prevent>
          <el-form-item label="姓名">
            <el-input></el-input>
          </el-form-item>
          <el-form-item label="密码">
            <el-input></el-input>
          </el-form-item>
          <el-form-item label="确认密码">
            <el-input></el-input>
          </el-form-item>
          <el-form-item label="性别">
            <el-radio-group>
              <el-radio label="男">男</el-radio>
              <el-radio label="woman">女</el-radio>
            </el-radio-group>
          </el-form-item>
          <el-form-item label="出生日期">
            <el-date-picker value-format="yyyy-mm-dd" type="date" placeholder="选择日期"></el-date-picker>
          </el-form-item>
          <el-form-item label="请输入家庭住址">
            <el-input type="textarea" :rows="2" placeholder="请输入家庭住址"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary">注册</el-button>
            <el-button type="danger">重置</el-button>
          </el-form-item>
        </el-form>
      </el-col>
    </el-row>
  </div>

  <!-- <div>
    <div class="row row-margin">
      <div class="col-md-6 col-md-offset-3">
        <form action role="form">
          <div class="form-group">
            <label for="name">姓名</label>
            <input type="text" id="name" name="name" class="form-control" placeholder="请输入姓名">
          </div>
          <div class="form-group">
            <label for="pwd">密码</label>
            <input type="password" id="pwd" name="pwd" class="form-control" placeholder="请输入密码">
          </div>
          <div class="form-group">
            <label for="upwd">确认密码</label>
            <input type="password" id="upwd" name="upwd" class="form-control" placeholder="请输入密码">
          </div>
          <div class="form-group">
            <label>性别</label>
            <div class="radio">
              <label class="radio-inline">
                <input type="radio" id="male" name="gender" checked>男
              </label>
              <label class="radio-inline">
                <input type="radio" id="girl" name="gender">女
              </label>
            </div>
          </div>
          <div class="form-group">
            <label for="date">出生日期</label>
            <input type="date" id="date" name="date" class="form-control" placeholder="请输入出生日期">
          </div>
          <div class="form-group">
            <label for="address">家庭地址</label>
            <input type="text" id="address" name="address" class="form-control" placeholder="请输入家庭地址">
          </div>
          <div class="form-group">
            <label for="currentResidence">现居住地址</label>
            <input type="text" id="currentResidence" name="currentResidence" class="form-control" placeholder="请输入现居住地址">
          </div>
          <div class="form-group">
            <input type="submit" class="btn btn-primary" id="submit" value="提交">
            <input type="reset" class="btn btn-danger" id="reset" value="重置">
          </div>
        </form>
      </div>
    </div>
  </div>-->
</template>

<script>
export default {
  data() {
    return {
      labelPosition: "right"
    };
  }
};
</script>

<style scoped>
.row-margin {
  margin: 0;
}
</style>
