<template>
  <div id="app">
    <img src="./assets/logo.png">
    <MyRadio @sex="get"/>
    <MyCheckbox @value="getValue"/>
    <p>性别:{{ getVal }}</p>
    <span>爱好:</span><span v-for="like in getLikes" :key="like">{{ `${like}  ` }}</span>
  </div>
</template>

<script>
import MyRadio from './components/MyRadio'
import MyCheckbox from './components/MyCheckbox'

export default {
  name: 'App',
  data(){
    return {
      getVal: '',
      getLikes: []
    }
  },
  components: {
    'MyRadio': MyRadio,
    'MyCheckbox': MyCheckbox
  },
  methods: {
    get(data){
      this.getVal = data;
    },
    getValue(data){
      this.getLikes = data; 
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
