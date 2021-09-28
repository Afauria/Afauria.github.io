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

# 博客效果

![博客效果](/images/BuildBlog/next-effect.png)

# NexT配置

## 添加Readme.md文件

在Hexo目录下的source根目录下添加一个README.md文件，修改站点配置文件`_config.yml`，将skip_render参数的值设置为`skip_render: README.md`，跳过渲染该文件

## 添加动态背景

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

## 修改文章底部的带#号的标签

修改模板/themes/next/layout/_macro/post.swig，搜索 rel=”tag”>#，将 # 换成`<i class="fa fa-tag"></i>`

## 设置网站的图标Favicon

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

## 添加搜索功能

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

踩坑：启用搜索功能之后，使用`hexo serve`运行正常，点击按钮弹出搜索框，发布到GitPage，搜索框直接显示到搜索按钮旁边了。

> 打开浏览器开发者工具，找到html元素，查看本地和GitPage页面差异，发现两者`main.css`样式不同，GitPage上搜素框css样式丢失
>
> 解决：`hexo clean`清除之前的编译结果，`hexo g -d`重新部署

## 去掉NexT自带的文章目录序号

NexT会为文章自动加上目录序号，如果自己的文章里面已经加了序号，不需要自动加的话，则修改主题配置文件

![去掉文章目录序号](/images/BuildBlog/config01.png)

## 生成分类、标签和关于页面

### 标签

`hexo new page tags`：在`站点/source/`目录下会生成新的文件夹tags，在该文件夹下会有一个index.md文件，头信息修改如下，不需要加正文内容

```
title: tags
date: 2018-04-04
type: "tags"
comments: false
```
### 分类

同理，将tags换成categories即可

### 关于

同理，自行编辑文章内容，不需要加type

注：主题配置文件的menu需要将tags和categories的注释去掉

## 修改样式

可以修改next主题下的layout和source中的布局和css样式，定制主题

## 站点地图sitemap

为了让博文被google或百度检索，需要使用hexo的sitemap功能。

见[hexo博客站点sitemap的使用](https://eericzeng.github.io/2019/07/14/hexo%E5%8D%9A%E5%AE%A2%E7%AB%99%E7%82%B9sitemap%E7%9A%84%E4%BD%BF%E7%94%A8/)

## 配置Live2d卡通人物

1. 安装`npm install --save hexo-helper-live2d`，具体配置见官网说明[hexo-helper-live2d](https://github.com/EYHN/hexo-helper-live2d)
2. 安装动画model，如`npm install live2d-widget-model-koharu`，可以到[live2d-widget-models](https://github.com/xiazeyu/live2d-widget-models)挑选自己喜欢的model，效果见[hexo live2d插件 2.0 !](https://huaji8.top/post/live2d-plugin-2.0/)
3. 将下述配置拷贝到根目录`_config.yml`中，不能拷到主题配置中，否则不生效。

```yml
live2d:
  enable: true
  scriptFrom: local
  tagMode: false
  log: false
  model:
    use: live2d-widget-model-koharu
  display:
    position: right
    width: 250
    height: 500
  mobile:
    show: true
    scale: 0.5
  react:
    opacity: 0.7
```

## 右上角配置Fork me on GitHub入口

1. 到[GitHub Corners](http://tholman.com/github-corners/)或者[GitHub Ribbons](https://github.blog/2008-12-19-github-ribbons/)选择喜欢的图标，copy相应的代码
2. 将代码粘贴到`themes/next/layout/_layout.swig`文件中(放在`body`的内即可)
3. 修改`href`链接为想要跳转的地址，如GitHub主页

## 添加每日一言/今日诗词

1. 在**layout或者md文档**中添加下面代码。我是将今日诗词添加到了**关于页面**，将每日一言添加到了`/themes/next/layout/_partials/sidebar/site_overview.swig`中

```html
<!--今日诗词-->
<div class="poem-wrap">
  <div class="poem-border poem-left"></div>
  <div class="poem-border poem-right"></div>
  <div class="poem-title">念两句诗</div>
  <p id="poem">挑选中...</p>
	<p id="info"></p>
  <script src="https://sdk.jinrishici.com/v2/browser/jinrishici.js" charset="utf-8"></script>
  <script defer>
    jinrishici.load(function(result) {
      poem.innerHTML = result.data.content
      info.innerHTML = '【' + result.data.origin.dynasty + '】' + result.data.origin.author + '《' + result.data.origin.title + '》'
  });
  </script>
</div>
<!--每日一言-->
<div class="poem-side">
  <div id="hitokoto">loading...</div>
  <div id="hitokotofrom"></div>
  <script defer>
  fetch('https://v1.hitokoto.cn')
    .then(response => response.json())
    .then(data => {
       	hitokoto.innerHTML = data.hitokoto
    	if(data.from_who != null) {
      	  hitokotofrom.innerHTML ='——' + data.from_who + ' 《' + data.from + '》'
      	} else {
	  hitokotofrom.innerHTML ='——《' + data.from + '》' 
      }
    })
    .catch(console.error) 
</script>
</div>
```

2. 在`/themes/next/source/css`中添加下面的css样式，也可自行修改样式

```css
.poem-wrap {
    position: relative;
    width: 730px;
    max-width: 80%;
    border: 2px solid #797979;
    border-top: none;
    text-align: center;
    margin: 80px auto;
}
 
.poem-wrap .poem-title {
    font-family: 'Lato', "PingFang SC", "Microsoft YaHei", sans-serif;
    font-weight: bold;
    line-height: 1.5;
    margin: 20px 0 15px;
    font-size: 30px;
    position: relative;
    margin-top: -20px;
    display: inline-block;
    letter-spacing: 4px;
    color: #797979;
}

.poem-wrap p {
    width: 70%;
    margin: auto;
    line-height: 30px;
    color: #797979;
}
 
.poem-wrap p#poem {
    font-size: 25px;
}
 
.poem-wrap p#info {
    font-size: 15px;
    margin: 15px auto;
}

.poem-border {
    position: absolute;
    height: 2px;
    width: 27%;
    background-color: #797979;
}
 
.poem-right {
    right: 0;
}
 
.poem-left {
    left: 0;
}
 
@media (max-width: 685px) {
    .poem-border {
        width: 18%;
    }
}
 
@media (max-width: 500px) {
    .poem-wrap {
        margin-top: 60px;
        margin-bottom: 20px;
        border-top: 2px solid #797979;
    }
 
    .poem-wrap h1 {
        margin: 20px 6px;
    }
 
    .poem-border {
        display: none;
    }
}

.poem-side {
    transform: translateX(0px);
    color: #f5f5f5;
    bottom: 100px;
    position: absolute;
    width: 90%;
    margin: 0px 5%;
}
.poem-side div#hitokoto {
    font-size: 15px;
    text-align: left;
}
 
.poem-side div#hitokotofrom {
    font-size: 12px;
    text-align: right;
}
```



# 参考文章

1. [Hexo博客Next主题个性设置集锦](http://www.mdslq.cn/archives/40609c5b.html#%E6%B7%BB%E5%8A%A0READMEmd%E6%96%87%E4%BB%B6)
2. [Hexo+NexT 主题配置备忘](http://blog.ynxiu.com/2016/hexo-next-theme-optimize.html)
3. [hexo博客添加搜索功能](https://blog.csdn.net/qq_40265501/article/details/80030627)
4. [hexo(next)——每日一言、今日诗词](https://blog.csdn.net/qq_44036990/article/details/105088198)