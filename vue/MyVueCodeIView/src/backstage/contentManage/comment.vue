<template>
  <div class="comment-box">
    <h1 :style="{ 'text-align': 'left', 'padding': '20px' }">评论管理</h1>
    <Card class="comment-card">
      <Row class="menu">
        <Col :span="6">
          <ButtonGroup>
            <Button type="success" icon="md-add">新增</Button>
            <Button type="info" icon="md-copy">保存</Button>
            <Button type="warning" icon="ios-albums-outline">审核</Button>
            <Button type="error" icon="ios-trash-outline">删除</Button>
          </ButtonGroup>
        </Col>
        <Col :span="6" :offset="3">
          <Dropdown :style="{ float: 'right' }">
            <Button>
              下拉菜单
              <Icon type="ios-arrow-down"></Icon>
            </Button>
            <DropdownMenu slot="list">
              <DropdownItem>春季</DropdownItem>
              <DropdownItem>夏季</DropdownItem>
              <DropdownItem>秋季</DropdownItem>
              <DropdownItem>冬季</DropdownItem>
            </DropdownMenu>
          </Dropdown>
        </Col>
        <Col :span="6" :offset="3">
          <Input suffix="ios-search" placeholder="Enter text"/>
        </Col>
      </Row>
      <Table :columns="columns2" :data="commentData" :style="{margin: '20px'}"></Table>
    </Card>
  </div>
</template>

<script>
export default {
  data() {
    return {
      columns2: [
        {
          type: "selection",
          width: 60,
          align: "center"
        },
        {
          title: "评论",
          key: "name"
        }
      ],
      commentData: [
        { id: 1, name: "菜品1", date: "2019-04-11" },
        { id: 2, name: "菜品2", date: "2019-04-12" },
        { id: 3, name: "菜品3", date: "2019-04-13" },
        { id: 4, name: "菜品4", date: "2019-04-14" },
        { id: 5, name: "菜品5", date: "2019-04-15" },
        { id: 6, name: "菜品6", date: "2019-04-16" },
        { id: 7, name: "菜品7", date: "2019-04-17" },
        { id: 8, name: "菜品8", date: "2019-04-18" },
        { id: 9, name: "菜品9", date: "2019-04-19" },
        { id: 10, name: "菜品10", date: "2019-04-20" }
      ]
    };
  }
};
</script>

<style scoped>
.comment-box {
  padding: 40px 20px;
}
</style>
