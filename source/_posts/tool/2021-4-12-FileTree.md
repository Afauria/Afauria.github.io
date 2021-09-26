---
layout: post
title: Markdown生成目录结构树
date: 2021-4-12
categories: 工具
tags: 
- 工具
- 笔记
description: 使用tree-node-cli工具Markdown生成目录结构树
keywords: [Markdown]
---

## 使用

1. 全局安装tree：`npm install tree-node-cli -g`
2. 查看帮助：`tree --help`，-L 确定目录层级，-I排除某个文件夹
3. 进入文件夹：示例输入`tree -L 4 -I node_modules`，效果如下

```
sample-shopping
├── index.html
├── package-lock.json
├── package.json
├── public
│   └── favicon.ico
├── README.md
├── src
│   ├── App.vue
│   ├── assets
│   │   └── logo.png
│   ├── components
│   │   └── HelloWorld.vue
│   ├── main.ts
│   └── shims-vue.d.ts
├── tsconfig.json
└── vite.config.ts
```

## 问题

1. Windows下系统自带了一个tree命令，直接输入tree会调用系统的命令

   > 可以使用treee命令，如上示例改为`treee -L 4 -I node_modules`
   >
   > npm帮我们创建了两个cmd文件

