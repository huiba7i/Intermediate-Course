import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';

import './list.css'


ReactDOM.render( <App /> , document.getElementById('root'));


// 三、使用继承创建组件，并引入
// import HelloWorld from './app/helloWorld.jsx'

// 二、使用组建类创建组件，React 16版本已废弃
// let HelloWorld = React.createClass({
//     render: function(){
//         return (<div className="test">
//             <h1>React 组件</h1>
//             <h2>组件传值 {this.props.name} </h2>
//         </div>);
//     }
// });

// 一、最原始写法
// let sty = { backgroundColor: 'blue', color: 'white' };
// let arr = [<h3>1</h3>, <h3>2</h3>, <h3>3</h3>];
// const element = (<div>
//     <h3 style={sty}>样式推荐使用内联样式</h3>
//     <h3>可以在大括号里写js表达式:{1 * 2 * 3}</h3>
//     <h2>可以使用数组{arr}</h2>
// </div>);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
