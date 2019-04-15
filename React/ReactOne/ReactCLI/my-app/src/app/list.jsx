import React from 'react'
import '../../src/list.css'

class list extends React.Component {
    constructor(props) {
        super(props);
    }
    render() {
        return (
            <ul className="listUl">
                {
                    this.props.todoList.map((name, index) => {
                        return (
                            // key区分虚拟dom，渲染不同的key标签
                            <li className="listLi" key={index}>
                                <span>{name}</span>
                                <div className="listDel">
                                    <button className="del" onClick={()=>{this.props.delItem(index)}}>删除</button>
                                </div>
                            </li>
                        )
                    })
                }
            </ul>
        )
    }
}

export default list;