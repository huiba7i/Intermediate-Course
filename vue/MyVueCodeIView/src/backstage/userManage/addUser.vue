<template>
  <div class="add-box">
    <h1 :style="{ 'text-align': 'left', 'padding': '20px' }">新增用户</h1>
    <Card class="add-card">
      <Form  :model="user" :label-width="100" :style="{ 'margin': '20px 30%' }">
        <FormItem label="用户名">
          <Input v-model="user.name" placeholder="请输入用户名"></Input>
        </FormItem>
        <FormItem label="用户密码">
          <Input v-model="user.passworld" placeholder="请输入用户密码"></Input>
        </FormItem>
        <FormItem label="管理权限">
            <Select v-model="user.jurisdiction">
                <Option value="SuperAdministrator">超级管理员</Option>
                <Option value="OrdinaryAdministrator">普通管理员</Option>
                <Option value="GeneralOperator">普通操作员</Option>
            </Select>
        </FormItem>
        <FormItem>
            <Button type="primary">Submit</Button>
            <Button style="margin-left: 8px">Cancel</Button>
        </FormItem>
      </Form>
    </Card>
  </div>
</template>

<script>
export default {
  data(){
    return{
      user: {
        name: '',
        passworld: '',
        jurisdiction: []
      }
    }
  }
};
</script>

<style scoped>
.add-box {
  padding: 40px 20px;
}
</style>
