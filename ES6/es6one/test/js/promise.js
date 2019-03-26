
// 原始方法
// function sendRequest(){
//    let xhr = new XMLHttpRequest();

//    xhr.open('get', 'data/1.txt');

//    xhr.onreadystatechange = function(){
//        if ( xhr.readyState == 4 && xhr.status == 200 ){
//            let data = xhr.responseText;
//            console.log(data);
//            document.getElementById('txt').innerHTML = data;
//        }
//    }

//    xhr.send();
// }

// // 使用Promise进行异步操作
// function createPromise(){
//     return callback(['data/1.txt']);
// }

// 请求单个文件
// function sendRequest(){
//     // 创建Promise对象
//     let p = createPromise();
//     // 添加成功回调函数
//     p.then((data)=>{
//         document.getElementById('txt').innerHTML = data;
//     });
// }

// // 请求多个文件
// function sendRequest(){
//     let p = createPromise();
//     p.then(([dataOne])=>{
//         let n = ['data/2.txt', dataOne];
//         return callback(...n);
//     }).then( (  [val1, val2Arr] )=>{
//         let n = ['data/3.txt', val1, val2Arr];
//         return callback(...n);
//     } ).then( ( [val1, val2Arr] ) =>{
//         let val2Txt = () => {
//             let txt = '';
//             for (let val2 of val2Arr) {
//                 txt += val2 + " ";
//             }
//             return txt;
//         }
//         console.log(val2Txt());
//         // 第一个显示的是数据是最后请求的数据
//         document.getElementById('txt').innerHTML += `${val1}    ${val2Txt()}`
//     });
// }

// // 使用Promise.all()，并行多个异步操作
// function sendRequest(){
//     let p1 = callback(...['data/1.txt']);
//     let p2 = callback(...['data/2.txt']);
//     let p3 = callback(...['data/3.txt']);

//     Promise.all([p1, p2, p3]).then((data)=>{
//         let txt = () => {
//             let countent = '';
//             for ( let p of data ){
//                 countent += p[0] + " ";
//             }
//             return countent;
//         }
//         console.log(txt());
//         document.getElementById('txt').innerHTML = `${txt()}`;
//     }).catch(()=>{ console.error('error'); });
// }

// 封装ajax函数
function callback(path, ...data){
    let p = new Promise(function(resolve, reject){
        let xhr = new XMLHttpRequest();
        xhr.open('get', path);
        xhr.onreadystatechange = function(){
            if ( xhr.readyState == 4 && xhr.status == 200 ){
                // 操作成功，执行resolve，并把响应成功的文本传过去，返回的是二维数组
                resolve([xhr.responseText, data]);
                // console.log(xhr.responseText, data);
            }
        } 
        xhr.send();
    });

    return p;
}