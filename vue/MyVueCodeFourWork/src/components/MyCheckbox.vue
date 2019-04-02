<template>
    <div>
        <label>爱好:</label>
        <input type="checkbox" value="足球" v-model="likes" v-on:change="val">足球
        <input type="checkbox" value="篮球" v-model="likes" v-on:change="val">篮球
        <input type="checkbox" value="乒乓球" v-model="likes" v-on:change="val">乒乓球
        <input type="checkbox" value="排球" v-model="likes" v-on:change="val">排球
    </div>
</template>

<script>

export default {
    name: 'MyCheckbox',
    data(){
        return {
            likes: []
        }
    },
    methods: {
        val(){
            this.$emit('value', this.likes);
        }
    }
}
</script>