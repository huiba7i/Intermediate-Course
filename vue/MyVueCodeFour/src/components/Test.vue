<template>
  <div>
    <h4>{{ msg }}</h4>
    <h4>{{ pContent }}</h4>
    <h4>父组件数据{{ pCount }}</h4>
    <button @click="add">修改父组件数据</button>
  </div>
</template>

<script>
export default {
  name: "Test",
  props: ["pContent", "pCount"],
  data() {
    return {
      msg: "嵌套组件，子组件"
    };
  },
  methods: {
    add() {
      this.$emit("addCount");
    }
  },
  beforeCreate() {
    console.log("Child初始化之前========");
    console.log("Child data: ", this.$data);
  },
  created() {
    console.log("Child初始化之后========");
    console.log("Child data: ", this.$data);
  },
  beforeMount() {
    console.log("Child挂载之前========");
    console.log("Child vm:", this);
  },
  mounted() {
    console.log("Child挂载之后========");
    console.log("Child vm:", this);
  },
  beforeUpdate() {
    console.log("Child更新数据之前========");
    console.log("Child vm:", this);
  },
  updated() {
    console.log("Child更新数据之后========");
    console.log("Child vm:", this);
  }
};
</script>

<style scoped>
h4 {
  background-color: black;
  color: width;
  overflow: hidden;
}
</style>


