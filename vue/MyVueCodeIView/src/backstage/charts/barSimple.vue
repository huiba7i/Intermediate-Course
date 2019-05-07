<template>
  <div id="chartTwo" :style="{ width: '320px', height: '300px'}"></div>
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
      let getXName = [];
      let chart = this.$echarts.init(document.getElementById("chartTwo"));

      chart.setOption({
        tooltip: {
          trigger: "item",
          formatter: "{a} <br/>{b}: {c}"
        },
        xAxis: {
          type: "category"
        },
        yAxis: {
          type: "value"
        },
        series: [{ name: "销量", type: "bar" }]
      });

      this.$http
        .get("/cgi-bin/barSimble.py")
        .then(resp => {
          // console.log(resp);
          for (let r of resp.data) {
            getXName.push(r.name);
          }
          chart.setOption({
            xAxis: {
              data: getXName
            },
            series: [
              {
                data: resp.data,
                type: 'bar'
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
