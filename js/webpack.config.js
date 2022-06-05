const {resolve} = require('path');
const webpack = require('webpack');

const PACKAGE_ROOT = resolve('.');
const PACKAGE_INFO = require(resolve(PACKAGE_ROOT, 'package.json'));

const rules = [
  {
    // Compile ES2015 using babel
    test: /(\.js|\.ts|\.tsx)$/,
    loader: 'babel-loader',
    include: /src/,
    options: {
      babelrc: false,
      presets: [
        [
          '@babel/preset-env',
          {
            targets: ['>0.2%', 'not ie 11', 'not dead', 'not chrome 49']
          }
        ],
        '@babel/preset-typescript'
      ]
    }
  }
];

const config = [
  {
    /**
     * Embeddable @deck.gl/jupyter-widget bundle
     *
     * Used in JupyterLab (whose entry point is at plugin.js) and Jupyter Notebook alike.
     *
     */
    entry: './src/index.js',
    resolve: {
      extensions: ['.ts', '.tsx', '.js', '.json']
    },
    output: {
      filename: 'bundle.js',
      path: resolve(__dirname, 'dist'),
      libraryTarget: 'umd'
    },
    devtool: 'source-map',
    module: {
      rules
    },
    plugins: [
      // Uncomment for bundle size debug
      // new (require('webpack-bundle-analyzer')).BundleAnalyzerPlugin()
      new webpack.DefinePlugin({
        __VERSION__: JSON.stringify(PACKAGE_INFO.version)
      })
    ]
  }
];

module.exports = config;
