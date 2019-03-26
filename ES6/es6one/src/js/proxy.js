// let target = { name:"Tom", age:12 };

// let interceptor = {
//     set: function(obj, prop, value){
//         if ( prop == 'age' ){
//             if ( Number.isNaN(value) ){
//                 console.log('必须输入数字');
//                 return;
//             } else if ( value<0 || value>=200 ){
//                 console.log('年龄不能小于0，或者大于200');
//                 return;
//             }
//             else{
//                 console.log('修改成功');
//             }
//         }
//         obj[prop] = value;
//         return true;
//     }
// }

// let proxy = new Proxy(target, interceptor);
// proxy.age = 8830;
// console.log(target.age);

let prom = new Promise(function(resolve, reject){
    reject('fail');
});

// 成功/失败，调用then回调函数
prom.then((result)=>{
    console.log(result);
}, (error)=>{
    console.log(error);
});

