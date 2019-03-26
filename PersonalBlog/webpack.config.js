module.exports = {
    mode: "development",
    entry: "./src/js/entry.js",
    output: {
        filename: "bundle.js",
        path: __dirname + '/dist'
    },
    module: {
        rules: [
            { test: /\.css$/, use: [ 'style-loader', 'css-loader' ] },
            { test: /\.less$/, use: [ 'style-loader', 'css-loader', 'less-loader' ] },
            { test: /\.[jpg|png|gif|svg]$/, use: [ 
                {
                    loader: 'url-loader',
                    options: {
                        limit: 8*1024
                    }
                }
            ] }
        ]
    }
}