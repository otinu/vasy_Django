const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    proxy: {
      '/products/': {
        target: process.env.VUE_APP_ROOT_API
      }
    }
  }
})
