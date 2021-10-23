const webpack = require('webpack');
const WebpackDevServer = require('webpack-dev-server');
const webpackConfig = require('./static\webpack.config.dev.js');

function runFunc(err) {
  if (err) {
    console.log(err);
  }
  console.log('Listening at http://127.0.0.1:8000/patients/video_call');
}

new WebpackDevServer(webpack(webpackConfig), {
  publicPath: '/static',
  hot: true,
  host: '0.0.0.0',
  open: 'chrome',
  after(app, server) {
  },
  headers: {
    // 'Cross-Origin-Embedder-Policy': 'unsafe-none',
    // 'Cross-Origin-Opener-Policy': 'unsafe-none',
  },
  openPage: 'http://127.0.0.1:8000/patients/video_call',
  disableHostCheck: true,
  historyApiFallback: true,
  proxy: [{
    path: 'http://127.0.0.1:8000/patients/meeting',
    target: 'http://127.0.0.1:9998/'
  }]
}).listen(9999, '0.0.0.0', runFunc);

new WebpackDevServer(webpack(webpackConfig), {
  publicPath: '/static',
  hot: true,
  host: '0.0.0.0',
  after(app, server) {
  },
  headers: {
    'Cross-Origin-Embedder-Policy': 'require-corp',
    'Cross-Origin-Opener-Policy': 'same-origin',
  },
  disableHostCheck: true,
  historyApiFallback: true,
}).listen(9998, '0.0.0.0', runFunc);
