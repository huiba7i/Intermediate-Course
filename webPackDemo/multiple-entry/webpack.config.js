var HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
    // 开发模式
    mode: 'development',
    // 入口文件(打包前)
    entry: {
        one: './src/js/one.js',
        two: './src/js/two.js'
    },
    // 出口文件(打包后)
    output: {
        filename: '[name].bundle.js',
        path: __dirname + '/dist'
    },
    // 使用自动生成html模块
    plugins: [
        new HtmlWebpackPlugin({
            filename: 'index.html', // 文件名称
            chunks: ['one']   // 依赖的文件
        }),
        new HtmlWebpackPlugin({
            filename: 'two.html',
            chunks: ['two']
        })
    ],
    // 使用webpack服务器，启动服务器，会在输出目录自动查找index.html，做为主页面
    devServer: {
        port: 8888,
        contentBase: __dirname + '/dist'
    }


}