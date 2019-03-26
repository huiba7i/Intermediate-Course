let a = 30;
document.writeln(a);

{
    let a = 3033;
    document.writeln(a);
}

const count = 30;

document.writeln(count);

const ftn = {
    "name": 11,
    "age": 32
}

document.writeln(ftn.name);

ftn.name = 22;

document.writeln(ftn.name);

let [aa, b, c] = [ 11, 32, 33 ];
document.writeln(aa, b, c);

let obj = {
    fist: 'hello',
    last: 'world'
}
let { fist: f, last: l } = obj;
document.writeln(f, l);

let {fo = true} = [];
document.writeln(fo+"<br>");

let { x, y=3 } = { x: 10, y:13 }
document.writeln(x, y);