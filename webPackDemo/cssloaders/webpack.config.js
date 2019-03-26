var HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
    // 指定模式
    mode: 'development',
    // entry属性 配置入口文件
    entry: './src/js/entry.js',
    // output属性 配置打包后的输出文件
    output: {
        filename: 'bundle.js', // 输出文件的名称
        path: __dirname + '/dist' // 输出文件所在的目录,必须是绝对路径
    },
    module: {
        rules: [
            // 加载器从右到左加载
            { test: /\.css$/, loader: [ 'style-loader', 'css-loader' ] },
            { test: /\.less$/, loader: ['style-loader', 'css-loader','less-loader' ] },
            // 解析图片，适合解析小图片
            { test: /.(jpg|png|gif|svg)$/, use: [
                {
                    loader: 'url-loader',
                    options: {
                        limit: 8*1024
                    }
                }
            ]}
        ]
    },
    plugins: [new HtmlWebpackPlugin()],
    devServer: {
        port: 8888,
        contentBase: __dirname
    }
}
