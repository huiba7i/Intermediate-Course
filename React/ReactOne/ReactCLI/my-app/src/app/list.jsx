import React from 'react'
import '../../src/list.css'
import 'antd/dist/antd.css';

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
                                    {/* <button className="del">删除</button> */}
                                    <Button type="danger">删除</Button>
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