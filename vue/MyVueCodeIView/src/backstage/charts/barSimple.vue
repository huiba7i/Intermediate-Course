<template>
  <div id="chartTwo" :style="{ width: '300px', height: '300px'}"></div>
</template>

<script>
export default {
  data() {
    return {};
  },
  mounted() {
    this.drawingTwo();
  },
  methods: {
    drawingTwo() {
      let chart = this.$echarts.init(document.getElementById("chartTwo"));

      chart.setOption({
        xAxis: {
          type: "category",
          data: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        },
        yAxis: {
          type: "value"
        },
        series: [
          {
            data: [120, 200, 150, 80, 70, 110, 130],
            type: "bar"
          }
        ]
      });
    }
  }
};
</script>

<style scoped>
</style>
