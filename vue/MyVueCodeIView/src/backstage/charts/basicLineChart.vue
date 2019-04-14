<template>
  <div id="chartThree" :style="{ width: '300px', height: '300px'}"></div>
</template>

<script>
export default {
  data() {
    return {};
  },
  mounted() {
    this.drawingThree();
  },
  methods: {
    drawingThree() {
      let chart = this.$echarts.init(document.getElementById("chartThree"));

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
            data: [820, 932, 901, 934, 1290, 1330, 1320],
            type: "line"
          },
          {
            data: [180, 292, 391, 194, 520, 630, 1000],
            type: "line"
          }
        ]
      });
    }
  }
};
</script>

<style scoped>
</style>
