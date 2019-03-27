function url(){
    let path = 'img/a.jpg';
    return new Promise(function(resolve, reject){
        resolve(path);
    });
}

function loadImg(){
    let p = url();
    // console.log(p);
    p.then((path)=>{
        const image = new Image();
        image.src = path;
        document.body.appendChild(image);
    }).catch((error)=>{
        console.log('出错啦');
    });
}