var BundleTracker = require("webpack-bundle-tracker");

module.exports = {
    publicPath: process.env.NODE_ENV === "production" ? "/static/dist/" : "http://localhost:8080",
    outputDir: "../backend/static/dist",
    indexPath: "../../templates/base-vue.html",

    chainWebpack: config => {
        config.optimization
            .splitChunks(false)
            
            config
            .plugin("BundleTracker")
            .use(BundleTracker, [{filename: "./webpack-stats.json"}])
        
        config.output
            .filename("bundle.js")

        config.resolve.alias
            .set("__STATIC__", "../backend/static")
        config.devServer
            .public('http://localhost:8080')
            .host("localhost")
            .port("8080")
            .hotOnly(true)
            .watchOptions({poll: 1000})
            .disableHostCheck(true)
            .headers({"Access-Control-Allow-Origin": "*"})
            .writeToDisk(filePath => filePath.endsWith("index.html"))
    }
}