<template>
  <div id="chartThree" :style="{ width: '320px', height: '300px'}"></div>
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
      let lastWeek = [];
      let nowWeek = [];
      let chart = this.$echarts.init(document.getElementById("chartThree"));

      chart.setOption({
        legend: {
          top: '20px',
          orient: "horizontal",
          data: ["上周", "现周"]
        },
        xAxis: {
          type: "category",
          data: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        },
        yAxis: {
          type: "value"
        },
        tooltip: {
          trigger: "axis",
          axisPointer: {
            type: "cross",
            label: {
              backgroundColor: "#6a7985"
            }
          }
        },
        series: [{ type: "line" }]
      });

      this.$http
        .get("/cgi-bin/basicLineChart.py")
        .then(resp => {
          // console.log(resp);
          lastWeek = resp.data.slice(0, 7);
          nowWeek = resp.data.slice(7);

          chart.setOption({
            series: [
              {
                name: "上周",
                data: lastWeek,
                type: "line"
              },
              {
                name: "现周",
                data: nowWeek,
                type: "line"
              }
            ]
          });
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
};
</script>

<style scoped>
</style>
