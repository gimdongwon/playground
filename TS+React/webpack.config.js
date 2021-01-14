require("dotenv").config();
const path = require("path");
const HtmlWebpackPlugin = require("html-webpack-plugin"); // public/index.html을 build/로 옮겨주는 script 태그
const webpack = require("webpack");

const appBuild = path.resolve(__dirname, "build");
const appIndex = path.resolve(__dirname, "src", "index.tsx");
const appSrc = path.resolve(__dirname, "src");
const appHtml = path.resolve(__dirname, "public", "index.html");
const appPublic = path.resolve(__dirname, "public");

const shouldUseSourceMap = process.env.GENERATE_SOURCEMAP !== "false"; // webpack-dev-server이용시 sourcemap 에러 해결

function getClientEnv(nodeEnv) {
  return {
    "process.env": JSON.stringify(
      Object.keys(process.env).filter(key => /^REACT_APP/i.test(key)).reduce((
        env,
        key
      ) => {
        env[key] = process.env[key];
        return env;
      }, { Node_ENV: nodeEnv })
    )
  };
}

module.exports = webpackEnv => {
  const isEnvDevelopment = webpackEnv === "development";
  const isEnvProduction = webpackEnv === "production";
  const clientEnv = getClientEnv(webpackEnv);
  return {
    mode: webpackEnv, // development, production, none 설정가능
    entry: appIndex, // 번들 작업을 할 파일
    output: {
      // 번들 결과물이 저장될 경로를 지정
      path: appBuild, // directory 위치
      filename: isEnvProduction // 결과물 파일명
        ? "static/js/[name].[contenthash:8].js"
        : isEnvDevelopment && "static/js/bundle.js",
      chunkFilename: isEnvProduction
        ? "static/js/[name].[contenthash:8].chunk.js"
        : isEnvDevelopment && "static/js/[name].chunk.js",
      publicPath: "/"
    },

    module: {
      // loader사용시 webpack은 js와 json만 이해하기 때문에 처리 방식 설정을 해주어야 한다.
      rules: [
        {
          test: /\.(ts|tsx)$/,
          exclude: /node_modules/,
          use: [
            "cache-loader",
            {
              loader: "ts-loader",
              options: {
                transpileOnly: isEnvDevelopment ? true : false //
              }
            }
          ]
        },
        {
          loader: "file-loader",
          exclude: [/\.(js|mjs|jsx|ts|tsx)$/, /\.html$/, /\,json$/],
          options: {
            outputPath: "static/media", // 파일이 저장될 경로 지정
            name: "[name].[hash:8].[ext]", // 파일명 지정
            esModule: false // CommonJS를 사용하기 위한 옵션, 모듈연결/트리 쉐이킹이 필요한 경우
          }
        },
        {
          test: [/\.bmp$/, /\.gif$/, /\.jpe?g$/, /\.png$/],
          loader: "url-loader",
          options: {
            limit: 10000,
            outputPath: "static/media",
            name: "[name].[hash:8].[ext]"
          }
        }
        // # deprecated
        // {
        //   test: /\.(ts|tsx)$/,
        //   enforce: "pre",
        //   exclude: /node_modules/,
        //   loader: "eslint-loader",
        //   options: {
        //     cache: true,
        //     formatter: isEnvDevelopment
        //       ? "codeframe"
        //       : isEnvProduction && "stylish"
        //   },
        //   include: appSrc
        // }
      ]
    },
    resolve: {
      // 모듈을 해석하는 방식을 js 1순위에서 아래 순위로 변경
      extensions: [".tsx", ".ts", ".js"]
    },
    plugins: [
      new HtmlWebpackPlugin({ template: appHtml }),
      new webpack.DefinePlugin(clientEnv)
    ],
    devServer: {
      port: 3000,
      contentBase: appPublic,
      open: true,
      historyApiFallback: true,
      overlay: true,
      stats: "errors-warnings"
    },
    devtool: isEnvProduction
      ? shouldUseSourceMap ? "source-map" : false
      : isEnvDevelopment && "cheap-module-source-map"
  };
};
