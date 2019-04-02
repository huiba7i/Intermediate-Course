<template>
  <div id="app">
    <h1>
      {{ msg }}
      <!-- 向下传入数据使用v-bind(:)
      向下传入事件使用v-on(@)-->
      <Test :pContent="content" :pCount="count" @addCount="addCount"></Test>
    </h1>
  </div>
</template>

<script>
import Test from "./Test.vue";
export default {
  name: "HelloWorld",
  data() {
    return {
      msg: "外部组件，父组件",
      content: "父组件数据",
      count: 0
    };
  },
  components: {
    Test: Test
  },
  methods: {
    addCount() {
      this.count++;
    }
  },
  beforeCreate() {
    console.log("App初始化之前========");
    console.log("App data: ", this.$data);
  },
  created() {
    console.log("App初始化之后========");
    console.log("App data: ", this.$data);
  },
  beforeMount() {
    console.log("App挂载之前========");
    console.log("App vm:", this);
  },
  mounted() {
    console.log("App挂载之后========");
    console.log("App vm:", this);
  },
  beforeUpdate() {
    console.log("App更新数据之前========");
    console.log("App vm:", this);
  },
  updated() {
    console.log("App更新数据之后========");
    console.log("App vm:", this);
  }
};
</script>

<style scoped>
h1 {
  background-color: blue;
  color: white;
}
</style>


