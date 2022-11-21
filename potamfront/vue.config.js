module.exports = {
    publicPath: process.env.NODE_ENV === 'production'
      ? '/potamapp/'
      : '/',
    devServer: {
        proxy: 'https://europe-west1-potamapp.cloudfunctions.net/function-1'
    }
  }