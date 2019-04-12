import React from 'react'
import '../../src/list.css'

let arr = ["css", "html", "javascript"];
class list extends React.Component {
    render() {
        return (
            <ul className="listUl">
                {
                    arr.map(function (name) {
                        return (
                            <li className="listLi" key={name}>
                                <span>{name}</span>
                                <div className="listDel">
                                    <button className="del">删除</button>
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