<template>
  <div class="basic-box">
    <h1 :style="{ 'text-align': 'left', 'padding': '20px' }">基本用户</h1>
    <Card class="basic-card">
      <Table :columns="columns3" :data="basicUserData" :style="{margin: '20px'}"></Table>
    </Card>
  </div>
</template>

<script>
export default {
  data() {
    return {
      columns3: [
        {
          title: "账户姓名",
          key: "userName",
          render: (h, params) => {
            return h("div", [
              h("Icon", {
                props: {
                  type: "person"
                }
              }),
              h("strong", params.row.userName)
            ]);
          }
        },
        {
          title: "账户密码",
          key: "userPwd"
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
      basicUserData: [
        { userName: "admin", userPwd: "123456" },
        { userName: "admin", userPwd: "123456" },
        { userName: "admin", userPwd: "123456" }
      ]
    };
  },
  methods: {
    show(index) {
      this.$Modal.info({
        title: "User Info",
        content: `Name：${this.basicUserData[index].userName}<br>
        <br>Password${this.basicUserData[index].userPwd}`
      });
    },
    remove(index) {
      this.basicUserData.splice(index, 1);
    }
  }
};
</script>

<style scoped>
.basic-box {
  padding: 40px 20px;
  position: relative;
}
</style>
