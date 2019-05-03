<template>
  <div class="dish-box">
    <h1 :style="{ 'text-align': 'left', 'padding': '20px' }">菜品管理</h1>
    <Card class="dish-card">
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
      <Table
        stripe
        :style="{margin: '20px'}"
        border
        ref="selection"
        :columns="columns1"
        :data="dishesData"
      ></Table>
      <Page :total="100" show-elevator show-total/>
      <hr :style="{ 'margin': '20px' }">
      <p :style="{ 'text-align': 'left', 'margin': '20px' }">
        <span>注：...</span>
      </p>
    </Card>
  </div>
</template>

<script>
export default {
  data() {
    return {
      columns1: [
        {
          type: "selection",
          width: 60,
          align: "center"
        },
        {
          title: "ID",
          key: "id",
          sortable: true
        },
        {
          title: "Name",
          key: "name",
          sortable: true
        },
        {
          title: "Province",
          key: "province",
          sortable: true
        },
        {
          title: "City",
          key: "city",
          sortable: true
        },
        {
          title: "Address",
          key: "address",
          sortable: true
        },
        {
          title: "Zip",
          key: "zip",
          sortable: true
        },
        {
          title: "Date",
          key: "date",
          sortable: true
        },
        {
          title: "Action",
          key: "action",
          width: 150,
          align: "center",
          render: (h, params) => {
            return h("div", [
              h(
                "Button",
                {
                  props: {
                    type: "primary",
                    size: "small"
                  },
                  style: {
                    marginRight: "5px"
                  },
                  on: {
                    click: () => {
                      this.show(params.index);
                    }
                  }
                },
                "查看"
              ),
              h(
                "Button",
                {
                  props: {
                    type: "error",
                    size: "small"
                  },
                  on: {
                    click: () => {
                      this.remove(params.index);
                    }
                  }
                },
                "删除"
              )
            ]);
          }
        }
      ],
      dishesData: []
    };
  },
  mounted() {
    this.getUserData(1);
  },
  methods: {
    show(index) {
      this.$Modal.info({
        title: "User Info",
        content: `Name：${this.dishesData[index].id}<br>Age：${
          this.dishesData[index].name
        }<br>Address：${this.dishesData[index].date}`
      });
    },
    remove(index) {
      this.dishesData.splice(index, 1);
    },
    getUserData(pageNum) {
      console.log(pageNum);
      let par = {
        pageNum: pageNum,
        id: '',
        name: '',
        province: '',
        city: '',
        zip: '',
        startDay: '',
        endDay: ''
      };
      console.log(par)
      this.$http
        .post("http://127.0.0.1:1111/cgi-bin/user_all.py", par, {
          emulateJSON: true
        })
        .then(resp => {
          console.log(resp);
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
};
</script>

<style scoped>
.dish-box {
  padding: 40px 20px;
}
.menu {
  padding: 10px;
}
</style>
