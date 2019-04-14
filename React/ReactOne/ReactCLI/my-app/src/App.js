import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import ToDoList from './app/todoList.jsx'

import 'antd/dist/antd.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <h3>欢迎来到React!</h3>
          <img src={logo} className="App-logo" alt="logo" />
          <ToDoList></ToDoList>
        </header>
      </div>
    );
  }
}

export default App;
