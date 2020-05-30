const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const { VueLoaderPlugin } = require('vue-loader');

module.exports = {
    watch: true,
    entry: ['./index.js', './index.scss'],
    output: {
        filename: 'app.js',
        path: path.resolve(__dirname, "../assets/dist"),
    },
    module: {
        rules: [
            {
                test: /\.vue$/,
                use: 'vue-loader'
            },
            {
                test: /\.module\.s(a|c)ss$/,
                loader: [
                    {
                        loader: 'css-loader',
                        options: {
                        modules: true,
                        sourceMap: false
                        }
                    },
                    {
                        loader: 'sass-loader',
                        options: {
                        sourceMap: false
                        }
                    }
                ]
            },
            {
                test: /\.s(a|c)ss$/,
                exclude: /\.module.(s(a|c)ss)$/,
                loader: [
                    MiniCssExtractPlugin.loader,
                    'css-loader',
                    {
                        loader: 'sass-loader',
                        options: {
                        sourceMap: false
                        }
                    }
                ]
            }
        ],
    },
    plugins: [
        new MiniCssExtractPlugin({
            filename: 'app.css',
            chunkFilename: 'app.css'
        }),
        new VueLoaderPlugin()
    ],
    resolve: {
        extensions: ['.js', '.scss', '.vue']
    }
}