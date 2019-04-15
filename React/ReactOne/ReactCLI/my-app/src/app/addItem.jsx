import React from 'react'
import '../../src/list.css'

class addItem extends React.Component {
    constructor(props) {
        super(props);

    }
    render() {
        return (
            <div>
                <input onChange={this.props.changeVal} type="text" id="inputtxt" placeholder="请输入..." />
                <button className="del" onClick={this.props.addVal} >添加</button>
            </div>
        )
    }
}

export default addItem;