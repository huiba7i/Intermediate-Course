<template>
  <div class="content">
    <Row>
      <Col :xs="{ span: 24 }" :sm="{ span: 24 }" :md="{ span: 6, offset: 2 }" :lg="{ span: 6, offset: 1 }" :xl="{ span: 5, offset: 2 }" :xxl="{ span: 5, offset: 2 }" >
        <Card>
          <DoughuntChart></DoughuntChart>
        </Card>
      </Col>
      <Col :xs="{ span: 24 }" :sm="{ span: 24 }" :md="{ span: 6, offset: 2 }" :lg="{ span: 6, offset: 1 }" :xl="{ span: 5, offset: 2 }" :xxl="{ span: 5, offset: 2 }" >
        <Card>
          <BarSimple></BarSimple>
        </Card>
      </Col>
      <Col :xs="{ span: 24 }" :sm="{ span: 24 }" :md="{ span: 6, offset: 2 }" :lg="{ span: 6, offset: 1 }" :xl="{ span: 5, offset: 2 }" :xxl="{ span: 5, offset: 2 }" >
       <Card>
         <BasicLineChart></BasicLineChart>
       </Card>
      </Col>
    </Row>
    <Row class="row-chart">
      <Col :xs="{ span: 24 }" :sm="{ span: 24 }" :md="{ span: 18, offset: 2 }" :lg="{ span: 19, offset: 2 }" :xl="{ span: 19, offset: 2 }" :xxl="{ span: 19, offset: 2 }">
        <Card>
          <StackedAreaChart></StackedAreaChart>
        </Card>
      </Col>
    </Row>
  </div>
</template>

<script>
import DoughuntChart from './charts/doughnutChart'
import BarSimple from './charts/barSimple'
import BasicLineChart from './charts/basicLineChart'
import StackedAreaChart from './charts/stackedAreaChart'

export default {
  data() {
    return {};
  },
  components: {
    DoughuntChart,
    BarSimple,
    BasicLineChart,
    StackedAreaChart
  }

};
</script>

<style scoped>
.content {
  margin-top: 40px;
}
.row-chart{
  margin-top: 50px;
}
</style>
