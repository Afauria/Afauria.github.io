---
layout: post
title: Hexo+GitPage搭建博客
date: 2018-10-17
categories: 工具
tags: 
- 工具
- Hexo
- 博客
description: Hexo+GitPage搭建博客
---

# Hexo简介

静态网页生成工具，可用于搭建博客。使用 [Markdown](http://daringfireball.net/projects/markdown/)（或其他渲染引擎）解析文章，有多种主题供选择。
[中文官方文档](https://hexo.io/zh-cn/docs/)

## 与Jekyll的区别？

在 Github Page 里用 Jekyll 其实是上传一个工程文件 ，Github 自动生成静态文件，而 Hexo 是先生成好文件再部署的。
此外，jekyll基于Ruby，Hexo基于Node

在 Hexo 中有两份主要的配置文件，其名称都是 _config.yml。其中，一份位于站点根目录下，主要包含 Hexo 本身的配置；另一份位于主题目录下，这份配置由主题作者提供，主要用于配置主题相关的选项。
将前者称为 站点配置文件， 后者称为 主题配置文件。

# Hexo使用

## 安装环境

[Node.js安装](https://nodejs.org/en/)
安装后打开cmd，输入`node -v`、`npm -v`检查是否安装成功（环境变量自动配置好了）
等于`node --version`、`npm --version`
[Git安装](https://git-scm.com/)
在电脑上右键出现Git Bash Here、Git GUI Here即表示安装成功。
若配置了环境变量，可输入`git --version`检查是否安装成功

注意：一般出于安全考虑，只有在Git Bash Here中才能进行Git的相关操作。如果需要在cmd命令行里调用Git，那么就要配置电脑的环境变量Path，或者在安装的时候选择use Git from the Windows Command Prompt。

## 安装hexo命令行工具

使用[npm](https://www.npmjs.com.cn/)进行安装：终端输入`npm install -g hexo-cli`
安装完成后可使用`hexo -v`或者`hexo --version`检查是否安装成功
注释：-g表示全局安装，不加则将模块下载到当前目录的node_modules中

如果下载较慢，可以设置[淘宝国内镜像](https://npm.taobao.org/)，又如下几种方式
（1）永久使用：

> npm config set registry https://registry.npm.taobao.org

（2）临时使用：
> npm --registry https://registry.npm.taobao.org

（3）可保存配置： 
> 编辑.npmrc文件，加入registry = https://registry.npm.taobao.org

（4）使用cnpm替代npm命令：
> npm install -g cnpm --registry=https://registry.npm.taobao.org
  cnpm install -g hexo-cli

配置成功后可通过`npm config get registry`命令验证是否成功

## 使用hexo

1. 终端进入一个空目录，输入`hexo init`，在该文件夹下初始化hexo工程，称为站点根目录
2. 输入`npm install`安装所需组件，即package.json中配置的库
3. 输入`hexo s`或`hexo server`启动服务
4. 默认端口为4000，访问 http://localhost:4000/ 即可，也可通过`hexo server -p 端口号`指定端口号
   出现下图就成功了，里面已经有一篇文章hello world了
   ![hexo成功图](/images/BuildBlog/hexo01.png)

# GitPage搭建

## Git账号注册

跳过，就和我们平常注册账号一样

## GitPage创建

创建一个新的仓库，仓库名称使用：用户名.github.io，如图
![git仓库创建](/images/BuildBlog/GitPage01.png)
创建完之后就可以通过 `https://moon-lights.github.io/` 来访问博客地址了

# 将GitPage和Hexo联系起来

## SSH配置

跳过，在[另一篇文章]()里介绍

## 修改站点配置文件

打开根目录的 `_config.yml` 文件，找到deploy，修改如下
```
deploy: 
​    type: git
​    repo: git@github.com:moon-lights/moon-lights.github.io.git
​    branch: master
```
repo地址如下图获取
![ssh地址拷贝](/images/BuildBlog/GitPage02.png)

## 安装上传到GitHub的插件

cmd打开终端，进入站点根目录，输入`npm install --save hexo-deployer-git`

注释：

| npm install X | npm install X --save | npm install X --save-dev |
| --- | ---| --- |
| 把X包安装到node_modules目录中 | 把X包安装到node_modules目录中 | 把X包安装到node_modules目录中|
| 不会修改package.json | 会在package.json的dependencies属性下添加X | 会在package.json的devDependencies属性下添加X |
| 运行npm install命令时，不会自动安装X | 运行npm install命令时，会自动安装X | 运行npm install命令时，会自动安装X |
|  | 之后运行npm install –production或者注明NODE_ENV变量值为production时，会自动安装X到node_modules目录中 | 之后运行npm install –production或者注明NODE_ENV变量值为production时，不会自动安装X到node_modules目录中 |

运行时需要用到的包使--save，否则使用--save-dev。

## 生成静态文件

使用`hexo generate`命令生成静态文件，简写为`hexo g`
此命令会在站点根目录生成public文件夹，即最终推到GitHub的文件。（与jekyll不同，jekyll是将工程推到Github，由GitPage生成静态文件，而这里是先生成静态文件再推到GitHub）

## 将静态文件推到GitHub上

使用`hexo deploy`命令推到GitHub上，简写为`hexo d`

上面两个命令可以合并为`hexo generate --deploy`或`hexo deploy --generate`
当然也可以简写为`hexo g -d`或`hexo d -g`

## 访问博客地址

访问刚才的博客地址，可以看到博客页面已经换成了Hexo的默认主题了，满满的成就感~~。

# 问题

## 两年后~，更新nodejs，hexo g -d发布失败。错误如下

![Hexo发布失败](/images/BuildBlog/HexoDeployFailed.png)

解决方案：

1. 更新hexo命令行工具：`npm install -g hexo-cli`
2. 更新`package.json`中依赖组件的版本

   1. 使用`npm update`更新所有依赖组件的版本
   2. 发现hexo从`^3.7.0`版本变到了`^3.9.0`，试了一下发布还是不行
   3. `package.json`中，版本号使用了^，只会更新小版本，不会更新大版本，因此还是版本号还是`3.x.x`
   4. 从[hexo工程模板](https://github.com/hexojs/hexo-starter)中拷贝最新的`package.json`，替换原来的版本
   5. 再执行`npm install`和`npm update`更新版本到`^5.3.0`，其他依赖也更新
3. 再执行`hexo g -d`，成功发布

![Hexo依赖版本图](/images/BuildBlog/HexoDependenciesVersion.png)

### 补充知识点

**[npm依赖包版本说明](../note/2021-4-12-NPM.md)**

## 升级之后菜单跳转404，url带%20

next menu配置：旧版本`链接 ||`中间有空格，升级Hexo之后需要删除空格

```yml
menu:
  home: /|| home
  about: /about/|| user
  tags: /tags/|| tags
  categories: /categories/|| th
  archives: /archives/|| archive
  schedule: /schedule/|| calendar
  sitemap: /sitemap.xml|| sitemap
```

## GitPage 构建失败

2021-5-16照常`hexo g -d`发布博客，结果收到GitHub错误邮件。

```
The page build failed for the `master` branch with the following error:

Unable to build page. Please try again later.

For information on troubleshooting Jekyll see:

  https://docs.github.com/articles/troubleshooting-jekyll-builds

If you have any questions you can submit a request at https://support.github.com/contact?repo_id=367865705&page_build_id=253625473
```

整了足足半天没解决，收了几十封错误邮件。尝试了很多方法无效：

1. 删除新上传的文件

2. 排查错误字符

3. 回退版本

4. `hexo clean`、并删除`.deploy_git`文件夹

5. 使用本地Jekyll编译运行正常

6. 删除了远程Git仓库，新建GitPage

7. 最后甚至准备转战Gitee发布，结果创建GitPage服务的时候提示服务不可用……

   ![GiteePages](/images/BuildBlog/GiteePages.png)

本地构建运行`hexo serve`正常，使用jekyll编译也正常，说明文章格式没有错误。就是GitPage构建的时候失败了。

最后实在没办法，于是暂时放着，静下来整理博客，反正本地运行也可以看。

结果到晚上随手发布了一下，居然成功了、成功了……

只能说GitHub太坑，估计下午哪里瓦特了

# 结束语

下篇介绍下Hexo的一些基本概念、配置和常用命令