"use strict";

var _obj;

var _typeof = typeof Symbol === "function" && typeof Symbol.iterator === "symbol" ? function (obj) { return typeof obj; } : function (obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; };

var _marked = /*#__PURE__*/regeneratorRuntime.mark(testGenerator);

function _defineProperty(obj, key, value) { if (key in obj) { Object.defineProperty(obj, key, { value: value, enumerable: true, configurable: true, writable: true }); } else { obj[key] = value; } return obj; }

// 1、参数使用默认值
function getPrice(price) {
    var t = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : 1;

    return price * t;
}

var newPrice = getPrice(10);
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
function add(a) {
    for (var _len = arguments.length, b = Array(_len > 1 ? _len - 1 : 0), _key = 1; _key < _len; _key++) {
        b[_key - 1] = arguments[_key];
    }

    console.log(a, b);
}
add(1, 2, 3, 4, 5);
add(3, 99);
add(11);
add();
console.log('——————————————————————————————————————————————————————————');

// 4、箭头函数
var sum = function sum(n) {
    var s = 0;
    for (var i = 1; i <= n; i++) {
        s += i;
    }

    return s;
};

console.log(sum(100));

// 4-1、参数只有一个时，()可省，函数体只有一条语句时，{}可省
var addSum = function addSum(n) {
    return n + 1;
};
console.log(addSum(1000));

// 4-2、this：普通函数中的this指向，随着运行的环境而变化，this的指向是可变的
console.log("默认指向window", undefined);
function test() {
    console.log("函数this", this);
}
// 普通调用this默认指向window
test();
// 构建函数调用this则指向：新创建的对象
new test();

// 4-3、箭头函数没有自己的this，其中的this指向的是定义时所在的对象，它的指向是固定的
var nav = function nav() {
    console.log("箭头函数", undefined);
};
nav();

// 4-4、函数内部直接使用this默认指向window，可以把this赋值给一个变量
function Person(name, age) {
    this.name = name;
    this.age = age;
    self = this;

    setInterval(function () {
        // this.age++;
        // console.log("默认this", this.age);      // 默认指向window

        // self.age++;
        // console.log("把this赋值给变量",self.age);   // 变量
    }, 1000);
}

// 使用箭头函数，this指的是当前函数
function Person(name, age) {
    this.name = name;
    this.age = age;

    // setInterval(() => {
    //     this.age++;
    //     console.log("使用箭头函数", this.age);
    // }, 1000);
}

var per = new Person("zz", 10);

console.log('——————————————————————————————————————————————————————————');
// (5)、数组的扩展
// 5-1、spread(...)，好比rest参数的逆运算，将一个数组转为用逗号分隔的参数序列
function add(x, y) {
    return x + y;
}
var numbers = [10, 20];
console.log(add.apply(undefined, numbers));

// 5-2、Array.from() 将类似数组对象，转换为真正的数组
var list = {
    0: 'html',
    1: 'css',
    2: 'js',
    length: 3
};

var arrList = Array.from(list);
console.log(arrList);
console.log('——————————————————————————————————————————————————————————');

// (6)、模板字符串
var name = 'Tom';
console.log("Hello " + name);
console.log('——————————————————————————————————————————————————————————');

// (7)、for...of用于遍历数组和类数组对象，注意区分for...in（遍历对象中的属性）
var names = ['tom', 'qq', 'jum'];
var _iteratorNormalCompletion = true;
var _didIteratorError = false;
var _iteratorError = undefined;

try {
    for (var _iterator = names[Symbol.iterator](), _step; !(_iteratorNormalCompletion = (_step = _iterator.next()).done); _iteratorNormalCompletion = true) {
        var n = _step.value;

        console.log(n);
    }
} catch (err) {
    _didIteratorError = true;
    _iteratorError = err;
} finally {
    try {
        if (!_iteratorNormalCompletion && _iterator.return) {
            _iterator.return();
        }
    } finally {
        if (_didIteratorError) {
            throw _iteratorError;
        }
    }
}

console.log('——————————————————————————————————————————————————————————');

// (8)、Map：相当于一个容器，可以存放"键值对"形式的数据
var m = new Map();
console.log(m);
var o = { p: 'hello world' };
m.set(o, 'content');
console.log(m.get(o));
console.log(m.delete(o));

// 如果对同一个键多次赋值，后面的值将覆盖前面的值
m.set(1, 'aaa').set(1, 'bbb');
console.log(m.get(1));

console.log(m.size);
console.log(m.set(1, 'aaa111'));
console.log(m.set(3, 'ccc'));
console.log(m.get(3), m.get(4)); // undefined
console.log(m.has(1)); // true
console.log(m.size);
console.log(m.delete(4)); // false
console.log(m.clear());
console.log(m.size);

// 8-1、WeakMap：键只能是对象，方法只有4个 delete,get,set,has
var wm = new WeakMap();
console.log(wm);
var wmObj = { 'name': 'Tom', 'age': 10 };
wm.set(wmObj, 'aowin');
console.log(wm);

// 8-2、set：也是一个容器，存储单值数据，不能存储重复的数据 
var ss = new Set();
ss.add(11);
ss.add(12);
ss.add(13);
ss.add(14);
console.log('set', ss);

[1, 2, 3, 11, 12, 13, 14].forEach(function (x) {
    ss.add(x);
});

console.log("数组添加数据SET", ss);

// 8-3、WeakSet与WeakMap相似，只能存储对象，不能重复

// 9-4、Iterator接口遍历器，提供for...of进行遍历
var ma = new Map();
ma.set("o1", 'content1');
ma.set("o2", 'content2');
ma.set("o3", 'content3');
var ssKey = ma.keys();
var _iteratorNormalCompletion2 = true;
var _didIteratorError2 = false;
var _iteratorError2 = undefined;

try {
    for (var _iterator2 = ssKey[Symbol.iterator](), _step2; !(_iteratorNormalCompletion2 = (_step2 = _iterator2.next()).done); _iteratorNormalCompletion2 = true) {
        var k = _step2.value;

        console.log("遍历Map的键名", k);
    }
} catch (err) {
    _didIteratorError2 = true;
    _iteratorError2 = err;
} finally {
    try {
        if (!_iteratorNormalCompletion2 && _iterator2.return) {
            _iterator2.return();
        }
    } finally {
        if (_didIteratorError2) {
            throw _iteratorError2;
        }
    }
}

var ssV = ma.values();
var _iteratorNormalCompletion3 = true;
var _didIteratorError3 = false;
var _iteratorError3 = undefined;

try {
    for (var _iterator3 = ssV[Symbol.iterator](), _step3; !(_iteratorNormalCompletion3 = (_step3 = _iterator3.next()).done); _iteratorNormalCompletion3 = true) {
        var _k = _step3.value;

        console.log("遍历Map的键值", _k);
    }
} catch (err) {
    _didIteratorError3 = true;
    _iteratorError3 = err;
} finally {
    try {
        if (!_iteratorNormalCompletion3 && _iterator3.return) {
            _iterator3.return();
        }
    } finally {
        if (_didIteratorError3) {
            throw _iteratorError3;
        }
    }
}

var ssEnt = ma.entries();
var _iteratorNormalCompletion4 = true;
var _didIteratorError4 = false;
var _iteratorError4 = undefined;

try {
    for (var _iterator4 = ssEnt[Symbol.iterator](), _step4; !(_iteratorNormalCompletion4 = (_step4 = _iterator4.next()).done); _iteratorNormalCompletion4 = true) {
        var _k2 = _step4.value;

        console.log("遍历Map的键值对", _k2);
    }
} catch (err) {
    _didIteratorError4 = true;
    _iteratorError4 = err;
} finally {
    try {
        if (!_iteratorNormalCompletion4 && _iterator4.return) {
            _iterator4.return();
        }
    } finally {
        if (_didIteratorError4) {
            throw _iteratorError4;
        }
    }
}

console.log('——————————————————————————————————————————————————————————');

// (9)、Symbol
var sid = Symbol('id');
console.log(sid, typeof sid === "undefined" ? "undefined" : _typeof(sid));

var obj = (_obj = {}, _defineProperty(_obj, Symbol('random'), 'This is a Symbo'), _defineProperty(_obj, "name", 'Tom'), _defineProperty(_obj, "age", 10), _obj);

// 获取对象中的Symbol属性
var s = Object.getOwnPropertySymbols(obj)[0];
console.log(s, obj[s]);

// 获取对象中的所有属性，不包括Symbols
var sName = Object.getOwnPropertyNames(obj);
console.log(sName[0], sName[1]);

var arr = [11, 33, 22];
console.log(arr);
var it = arr[Symbol.iterator]();
var ol = it.next();
console.log(ol);
console.log(it.next());
console.log(it.next());
console.log(it.next());

console.log('——————————————————————————————————————————————————————————');

// (10)、定义一个Generator函数，就是一个普通的函数，需要在function和函数名之间添加*
function testGenerator() {
    return regeneratorRuntime.wrap(function testGenerator$(_context) {
        while (1) {
            switch (_context.prev = _context.next) {
                case 0:
                    console.log('hello');
                    _context.next = 3;
                    return 'hello';

                case 3:
                    // 产出一个状态值
                    console.log('world');
                    _context.next = 6;
                    return 'world';

                case 6:

                    console.log('end');
                    return _context.abrupt("return", 'end');

                case 8:
                case "end":
                    return _context.stop();
            }
        }
    }, _marked, this);
}

// 调用Generator()返回的是迭代器对象
var itt = testGenerator();
console.log(itt);

console.log(te.next);
