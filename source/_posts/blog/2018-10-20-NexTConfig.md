---
layout: post
title: NexTConfig
date: 2018-10-20
categories: 工具
tags:
- 工具
- Hexo
- 博客
description: NexT高级配置
---

# NexT配置

## 1. 添加Readme.md文件

在Hexo目录下的source根目录下添加一个README.md文件，修改站点配置文件_config.yml，将skip_render参数的值设置为`skip_render: README.md`，跳过渲染该文件

## 2. 添加动态背景

修改主题配置文件 themes/next/_config.yml，不同动态背景，值为true应用：
```yml
canvas_nest: false
three_waves: false
canvas_lines: false
canvas_sphere: false

# Only fit scheme Pisces
canvas_ribbon:
  enable: false
  size: 300
  alpha: 0.6
  zIndex: -1
```

## 3. 修改文章底部的带#号的标签

修改模板/themes/next/layout/_macro/post.swig，搜索 rel=”tag”>#，将 # 换成`<i class="fa fa-tag"></i>`

## 4. 设置网站的图标Favicon

在[EasyIcon](http://www.easyicon.net/)中找一张（32*32）的ico图标,或者去别的网站下载或者制作，并将图标名称改为favicon.ico，然后把图标放在/themes/next/source/images里，并且修改主题配置文件：

```yml
favicon: 
	small: /images/favicon.ico
	medion: /images/favicon.ico
	#apple_touch_icon: /images/apple-touch-icon-next.png
	#safari_pinned_tab: /images/logo.svg
  	#android_manifest: /images/manifest.json
  	#ms_browserconfig: /images/browserconfig.xml
```

## 5. 添加搜索功能

NexT主题支持集成 Swiftype、 微搜索、Local Search 和 Algolia,Swiftype和Algolia都只有一段时间的试用期，可以采用Hexo提供的Local Search,原理是通过hexo-generator-search插件在本地生成一个search.xml文件，搜索的时候从这个文件中根据关键字检索出相应的链接。

安装插件

```shell
cd hexo
npm install hexo-generator-search --save
npm install hexo-generator-searchdb --save
```

修改站点配置文件：

>search:
>path: search.xml
>field: post
>format: html
>limit: 10000

修改NexT主题配置文件：

> local_search:
> ​	enable: true

## 6. 去掉NexT自带的文章目录序号

NexT会为文章自动加上目录，如果自己的文章里面已经加了序号，不需要自动加的话，则修改主题配置文件

![去掉文章目录序号](/images/BuildBlog/config01.png)

## 7. 生成分类、标签和关于页面

### 7.1. 标签

`hexo new page tags`：在`站点/source/`目录下会生成新的文件夹tags，在该文件夹下会有一个index.md文件，头信息修改如下，不需要加正文内容

```
title: tags
date: 2018-04-04
type: "tags"
comments: false
```
### 7.2. 分类

同理，将tags换成categories即可

### 7.3. 关于

同理，自行编辑文章内容，不需要加type

注：主题配置文件的menu需要将tags和categories的注释去掉

### 8. 修改样式

可以修改next主题下的layout和source中的布局和css样式，定制主题

# 参考文章

[Hexo博客Next主题个性设置集锦](http://www.mdslq.cn/archives/40609c5b.html#%E6%B7%BB%E5%8A%A0READMEmd%E6%96%87%E4%BB%B6)
[Hexo+NexT 主题配置备忘](http://blog.ynxiu.com/2016/hexo-next-theme-optimize.html)
[hexo博客添加搜索功能](https://blog.csdn.net/qq_40265501/article/details/80030627)