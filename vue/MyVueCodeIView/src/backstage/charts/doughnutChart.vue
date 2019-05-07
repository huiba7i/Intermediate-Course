<template>
  <div id="chartOne" :style="{ width: '300px', height: '300px'}"></div>
</template>

<script>
export default {
  data() {
    return {
      chartData: []
    };
  },
  mounted() {
    this.drawingOne();
  },
  methods: {
    drawingOne() {
      let getName = [];
      let chart = this.$echarts.init(document.getElementById("chartOne"));

      chart.setOption({
        // 工具提示
        tooltip: {
          trigger: "item",
          formatter: "{a} <br/>{b}: {c} ({d}%)"
        },
        // 系列列表。每个系列通过 type 决定自己的图表类型
        series: [
          {
            center: ["55%", "60%"],
            name: "访问来源",
            type: "pie",
            radius: ["50%", "70%"],
            avoidLabelOverlap: false,
            label: {
              normal: {
                show: false,
                position: "center"
              },
              emphasis: {
                show: true,
                textStyle: {
                  fontSize: "30",
                  fontWeight: "bold"
                }
              }
            },
            labelLine: {
              normal: {
                show: false
              }
            }
          }
        ]
      });

      this.$http
        .get("/cgi-bin/doughnutChart.py")
        .then(resp => {
          // console.log(resp);
          for (let d of resp.data) {
            getName.push(d.name);
          }
          chart.setOption({
            // 图例组件
            legend: {
              orient: "vertical",
              x: "left",
              data: getName
            },
            series: [
              {
                data: resp.data
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
