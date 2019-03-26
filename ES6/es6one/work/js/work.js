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