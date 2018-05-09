const path = require('path');
const webpack = require('webpack');
const vueLoader = require('vue-loader');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const CopyWebpackPlugin = require('copy-webpack-plugin');


const outputPath = path.resolve(__dirname, '../../dist/');

let config = {
    mode: process.env.NODE_ENV || 'production',
    entry: path.resolve(__dirname, '../client/index.js'),
    output: {
        path: outputPath,
        filename: 'static/js/[name].[hash].js',
        chunkFilename: 'static/js/[id].[hash].js',
    },
    module: {
        rules: [
            {
                test: /\.vue$/,
                loaders: 'vue-loader',
                options: {
                    loaders: {
                        'scss': 'vue-style-loader!css-loader!sass-loader',
                        'sass': 'vue-style-loader!css-loader!sass-loader?intendedSyntax',
                    }
                },
                // Vue loader options
            },
            {
                test: /\.js$/,
                loader: 'babel-loader',
                exclude: /node_modules/
            },
            {
                test: /\.es6$/,
                loaders: ['babel-loader']
            },
            {
                test: /\.(png|jpe?g|gif|svg)$/,
                loader: 'file-loader',
                options: {
                    name: '[name].[ext]?[hash]'
                },
            },
            {
                test: /\.(css|sass|scss)$/,
                use: [
                    'vue-style-loader',
                    'css-loader',
                    'sass-loader',
                ],
            }
        ]
    },
    resolve: {
        alias: {
            'vue$': 'vue/dist/vue.esm.js',
            'static': path.resolve(__dirname, '../static'),
        },
    },
    devServer: {
        historyApiFallback: true,
        noInfo: true,
    },
    performance: {
        hints: false,
    },
    devtool: '#eval-source-map',
    plugins: [
        new vueLoader.VueLoaderPlugin(),
        new HtmlWebpackPlugin({
            title: "VGU Alumni",
            template: path.resolve(__dirname, '../index.html'),
            filename: path.join(outputPath, 'index.html'),
        }),
        new CopyWebpackPlugin([
            {
                from: path.resolve(__dirname, '../static'),
                to: path.join(outputPath, 'static'),
            }
        ]),
    ]
};

if (process.env.NODE_ENV === 'production') {
    config.devtool = '#source-map';
    config.optimization = {
        minimize: true,
    };
    config.plugins = (config.plugins || []).concat([
        new webpack.LoaderOptionsPlugin({
            minimize: true,
        }),
    ]);
}

module.exports = config;
