import React, { Component } from 'react';
import './App.css';

import ToDoList from './app/todoList.jsx'

import 'antd/dist/antd.css';

class App extends Component {
  tick() {
    this.setState({
      time: new Date().toLocaleString()
    })
  }

  componentWillMount() {
    console.log('组件将安装')
  }
  componentDidMount() {
    console.log('组件已装入')
    this.time = setInterval(() => {
      this.tick()
    }, 1000)
  }
  componentWillReceiveProps(newProps) {
    console.log('组件收到props')
  }
  shouldComponentUpdate(newProps, newState) {
    return true;
  }
  componentWillUpdate(nextProps, nextState) {
    console.log('组件将更新！');
  }
  componentDidUpdate(prevProps, prevState) {
    console.log('组件已更新!')
  }
  componentWillUnmount() {
    console.log('组件将卸载!')
  }
  constructor() {
    super();
    this.state = {
      count: 4,
      price: 12.2
    }
  }

  addCount = () => {
    this.setState({ count: this.state.count + 1 });
  }

  render() {
    return (
      <div className="App">
        <p>当前时间：{this.state.time}</p>

        <header className="App-header">
          <h1>ToDoList</h1>
          <ToDoList></ToDoList>
        </header>
        {/* <div>
          count is:{this.state.count}
          price is:{this.state.price}<br />
          <p>总价格：{this.state.count * this.state.price}</p>
          <button onClick={this.addCount}>数量加1</button>
        </div> */}

      </div>
    );
  }
}

export default App;
