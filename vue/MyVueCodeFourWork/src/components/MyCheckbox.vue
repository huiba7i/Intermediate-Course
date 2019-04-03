<template>
    <div>
        <mycheckbox />
        <!-- <label>爱好:</label>
        <input type="checkbox" value="足球" v-model="likes" v-on:change="val">足球
        <input type="checkbox" value="篮球" v-model="likes" v-on:change="val">篮球
        <input type="checkbox" value="乒乓球" v-model="likes" v-on:change="val">乒乓球
        <input type="checkbox" value="排球" v-model="likes" v-on:change="val">排球 -->
    </div>
</template>

<script>
// let mycheckbox = {
//     data(){
//         return{
//             likes: [],
//             checkName: [ "足球", "篮球", "乒乓球", "排球" ]
//         }
//     },
//     methods: {
//         val(){
//             this.$emit('value', this.likes);
//         }
//     },
//     template: '<div><label>爱好:</label><span v-for="name in checkName" :key="name"><input type="checkbox" :value="name" v-model="likes" v-on:change="val"><span>{{name}}</span></span></div>'
// }

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
    },
    components: {
        mycheckbox
    }
}
</script>