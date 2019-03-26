"use strict";

var a = 30;
document.writeln(a);

{
    var _a = 3033;
    document.writeln(_a);
}

var count = 30;

document.writeln(count);

var ftn = {
    "name": 11,
    "age": 32
};

document.writeln(ftn.name);

ftn.name = 22;

document.writeln(ftn.name);

var aa = 11,
    b = 32,
    c = 33;

document.writeln(aa, b, c);

var obj = {
    fist: 'hello',
    last: 'world'
};
var f = obj.fist,
    l = obj.last;

document.writeln(f, l);

var _fo = [].fo,
    fo = _fo === undefined ? true : _fo;

document.writeln(fo + "<br>");

var _x$y = { x: 10, y: 13 },
    x = _x$y.x,
    _x$y$y = _x$y.y,
    y = _x$y$y === undefined ? 3 : _x$y$y;

document.writeln(x, y);