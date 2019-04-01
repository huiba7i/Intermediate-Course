import Vue from 'vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import axios from 'axios'

Vue.config.productionTip = false

let vm = new Vue({
    el: '#app',
    data: {
        items: []
    },
    created(){
        // 请求模拟数据
        axios.get('/static/commodity.json').then((resp)=>{
            vm.items = resp.data;
        }).catch((error)=>{
            console.error(error);
        });
    },
    methods: {
        // 减少
        reduce(index){
            if ( vm.items[index].num == 1 ){
                alert('数量最低为一哦');
                return;
            }
            --vm.items[index].num;
        },
        // 添加
        increase(index){
            ++vm.items[index].num;
        },
        // 删除一条数据
        delSingle(index){
            let name = vm.items[index].name;
            let r = confirm(`确定要删除 ${name} 吗？`);
            if ( r == true ){
                vm.items.splice(index, 1);
            }
        }
    },
    filters: {
        // 在价格前添加￥
        currency: function(value){
            let t = /^[0-9]/;
            if ( t.test(value) ){
                return '￥' + value;
            }
        }
    },
    computed: {
        // 计算总数量
        totalNumber: function(){
            let tNumber = 0;
            for ( let item of vm.items ){
                tNumber += Number(item.num);
            }
            return tNumber;
        },
        // 计算总金额
        totalSum: function(){
            let tSum = 0;
            for ( let item of vm.items ){
                tSum += Number(item.price)*item.num;
            }
            return tSum;
        }
    }
});