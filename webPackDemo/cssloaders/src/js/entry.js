document.write('配置文件');

var a = require('./module');
document.writeln(a.name);

require('../css/index.css');
require('../css/index.less');

var oImg = new Image();
oImg.src = require('../img/taobao_logo.gif');
document.body.appendChild(oImg);

import json from '../data/student.json';

console.log(json);

// (10)、定义一个Generator函数，就是一个普通的函数，需要在function和函数名之间添加*
function* testGenerator(){
    console.log('hello');
    yield 'hello';  // 产出一个状态值
    console.log('world');
    yield 'world';
  
    console.log('end');
    return 'end';
}  

// 调用Generator()返回的是迭代器对象
// let it = testGenerator();
// console.log(it);

// console.log(it.next());
// let stat = it.next();
// console.log(stat, stat.value, stat.done);

// for ( let item of it )
// {
//     console.log(item);
// }


// 作为遍历器的生成函数使用
let obj = {
    name: '小白',
    age: 1,
    color: 'black'
  }
  // obj is not iterable:obj对象不可迭代的
  /* for(let prop of obj){
    console.log(prop)
  } */
  
  // console.log(obj.name, obj['name']);
  
  // 给对象部署一个Iterator接口 迭代器,通过[Symbol.iterator]
  obj[Symbol.iterator] = function*(){
    yield this.name;
    yield this.age;
    yield this.color;
  }
  
  for(let prop of obj){
    console.log(prop);
  }
  