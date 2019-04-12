import React from 'react'

class HelloWorld extends React.Component {
    render() {
        return (<div className="test">
            <h1>React 组件 (导入组件)</h1>
            <h2>组件传值 {this.props.name} </h2>
        </div>);
    }
}

export default HelloWorld;