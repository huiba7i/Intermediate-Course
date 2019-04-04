<template>
  <div>
    <h1>One</h1>
    <h3>{{ $store.getters.totalPrice }}</h3>
    <h1>{{ $store.state.uName }}</h1>

    <button @click="updateCount">修改count的值</button>
    <button @click="updateCountAsync">异步修改count的值</button>
  </div>
</template>

<script>
export default {
  data() {
    return {};
  },
  methods: {
    updateCount: function() {
      // 单个参数
      //   this.$store.commit('changeCount', 3);

      // 传递多个参数
      this.$store.commit({
        type: "changeCount",
        num: 3,
        str: "change"
      });
    },
    updateCountAsync: function() {
      this.$store.dispatch({
        type: "async",
        num: 2,
        str: "async"
      });
    }
  }
};
</script>

