<template>
  <div id="chartOne" :style="{ width: '300px', height: '300px'}"></div>
</template>

<script>
export default {
  data() {
    return {};
  },
  mounted() {
    this.drawingOne();
  },
  methods: {
    drawingOne() {
      let chart = this.$echarts.init(document.getElementById("chartOne"));

      chart.setOption({
        // 工具提示
        tooltip: {
          trigger: "item",
          formatter: "{a} <br/>{b}: {c} ({d}%)"
        },
        // 图例组件
        legend: {
           
          orient: "vertical",
          x: "left",
          data: ["直接访问", "邮件营销", "联盟广告", "视频广告", "搜索引擎"]
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
            },
            data: [
              { value: 335, name: "直接访问" },
              { value: 310, name: "邮件营销" },
              { value: 234, name: "联盟广告" },
              { value: 135, name: "视频广告" },
              { value: 1548, name: "搜索引擎" }
            ]
          }
        ]
      });
    }
  }
};
</script>

<style scoped>
</style>
