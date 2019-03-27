console.log('-----1. 建立一个Map对象,里面保存的Key - value 分别是省名和省会名。测试:根据用户输入一个省名,打印出对应的省会名,如果map中没有这个省名,则打印出”无这样的信息”。-----');
let txt = document.getElementById('name');
let map = new Map();
map
.set('安徽省', '合肥市')
.set('江苏省', '南京市')
.set('浙江省', '杭州市')
.set('河南省', '郑州市')
.set('山东省', '济南市')
.set('河北省', '石家庄市')
.set('吉林省', '长春市');

txt.onchange = () => { map.has(txt.value) ? alert(map.get(txt.value)) : alert('无信息') }

console.log('-----2. 写一个程序，使用Set来存放一些石头(构造函数模板名称Rock) 对象，并迭代输出石头的名字。------');

function Rock(name){
    this.name = name;
}
let set = new Set();
set.add(new Rock('翡翠'));
set.add(new Rock('和田玉'));
set.add(new Rock('钻石'));

set.forEach( (value, key) => console.log(value.name) );

console.log('-----3. 通过 Symbol.iterator 给一个对象设置默认的遍历器------');

let obj = {
    name: '狸花猫',
    age: 1,
    color: '鲭鱼纹'
}

obj[Symbol.iterator] = function*(){
    yield this.name;
    yield this.age;
    yield this.color;
}

for(let prop of obj){
console.log(prop);
}

console.log('-----1. 使用Proxy代理器对对象的访问进行拦截,如果访问目标对象不存在的属性，会抛出一个错误。------');

let interceptor = {
    get: function(obj, objKey, receiver){
        if ( objKey in obj )
        {
            return obj[objKey];
        }
        else
        {
            throw new Error('不存在');
        }
        // return obj[objKey];
    }
}

let proxy = new Proxy(obj, interceptor);

console.log(proxy.name);

console.log('-----2. Promise异步加载一张图片定义一个函数,参数传入一个图片的url地址,返回一个Promise对象,该Promise在图片下载完成的时候resolve,并将下载的图片显示在页面中,下载失败则reject。-----');

function url(){
    let path = 'img/a.jpg';
    return new Promise(function(resolve, reject){
        resolve(path);
    });
}

function loadImg(){
    let p = url();
    console.log(p);
    p.then((path)=>{
        const image = new Image();
        image.src = path;
        document.body.appendChild(image);
    }).catch((error)=>{
        console.log('出错啦');
    });
}

console.log('-----1.所有的电器都有用电的方法，电视也用电，但是还可以放电影，手机电视还可以打电话。利用继承关系实现。-----');
class anElectricAppliance{
    constructor(name){
        this.name = name;
    }
    use(){
        return `看，广场是的人们都在看${this.name}`;
    }
}

let a = new anElectricAppliance('电视');
console.log(a.use());

class anElectricApplianceB extends anElectricAppliance{
    constructor(name){
        super(name);
    }
}

let b = new anElectricApplianceB('手机');
console.log(b.use());
console.log(b);

console.log(`----- 
2.编写2个类：Monkey类、People类。要求： 
(1) Monkey类中有个构造方法：constructor (name)，并且有个speak() 方法，输出“小样的，不错嘛！会说话了！”的信息。
(2)People类是Monkey类的子类，在People类中添加新方法think()，在think方法中输出“别说话！认真思考！” 的信息。 
-----`);

import Monkey from './monkey.js';
let monkey = new Monkey('狒狒');
console.log(monkey.speak());

import people from './prople.js';
let peo = new people('项羽');
console.log(peo.think());
peo.process();
peo.result();

console.log(`-----3.定义一个Student类，其中包括学号、姓名、性别、出生年月等属性以及display( )方法——显示各属性。实现并测试这个类。-----`);

import student from './student.js';
let stu = new student("001", "狒狒", "男", "0101");
stu.display();

console.log(`-----4.从上题的Student类中派生出子类Graduate(研究生)，添加属性：专业subject、导师adviser。-----`);

import graduate from './graduate.js';
let gra = new graduate('002', '沈阳', '女', '0202', '金融', '巴菲特' );
gra.displayTwo();