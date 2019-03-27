let name = 'Tom';
let ageN = 'age';
let key = Symbol('Symbol描述');

let proto = {
    foo: 'hello'
}

let obj = {
    name: name,
    [ageN]: 100,
    ['a'+'bc']: 124,
    ['a'+'cc'](){
        console.log('表达式还可以定义方法名');
    },
    info(){
        console.log('对象里直接定义方法');
    },
    [key]() {},
    foo: 'world',
    find(){
        console.log('当前对象的foo值是：', this.foo, '\nsuper，指向当前对象的原型对象，foo的值是', super.foo);
    }
}

// console.log('返回对象里属性或方法的名称',obj[key].name);
// console.log('for...in循环遍历对象自身的和继承的可枚举属性（不含 Symbol 属性）。');
// // for ( let o in obj ){ console.log(o); }
// console.log('Object.keys返回一个数组，包括对象自身的（不含继承的）所有可枚举属性（不含 Symbol 属性）的键名。', Object.keys(obj));
// console.log('Object.getOwnPropertyNames返回一个数组，包含对象自身的所有属性（不含 Symbol 属性，但是包括不可枚举属性）的键名。', Object.getOwnPropertyNames(obj));
// console.log('Object.getOwnPropertySymbols返回一个数组，包含对象自身的所有 Symbol 属性的键名。', Object.getOwnPropertySymbols(obj));
// console.log('返回一个数组，包含对象自身的所有键名，不管键名是 Symbol 或字符串，也不管是否可枚举。',Reflect.ownKeys(obj));


// Object.setPrototypeOf(obj, proto);
// obj.find();

console.log('-----ES5构造函数-----');

// function info(name, age, gender){
//     this.name = name;
//     this.age = age;
//     this.gender = gender;

//     // 创建对象方法
//     this.objFun = function(){
//         console.log(`对象方法，只有new对象可以使用的方法。他叫${this.name},今年${this.age}岁了。`);
//     }
// }

// // 创建原型方法
// info.prototype.test = function(){
//     console.log(`原型方法，所有new对象都可以使用的方法,他叫${this.name},今年${this.age}岁了。`);
// }

// // 创建静态方法，定义在构造函数上的方法，不需要new对象使用
// info.staticTest = function(){
//     console.log('静态方法，可以直接调用，不需要new对象');
// }

// info.staticTest();

// let fun1 = new info('Tom', 20, '男');
// fun1.objFun();
// fun1.test();

// let fun2 = new info('Jo', 22, '女');
// fun2.test();
// fun2.objFun();

console.log('-----ES6构造函数-----');

class info{
    constructor(name, age, gender){
        this.name = name;
        this.age = age;
        this.gender = gender;

        // 对象方法
        this.objFun = function(){
            console.log(`对象方法，只有new对象可以使用的方法。他叫${this.name},今年${this.age}岁了。`);
        }
    }

    // 原型方法
    test(){
        console.log(`原型方法，所有new对象都可以使用的方法,他叫${this.name},今年${this.age}岁了。`);
    }

    static staticTest(){
        console.log('静态方法，可以直接调用，不需要new对象');
    }
};

// info.staticTest();

// let fun1 = new info('MAMA', 100, '女');
// fun1.objFun();
// fun1.test();

// let fun2 = new info('Jo', 22, '女');
// fun2.test();
// fun2.objFun();

class info2 extends info{
    constructor(name, age, gender){
        super(name, age, gender);
    }
}
let n2 = new info2('asdf', 10, '女');
console.log(n2.name, n2.age, n2.gender);
n2.test();

// import {content, test} from './module.js';
// console.log(content);
// test();