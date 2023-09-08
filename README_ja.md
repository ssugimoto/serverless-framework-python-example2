# serverless-framework-python-example

[In English](README.md)

- このリポジトリでは、[serverless-framework](https://www.serverless.com/) でのAWS Lambda の Python を利用した場合のローカル開発環境を手助けするサンプルです。

- Qiitaの記事にも記載しています。https://qiita.com/ssugimoto/items/511e352709bbf8483fb8

# Requirement

* docker engine 
* docker compose V2

Docker Desktopを利用すると、上記２つとも利用可能です

* VS Code
* VS Code extension
    - それぞれの関係がよくわからないのですが、ひとまず３つ入れておけばなんとかなる
    - [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
    - [Remote explorer](https://marketplace.visualstudio.com/items?itemName=ms-vscode.remote-explorer) 
    - [Remote Development](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack)


# Installation

## 1. git clone OR GitHubリポジトリから Download ZIP 

```
│  .env
│  .gitignore
│  compose.yml
│  README.md
├─app
└─serverless
        Dockerfile
```

## 2. env

AWSクラウドで利用する IAMユーザー等の認証情報が必要です。指定した認証情報でAWSに対してServerless FrameworkがCloudformationを実行します。
```
AWS_ACCESS_KEY_ID=XXXXXXXXXXXXXXX
AWS_SECRET_ACCESS_KEY=YYYYYYYYYYYYYYY
```

## 3. docker コマンド実行

- cd compose.ymlファイルのあるディレクトリ
- docker compose up 

```sh
cd xxxx
docker compose up -d
```
 
# Usage
 
実行方法と基本的な操作の流れ


1. docker コンテナ起動 
```bash
git clone https://github.com/ssugimoto/serverless-framework-nestjs-example.git
cd serverless-framework-nestjs-example
python docker compose up -d
```

2. VS Codeでdocker composeで起動したコンテナの中に入る
3. VS Codeのターミナルで node, npm, sls のPATHを確認する

```sh
# node -v
v18.17.1

# npm -v
9.6.7

# sls -v
Framework Core: 3.34.0
Plugin: 6.2.3
SDK: 4.3.2

# python --version
Python 3.11.5
```

4.  AWS Lambdaのpythonコードのテンプレートからコード生成

- コンテナの中でコマンド実行
```
cd /app/app
serverless create --template aws-python3 --name lambda-sample --path ./lambda-sample
```

5. AWS Lambdaとして AWSリソース作成とデプロイ


```
# /app/app/lambda-sample
# sls deploy
```

# Note

 
# Author

* ssugimoto
 
# License
MIT
