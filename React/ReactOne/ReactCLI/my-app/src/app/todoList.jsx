import React from 'react'
import List from './list.jsx'
import Add from './addItem.jsx'

class todoList extends React.Component {
    constructor() {
        super();
        this.state = {
            arr: ["css", "html", "javascript"],
            newVal: ''
        }
    }

    changeVal = (event) => {
        this.setState({ newVal: event.target.value });
    }

    addVal = () =>　{
        this.state.arr.push(this.state.newVal);
        console.log(this.state.arr);
        // 强制更新state
        this.setState({arr: this.state.arr})
    }

    deleteItem = (i) => {
        console.log(i);
        this.state.arr.splice(i, 1);
        // this.setState({arr: this.state.arr})
    }

    render() {
        return (<div>
            <Add changeVal={this.changeVal} addVal={this.addVal}></Add>
            <List todoList={this.state.arr} delItem={this.deleteItem}></List>
        </div>)
    }
}

export default todoList;