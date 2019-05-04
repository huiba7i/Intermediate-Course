<template>
  <div class="dish-box">
    <h1 :style="{ 'text-align': 'left', 'padding': '20px' }">信息管理</h1>
    <Card class="dish-card">
      <Row class="menu">
        <Col :span="6">
          <ButtonGroup>
            <Button type="success" icon="md-add" @click="()=>{$router.push('/addUser')}">新增</Button>
            <Button type="info" icon="md-copy">保存</Button>
            <Button type="warning" icon="ios-albums-outline">审核</Button>
            <Button type="error" icon="ios-trash-outline">删除</Button>
          </ButtonGroup>
        </Col>
        <Col :span="6" :offset="3">
          <Dropdown :style="{ float: 'right' }" @on-click="changeOption">
            <Button v-text="this.option" :style="{ width: '100px' }">
              <Icon type="ios-arrow-down"></Icon>
            </Button>
            <DropdownMenu slot="list" :style="{ width: '100px' }">
              <DropdownItem name="分页">分页</DropdownItem>
              <DropdownItem name="全部">全部</DropdownItem>
            </DropdownMenu>
          </Dropdown>
        </Col>
        <Col :span="9">
          <Date-picker type="date" placeholder="选择开始日期" v-model="startDay" style="width: 200px"></Date-picker>-
          <Date-picker type="date" placeholder="选择结束日期" v-model="endDay" style="width: 200px"></Date-picker>
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
      <Page
        :total="dataPage.countTotal"
        :page-size="dataPage.pageSize"
        @on-change="tabData"
        show-elevator
        show-total
        v-show="this.isShow"
      />
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
          width: 300,
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
                    marginRight: "10px"
                  },
                  on: {
                    click: () => {
                      this.update(params.row.id);
                    }
                  }
                },
                "修改"
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
                      this.remove(params.row);
                    }
                  }
                },
                "删除"
              )
            ]);
          }
        }
      ],
      dishesData: [],
      dataPage: [],
      option: "筛选",
      isShow: true,
      startDay: "",
      endDay: ""
    };
  },
  mounted() {
    this.getUserData(1);
  },
  methods: {
    // 分页获取用户信息
    getUserData(pageNum) {
      console.log(this.startDay, this.endDay);
      let par = {
        pageNum: pageNum,
        id: "",
        name: "",
        province: "",
        city: "",
        zip: "",
        startDay: this.startDay,
        endDay: this.endDay
      };

      this.$http
        .post("http://127.0.0.1:1111/cgi-bin/user_all_page.py", par, {
          emulateJSON: true
        })
        .then(resp => {
          console.log(resp);
          this.dataPage = resp.data;
          this.dishesData = resp.data.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
    // 分页
    tabData(e) {
      this.getUserData(e);
    },
    // 获取全部用户信息
    changeOption(e) {
      if (e == "全部") {
        this.option = e;
        this.isShow = false;
        this.$http
          .get("http://127.0.0.1:1111/cgi-bin/user_all.py")
          .then(resp => {
            // console.log(resp);
            this.dishesData = resp.data;
          })
          .catch(error => {
            console.log(error);
          });
      } else if (e == "分页") {
        this.option = e;
        this.isShow = true;
        this.getUserData(1);
      }
    },
    // 修改信息
    update(id) {
      this.$router.push({
        name: "updateUser",
        params: {
          id: id
        }
      });
    },
    // 删除用户
    remove(e) {
      this.$http
        .post(
          "http://127.0.0.1:1111/cgi-bin/user_delete.py",
          { id: e.id },
          { emulateJSON: true }
        )
        .then(resp => {
          console.log(resp);
          if (resp.data == "success") {
            this.$Message.success("删除成功");
            this.getUserData(1);
          }
        })
        .catch(error => {
          this.$Message.error("删除失败");
          console.error(error);
        });
    },
    // // 时间查找
    // timeLookup() {
    //   let par = {
    //     startDay: this.startDay,
    //     endDay: this.endDay
    //   };

    //   this.$http
    //     .post("http://127.0.0.1:1111/cgi-bin/user_all_page.py", par, {
    //       emulateJSON: true
    //     })
    //     .then(resp => {
    //       console.log(resp);
    //     })
    //     .catch(error => {
    //       console.error(error);
    //     });
    // },
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
.dish-box {
  padding: 40px 20px;
}
.menu {
  padding: 10px;
}
</style>
