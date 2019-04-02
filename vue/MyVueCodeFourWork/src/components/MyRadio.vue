<template>
    <div>
        <label>性别:</label>
        <input type="radio" value="男" v-model="sex" v-on:change="val">男
        <input type="radio" value="女" v-model="sex" v-on:change="val">女
    </div>
</template>

<script>
export default {
    name: 'MyRadio',
    data(){
        return {
            sex: ''
        }
    },
    methods: {
        val(){
            this.$emit('sex', this.sex);
        }
    }
}
</script>