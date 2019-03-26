// 1、参数使用默认值
function getPrice(price, t=1){
    return price*t;
}

let newPrice = getPrice(10);
console.log(newPrice);
newPrice = getPrice(100, 10);
console.log(newPrice);
console.log('——————————————————————————————————————————————————————————');

// 2、函数的length， name属性
console.log("函数参数的个数", getPrice.length); // 不包括默认值参数
console.log("函数名称", getPrice.name);
console.log('——————————————————————————————————————————————————————————');

// 3、arguments|this|...
//函数的rest参数（...参数名称），用于接收多余的实际参数值，替代了arguments对象
function add(a, ...b){
    console.log(a, b);
}
add(1, 2, 3, 4, 5);
add(3, 99);
add(11);
add();
console.log('——————————————————————————————————————————————————————————');

// 4、箭头函数
let sum = function(n){
    let s = 0;
    for ( let i = 1; i <= n; i ++ )
    {
        s += i;
    }

    return s;
}

console.log(sum(100));

// 4-1、参数只有一个时，()可省，函数体只有一条语句时，{}可省
let addSum = n => n+1;
console.log(addSum(1000));

// 4-2、this：普通函数中的this指向，随着运行的环境而变化，this的指向是可变的
console.log("默认指向window", this);
function test(){
    console.log("函数this", this);
}
// 普通调用this默认指向window
test();
// 构建函数调用this则指向：新创建的对象
new test();

// 4-3、箭头函数没有自己的this，其中的this指向的是定义时所在的对象，它的指向是固定的
let nav = () => { console.log("箭头函数",this); };
nav();

// 4-4、函数内部直接使用this默认指向window，可以把this赋值给一个变量
function Person(name, age){
    this.name = name;
    this.age = age;
    self = this;

    setInterval(function(){
        // this.age++;
        // console.log("默认this", this.age);      // 默认指向window

        // self.age++;
        // console.log("把this赋值给变量",self.age);   // 变量
    }, 1000);
}

// 使用箭头函数，this指的是当前函数
function Person(name, age){
    this.name = name;
    this.age = age;

    // setInterval(() => {
    //     this.age++;
    //     console.log("使用箭头函数", this.age);
    // }, 1000);
}

let per = new Person("zz", 10);

console.log('——————————————————————————————————————————————————————————');
// (5)、数组的扩展
// 5-1、spread(...)，好比rest参数的逆运算，将一个数组转为用逗号分隔的参数序列
function add(x, y){
    return x + y;
  }
  let numbers = [10, 20];
console.log(add(...numbers));

// 5-2、Array.from() 将类似数组对象，转换为真正的数组
let list = {
    0: 'html',
    1: 'css',
    2: 'js',
    length: 3
}

var arrList = Array.from(list);
console.log(arrList);
console.log('——————————————————————————————————————————————————————————');

// (6)、模板字符串
let name = 'Tom';
console.log(`Hello ${name}`);
console.log('——————————————————————————————————————————————————————————');


// (7)、for...of用于遍历数组和类数组对象，注意区分for...in（遍历对象中的属性）
let names = ['tom', 'qq', 'jum'];
for ( let n of names )
{
    console.log(n);
}
console.log('——————————————————————————————————————————————————————————');

// (8)、Map：相当于一个容器，可以存放"键值对"形式的数据
let m = new Map();
console.log(m);
let o = {p: 'hello world'};
m.set(o, 'content');
console.log(m.get(o));
console.log(m.delete(o));

// 如果对同一个键多次赋值，后面的值将覆盖前面的值
m.set(1, 'aaa').set(1, 'bbb');
console.log(m.get(1));

console.log(m.size);
console.log(m.set(1, 'aaa111'));
console.log(m.set(3, 'ccc'));
console.log(m.get(3), m.get(4));  // undefined
console.log(m.has(1));  // true
console.log(m.size);
console.log(m.delete(4));   // false
console.log(m.clear());
console.log(m.size);

// 8-1、WeakMap：键只能是对象，方法只有4个 delete,get,set,has
let wm = new WeakMap();
console.log(wm);
let wmObj = {'name':'Tom', 'age':10 };
wm.set(wmObj, 'aowin');
console.log(wm);

// 8-2、set：也是一个容器，存储单值数据，不能存储重复的数据 
let ss = new Set();
ss.add(11);
ss.add(12);
ss.add(13);
ss.add(14);
console.log('set', ss);

[1, 2, 3, 11, 12, 13, 14].forEach(x => {
    ss.add(x);
});

console.log("数组添加数据SET", ss);

// 8-3、WeakSet与WeakMap相似，只能存储对象，不能重复

// 9-4、Iterator接口遍历器，提供for...of进行遍历
let ma = new Map();
ma.set("o1", 'content1');
ma.set("o2", 'content2');
ma.set("o3", 'content3');
let ssKey = ma.keys();
for ( let k of ssKey )
{
    console.log("遍历Map的键名",k);
}
let ssV = ma.values();
for ( let k of ssV )
{
    console.log("遍历Map的键值",k);
}
let ssEnt = ma.entries();
for ( let k of ssEnt )
{
    console.log("遍历Map的键值对",k);
}

console.log('——————————————————————————————————————————————————————————');

// (9)、Symbol
let sid = Symbol('id');
console.log(sid, typeof(sid));

let obj = {
    [Symbol('random')]:'This is a Symbo',
    name: 'Tom',
    age: 10
}

// 获取对象中的Symbol属性
let s = Object.getOwnPropertySymbols(obj)[0];
console.log(s, obj[s]);

// 获取对象中的所有属性，不包括Symbols
let sName = Object.getOwnPropertyNames(obj);
console.log(sName[0], sName[1]);

let arr = [11, 33, 22];
console.log(arr);
let it = arr[Symbol.iterator]();
let ol = it.next();
console.log(ol);
console.log(it.next());
console.log(it.next());
console.log(it.next());

console.log('——————————————————————————————————————————————————————————');

