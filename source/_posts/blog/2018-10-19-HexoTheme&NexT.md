---
layout: post
title: Hexo更换主题：NexT
date: 2018-10-19
categories: 工具
tags: 
- 工具
- Hexo
- 博客
description: Hexo更换主题：NexT
---

前面讲了如何使用[Hexo和GitPage搭建博客]()，开始本篇之前确保上篇的配置都已完成。如安装nodejs、Git环境、Hexo插件等。
再次说明一下：在 Hexo 中有两份主要的配置文件，其名称都是 `_config.yml`。 其中，一份位于站点根目录下，主要包含 Hexo 本身的配置；另一份位于主题目录下，这份配置由主题作者提供，主要用于配置主题相关的选项。
将前者称为 站点配置文件， 后者称为 主题配置文件。

## 一. Hexo主题

创建 Hexo 主题非常容易，您只要在 `themes` 文件夹内，新增一个任意名称的文件夹，并修改 `_config.yml`内的 `theme` 设定，即可切换主题。

Hexo提供了很多种[主题](https://hexo.io/themes/)，可挑选自己喜欢的。

主题文件说明：
（1）`_config.yml`：主题的配置文件。修改时会自动更新，无需重启服务器。
（2）languages：语言文件夹，不同语言文件
（3）layout：布局文件夹。用于存放主题的模板文件，决定了网站内容的呈现方式。
（3）script：脚本文件夹。在启动时，Hexo 会载入此文件夹内的 JavaScript 文件
（4）source：资源文件夹，存放 CSS、JavaScript、images 文件等资源。

## 二. NexT主题使用

[官方文档](http://theme-next.iissnan.com/getting-started.html)

### 1. 下载NexT主题

cmd打开终端，进入站点根目录（配置了Git环境变量）。或者直接右键点击`Git Bash Here`打开Git终端。
输入以下命令克隆主题到根目录下的`themes/next`文件夹中。
`git clone https://github.com/iissnan/hexo-theme-next themes/next`

### 2. 启用NexT主题

打开站点配置文件， 找到 theme 字段，并将其值更改为 next。

### 3. 运行验证

输入`hexo s`启动服务，浏览器访问 http://localhost:4000 ，可以看到主题已经变更。
可以输入`hexo g -d`生成静态文件部署到仓库中。

生成静态文件之前可使用`hexo clean`命令清除缓存

## 三. NexT主题配置文件说明

主题配置文件：`站点根目录/themes/next/_config.yml`中已经有具体的说明了，下面讲下常用的配置以及示例

### 1. 更换主题

NexT内置了三套主题，这里叫Scheme（用一送三很划算）：
修改主题配置文件的scheme字段：

```
Muse: 默认 Scheme，这是 NexT 最初的版本，黑白主调，大量留白
Mist: Muse 的紧凑版本，整洁有序的单栏外观
Pisces: 双栏 Scheme，小家碧玉似的清新
```

### 2. 设置菜单

修改主题配置文件的menu字段

格式为`菜单项名称（会匹配翻译）: 链接 || Font Awesome图标`

**注：旧版本`链接 ||`中间有空格，升级Hexo之后跳转404，链接多了个`%20`，表示空格，需要删除**

示例配置

```yml
menu:
  home: /|| home
  about: /about/|| user
  tags: /tags/|| tags
  categories: /categories/|| th
  archives: /archives/|| archive
  schedule: /schedule/|| calendar
  sitemap: /sitemap.xml|| sitemap
  #commonweal: /404/|| heartbeat
```
菜单项的名称并不直接用于界面上的展示。Hexo 在生成的时候将使用 这个名称查找对应的语言翻译，并提取显示文本。这些翻译文本放置在 NexT 主题目录下的 languages/{language}.yml （{language} 为你所使用的语言）。如简体中文配置文件：languages/zh-Hans.yml

修改翻译或者添加自定义的字段other：
```
menu:
  home: 首页
  archives: 归档
  categories: 分类
  tags: 标签
  about: 关于
  search: 搜索
  commonweal: 公益404
  other: 其他
```

### 3. 设置头像

修改avatar字段，设置头像链接地址，如：

| 完整的互联网URI | 放置到 `source/images/`路径下 |
| --- | --- |
| `avatar: http://example.com/avatar.png` | `avatar: /images/avatar.png`  |
文章中引用图片也是如此

## 四. Next升级

hexo升级之后Next会出现一些错误，原来Next版本为5.1.4，需要升级为V7+。

本文配置基于V5，升级之后部分配置需要相应修改。

[参考升级说明](https://github.com/theme-next/hexo-theme-next/blob/master/docs/zh-CN/UPDATE-FROM-5.1.X.md)

# 问题记录

hexo g生成报错

```shell
 ERROR Template render error: (e:\GitPageBlog\AkiyamaBlog\themes\next\layout\post.swig)
 Error: Unable to call `post["categories"]["toArray"]`, which is undefined or falsey
```

> 修改`themes/next/layout/_macro/post.swig`文件，去掉`post.categories.toArray()`和`post.tags.toArray()`中的`toArray()`

**注：回来补充，不能去掉toArray()，否则文章的分类和标签无法显示……估计和个人的版本有关系**

# 结束语

参考[Hexo官方文档](https://hexo.io/zh-cn/docs/)和[NexT官方文档](http://theme-next.iissnan.com/getting-started.html)下篇介绍NexT的一些进阶配置。