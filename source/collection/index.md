---
layout: post
title: 站点和工具收藏
date: 2021-9-24
description: 整理和收藏好用的站点、在线工具、资源下载、别人家的博客等
---
<style>
  .item-list {
  }
  .item {
    margin: 0 12px 12px 0;
    border: 1px solid #ccc;
	background: #fbfbfb;
    position: static;
    border-radius: 4px;
    transition: box-shadow 0.3s ease-in-out;
    padding: 10px 15px 10px 8px;
    color: #444;
  }
  .item:hover {
    box-shadow: 0 3px 8px 0 rgb(0 0 0 / 20%);
  }
  .item-title {
    font-size: 20px;
    font-weight: bold;
  }
  .item-desc {
    border-top: 1px solid #ddd;
    margin-top: 8px;
    padding: 10px 0;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
  .item-url {
    color: #999;
  }
  .item-list tbody {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    justify-content: space-evenly;
    border: none;
    padding-left: 8px;
  }
  .item-list tbody tr {
    margin: 0 12px 12px 0;
    background: #fbfbfb;
    position: static;
    border-radius: 4px;
    transition: box-shadow 0.3s ease-in-out;
    padding: 8px 14px;
    color: #444;
    position: relative;
  }
  .item-list td,
  .item-list tr {
    display: block;
    border: none;
  }
  .item-list thead,
  .item-list th {
    display: none;
  }
  .item-list tr:hover {
    box-shadow: 0 3px 8px 0 rgb(0 0 0 / 20%);
  }
  .item-list tbody tr td:first-child {
    font-size: 16px;
    font-weight: bold;
    padding: 0px 8px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
  .item-list tbody tr td:nth-child(2) {
    font-size: 14px;
    color: #999;
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 3;
    word-break: break-all;
    overflow: hidden;
    text-overflow: ellipsis;
    padding: 0px 8px;
  }
  .item-list tbody tr td:last-child {
    color: #999;
    padding: 0px 8px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    display: none;
  }
  .item-list td a {
    text-decoration: none;
    border: none;
  }
</style>

# 前言

~~整理了多个在线工具和站点，顺便清理了一下自己的Chrome书签。有很多功能重复的，应该取其精华，但由于本人有收藏癖，怕哪天找不到了，因此都列举了出来。有空再整理出最好用的工具集合。~~

本来是准备放一些实用工具链接，方便查找，结果书签越整理越多，并且会有很多重复的，不太好分类的。添加了知名站点、实用工具、博客、学习网站、资源网站等。

有些网站可能过期了或者被墙了，不确定会不会恢复。

有过期或者补充的网站可以给我提issue或者评论。

2022-11-05日：部分从轮子哥的[AndriodIndex](https://github.com/getActivity/AndroidIndex)中补充而来

<div class="item-list">

# 知名站点

| 标题                                                         | 描述                                                         | 地址                                              |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------- |
| <a href='https://tool.lu/'>在线工具</a>                      | 丰富的在线工具集合                                           | https://tool.lu/                                  |
| [程序员在线工具](http://www.ofmonkey.com/m/funs)             | 程序员在线工具                                               | http://www.ofmonkey.com/m/funs                    |
| [FeHelper](https://www.baidufe.com/fehelper/index/index.html) | 前端开发助手，包含多种在线工具，另外提供浏览器插件使用       | https://www.baidufe.com/fehelper/index/index.html |
| [土拨鼠](https://www.tuboshu.mobi/)                          | 多款在线工具，软件推荐，资源推荐                             |                                                   |
| [Android社区](https://www.androidos.net.cn/)                 | Andorid源码、资讯、技术文章、代码片段等                      |                                                   |
| [AndroidDevTools](https://www.androiddevtools.cn/)           | 收集整理Android开发所需的Android SDK、开发中用到的工具、Android开发教程、Android设计规范，免费的设计素材等 |                                                   |
| [Flutter社区](https://www.flutterchina.net.cn/)              | Flutter和Dart开发指南、文档、电子书、资讯等                  |                                                   |
| [Flutter中文网](https://flutterchina.club/)                  | 《Flutter实战》作者Wendux建立，同步翻译Flutter官网文档，开源Flutter项目等 |                                                   |
| [WanAndroid](https://www.wanandroid.com/tools)               | WanAndroid在线工具箱、博客文章、开源项目、开发API接口等      | https://www.wanandroid.com/tools                  |
| [干货集中营](https://gank.io/)                               | 技术文章、开发API接口、包含大量妹子图片                      |                                                   |
| [泡在网上的日子](http://www.jcodecraeer.com/)                | Android、Web开发技术文章，资讯，Android开发网址导航          |                                                   |
| [helloworld](https://www.helloworld.net/)                    | 专业开发者社区。学习交流技术的平台                           | https://www.helloworld.net/                       |
| <a href='http://cn.hipenpal.com/tool/index.php'>国际笔友中心</a> | 中、英、日、韩工具、ASCII、Unicode等编码转换工具             | http://cn.hipenpal.com/tool/index.php             |
| [PatOrJK站点](http://patorjk.com)                            | Web、App工具和博客                                           | http://patorjk.com                                |
| [BeJSON](https://www.bejson.com/)                            | 在线json格式化校验、编解码、加密、模拟请求等工具             | https://www.bejson.com/                           |
| [开源中国OSChina](https://www.oschina.net/)                  | OSC(Open Source China)，国内著名开源社区。Gitee的母公司，包括开源软件库、博客资讯、实用工具等。为IT开发者提供发现、使用、并交流开源技术的平台。 |                                                   |
| [PostJson](http://coolaf.com/)                               | http请求模拟，json格式化、编解码、加密工具                   | http://coolaf.com/                                |
| [制图网](http://www.makepic.net/)                            | 图片转换、处理、生成图片                                     | http://www.makepic.net/                           |
| [站长之家](http://tool.chinaz.com/)                          | 在线工具、源码下载，图片、PPT素材等                          | http://tool.chinaz.com/                           |
| [神奇海螺试验场](https://lab.magiconch.com/)                 | 网络缩写释义、图片风格化、切九图、手办筛选等                 | https://lab.magiconch.com/                        |
| [AppsCyborg](https://appscyborg.com/)                        | 网页图片提取、图像处理、文件转换等                           | https://appscyborg.com/                           |
| [RapitTables](https://www.rapidtables.com/)                  | 在线工具集合：计算机、单位换算、Html开发等                   | https://www.rapidtables.com/                      |
| [推酷](https://www.tuicool.com/)                             | （@Deprecated）专注于IT领域的信息挖掘和聚合推荐，内容涵盖科技、技术、设计、营销等方面。 |                                                   |

# 在线工具

## 工具箱合集

太多同质化产品了，建议挑一个全面的站点收藏。希望有一天我也能建一个工具箱，自己的总是最好的

| 标题                                                | 描述                                             | 地址                           |
| --------------------------------------------------- | ------------------------------------------------ | ------------------------------ |
| [BeJSON](https://www.bejson.com/)                   | 在线json格式化校验、编解码、加密、模拟请求等工具 | https://www.bejson.com/        |
| [Jsons.cn](http://www.jsons.cn/websocket/)          | 在线json校验、http、websocket连接测试等          | http://www.jsons.cn/websocket/ |
| [json.cn](https://www.json.cn/)                     | 在线json解析工具                                 |                                |
| [菜鸟工具](https://c.runoob.com/)                   |                                                  |                                |
| [草料二维码](https://cli.im/)                       | 二维码生成工具                                   |                                |
| [The X在线工具箱](https://the-x.cn/)                | 在线工具合集                                     |                                |
| [txttool](http://www.txttool.com/)                  | 在线文本工具合集                                 |                                |
| [试试吧](https://try8.cn/tool/time/convert)         |                                                  |                                |
| [metools工具箱](http://www.metools.info/)           |                                                  |                                |
| [fly63工具箱](https://www.fly63.com/tool/home.html) |                                                  |                                |
| [脚本之家在线工具](http://tools.jb51.net/)          |                                                  |                                |
| [OSChina实用代码工具](https://tool.oschina.net/)    |                                                  |                                |

## 实用工具

| 标题                                                         | 描述                                         | 地址                                                  |
| ------------------------------------------------------------ | -------------------------------------------- | ----------------------------------------------------- |
| [YOPmail](https://yopmail.net/zh/)                           | 提供临时邮箱服务                             | https://yopmail.net/zh/                               |
| [PlantUML](https://plantuml.com/zh/)                         | UML绘制生成，例子学习                        | https://plantuml.com/zh/                              |
| [图标工厂](https://icon.wuruihong.com/)                      | 一键生成iOS、Android各分辨率应用图标、启动图 | https://icon.wuruihong.com/                           |
| [JSON to Dart](https://javiercbk.github.io/json_to_dart/)    | JSON数据转Dart类，Flutter开发用              | https://javiercbk.github.io/json_to_dart/             |
| [icomoon](https://icomoon.io/app/#/select)                   | 图标资源下载，生成字体图标                   | https://icomoon.io/app/#/select                       |
| [阿里iconfont](https://www.iconfont.cn/collections/index)    | 图标资源下载，生成字体图标                   | https://www.iconfont.cn/collections/index             |
| [ColorConverter](https://www.rapidtables.com/)               | 在线颜色转换                                 | https://www.rapidtables.com/convert/color/index.html  |
| [Regex101](https://regex101.com/)                            | 正则表达式运行                               | https://regex101.com/                                 |
| [websocket-test](http://www.websocket-test.com/)             | 在线WebSocket测试服务器                      | http://www.websocket-test.com/                        |
| [Mermaid Live Editor](https://mermaid-js.github.io/mermaid-live-editor/edit) | 在线mermaid编写、渲染                        | https://mermaid-js.github.io/mermaid-live-editor/edit |
| [Markmap](https://markmap.js.org/)                           | Markdown生成思维导图                         |                                                       |
| [Carbon](https://carbon.now.sh/)                             | 源代码生成好看的图片                         |                                                       |

## 文件格式转换

| 标题                                                         | 描述                                                | 地址                             |
| ------------------------------------------------------------ | --------------------------------------------------- | -------------------------------- |
| [OfficeConvert](https://cn.office-converter.com/)            | 在线文件格式转换                                    | https://cn.office-converter.com/ |
| [OnlineConvert](https://www.online-convert.com/)             | 在线文件格式转换                                    | https://www.online-convert.com/  |
| [CloudConvert](https://cloudconvert.com/)                    | 在线文件格式转换：图像、音视频、文档，并提供API接口 | https://cloudconvert.com/        |
| [Android SVG to Vector Drawable](http://inloop.github.io/svg2android/) |                                                     |                                  |
| [JPG、PNG转SVG](https://www.pngtosvg.com/)                   |                                                     |                                  |
| [迅捷PDF转换器](https://app.xunjiepdf.com/ocr/)              | 从图片中提取文字，图片、PDF、Word、音视频格式转换   |                                  |

## 图片处理

| 标题                                      | 描述                 | 地址                          |
| ----------------------------------------- | -------------------- | ----------------------------- |
| [在线PS工具](https://www.uupoop.com/#/)   | 在线PS工具，图片处理 | https://www.uupoop.com/#/     |
| [美图秀秀图片处理](https://pc.meitu.com/) | 美图秀秀在线图片处理 | https://pc.meitu.com/         |
| [SooGif](https://www.soogif.com/crop)     | gif图处理、压缩      | https://www.soogif.com/crop   |
| [PicDiet](https://www.picdiet.com/zh-cn)  | 在线图片压缩         | https://www.picdiet.com/zh-cn |
| [TinyPng](https://tinypng.com/)           | 在线图片压缩         |                               |
| [PngQuant](https://pngquant.org/)         | 在线图片压缩         |                               |

## 数学

| 标题                                           | 描述                                                  | 地址                               |
| ---------------------------------------------- | ----------------------------------------------------- | ---------------------------------- |
| [MyScript](https://webdemo.myscript.com/)      | 手写公式、算法、图表，生成函数曲线                    | https://webdemo.myscript.com/      |
| [Mathcha](https://www.mathcha.io/editor)       | 数学表达式编辑                                        | https://www.mathcha.io/editor      |
| [Desmos](https://www.desmos.com/?lang=zh-CN)   | 数学工具：函数曲线、几何工具、计算器等，并提供API接口 | https://www.desmos.com/?lang=zh-CN |
| [CodeCogs](https://www.codecogs.com/index.php) | 在线公式编辑器，LaTex生成等                           | https://www.codecogs.com/index.php |

## 其他

| 标题                                                         | 描述                              | 地址                                    |
| ------------------------------------------------------------ | --------------------------------- | --------------------------------------- |
| [SVGOMG](https://jakearchibald.github.io/svgomg/)            | SVG在线预览，格式化，压缩等       | https://jakearchibald.github.io/svgomg/ |
| [字魂-字体转换器](https://izihun.com/art-edit/)              | 字体转换器，字体下载等            | https://izihun.com/art-edit/            |
| [ASCIIFlow](https://asciiflow.com/#/)                        | 绘图生成ASCII字符                 | https://asciiflow.com/#/                |
| [char-dust](https://www.yunyoujun.cn/char-dust/)             | 将图片变成字符画（又称ASCII艺术） | https://www.yunyoujun.cn/char-dust/     |
| [ClipConvert](http://www.clipconverter.cc/)                  | Youtube视频下载                   | http://www.clipconverter.cc/            |
| [GIPHY](https://giphy.com/)                                  | 上传gif生成链接，下载搜索gif资源  | https://giphy.com/                      |
| [在线文本比较工具](https://www.qianbo.com.cn/Tool/Text-Difference/) |                                   |                                         |
| [eletypes](https://www.eletypes.com/)                        | 练习打字速度的网站                |                                         |

# API接口数据

| 标题                                                      | 描述                                                         | 地址 |
| --------------------------------------------------------- | ------------------------------------------------------------ | ---- |
| [JsonPlaceholder](http://jsonplaceholder.typicode.com/)   | 提供测试用JSON假数据，包含文章、评论、相册、待办列表、用户信息等假数据 |      |
| [Random User Generator](https://randomuser.me/)           | 生成随机用户信息假数据，支持条件查询，支持JSON、CSV、XML等数据格式 |      |
| [爱思路API接口](https://api.asilu.com/)                   | 汇集多种数据接口，如抖音、开源中国、网易云音乐、有道翻译、天气查询等。支持在线请求查看结果 |      |
| [WanAndroid API](https://www.wanandroid.com/blog/show/2)  | WanAndorid开放接口。包含技术文章、分类、开源项目等接口数据   |      |
| [干货集中营-拿着Api去玩耍](https://gank.io/api)           | 提供文章、干货、妹子图片接口                                 |      |
| [Hitokoto每日一言](https://hitokoto.cn/#)                 | 动漫也好、小说也好、网络也好，不论在哪里，我们总会看到有那么一两个句子能穿透你的心。我们把这些句子汇聚起来，形成一言网络，以传递更多的感动。 |      |
| [今日诗词](https://www.jinrishici.com/)                   | 今日诗词 API 是一个可以返回一句古诗词名句的接口。它可以通过图片和 JSON 格式调用。今日诗词 API 根据不同地点、时间、节日、季节、天气、景观、城市进行智能推荐。 |      |
| [易源接口](https://www.showapi.com/)                      | 为用户提供基于大数据的API服务                                |      |
| [聚合数据](https://www.juhe.cn/docs)                      | 一家基于API技术的综合性数据处理服务商                        |      |
| [Public APIs](https://github.com/public-apis/public-apis) | 各种免费API接口集合                                          |      |
| [Free API](https://www.free-api.com/)                     | 各种免费API接口和文档集合，支持在线请求功能                  |      |

[知乎回答-想写个 App 练手，有什么有趣的 API 接口推荐吗？](https://www.zhihu.com/question/39479153)

[知乎回答-有哪些好玩的免费的API接口?](https://www.zhihu.com/question/32225726/answer/785525942)

# 别人家的博客

## 学习博客

关注下大佬们的博客，相形见绌。

| 标题                                                         | 描述                                          | 地址 |
| ------------------------------------------------------------ | --------------------------------------------- | ---- |
| [鸿洋的CSDN博客](https://blog.csdn.net/lmj623565791/?type=blog) | Android开发技术干货                           |      |
| [郭霖的CSDN博客](https://blog.csdn.net/guolin_blog)          | 《第一行代码》作者                            |      |
| [养生达人不熬夜](http://www.reo-lin.top/)                    | Android和Java知识点和源码学习                 |      |
| [BATcoder - 刘望舒](http://liuwangshu.cn/)                   | Android进阶三部曲的作者                       |      |
| [Gityuan](http://gityuan.com/)                               | Android开发大佬，Android源码分析              |      |
| [ConstXiong记录编程实践](https://www.javanav.com/interview/93b0069472fd479393006c0e73043fc4.html) | Java开发工程师，整理了一些在线题目            |      |
| [沉默王二](https://www.itwanger.com/)                        | Java工程师，知名博主。Java 程序员进阶之路专栏 |      |
| [一叶知秋](http://qiushao.net/)                              | Android系统开发                               |      |
| [技术小黑屋](https://droidyue.com/)                          | Android、Java开发                             |      |
| [Android开发技术周报](https://www.androidweekly.cn/)         | Android 开发技术周报                          |      |
| [彭旭锐的简书博客](https://www.jianshu.com/u/d9761b0d1618)、[彭旭锐的掘金博客](https://juejin.cn/user/1063982987230392/posts) | Java和Android技术文章                         |      |
| [廖雪峰的官方网站](https://www.liaoxuefeng.com/)             | 包含Java、Python、JS、Git教程等               |      |
| [阮一峰的个人网站](https://www.ruanyifeng.com/)              | 大量的读书、学习、分享                        |      |
| [红橙 Darren](https://www.jianshu.com/u/35083fcb7747)        |                                               |      |
| [weishu](https://weishu.me/)                                 | 骨灰级Android开发                             |      |
| [刘一刀](https://juejin.cn/user/272334612601559/posts)       |                                               |      |
| [Flywith24](https://juejin.cn/user/219558054476792/posts)    |                                               |      |
| [胡飞洋](https://juejin.cn/user/2295436011910894/posts)      |                                               |      |
| [蓝师傅](https://juejin.cn/user/3298190612500696/posts)      |                                               |      |
| [业志陈](https://juejin.cn/user/923245496518439/posts)       |                                               |      |
| [路遥在路上](https://juejin.cn/user/2137106333043070/posts)  |                                               |      |
| [开发者如是说](https://juejin.cn/user/3685218704691469/posts) |                                               |      |
| [依然范特稀西](https://juejin.cn/user/1204720443862887/posts) | 公众号《技术最Top》                           |      |
| [JessYan](https://juejin.cn/user/976022014539326/posts)      | MVPArms作者                                   |      |
| [恋猫de小郭](https://juejin.cn/user/817692379985752/posts)   | 《Flutter开发实战详解》作者                   |      |
| [拉丁吴](https://juejin.cn/user/976022014531134/posts)       |                                               |      |
| [天之界线2010](https://juejin.cn/user/4336129589120302/posts) |                                               |      |
| [究极逮虾户](https://juejin.cn/user/4265760848090664/posts)  |                                               |      |
| [BaronTalk](https://juejin.cn/user/923245496502232/posts)    |                                               |      |
| [bennyhuo](https://juejin.cn/user/1187128286120631/posts)    | 深入理解Kotlin协程作者                        |      |
| [yechaoa](https://juejin.cn/user/659362706101735/posts)      |                                               |      |
| [Mlx](https://juejin.cn/user/1345457961046055/posts)         |                                               |      |
| [貌似许亚军](https://juejin.cn/user/1433418891789149/posts)  |                                               |      |
| [D_clock爱吃葱花](https://juejin.cn/user/1926000099735373/posts) |                                               |      |
| [NanBox](https://juejin.cn/user/3175045309414935/posts)      |                                               |      |
| [朱涛的自习室](https://juejin.cn/user/2119514149637032/posts) |                                               |      |
| [Blankj](https://juejin.cn/user/1978776659167981/posts)      |                                               |      |
| [Carson 带你学 Android](https://juejin.cn/user/2524134385917293/posts) |                                               |      |
| [程序员DHL](https://juejin.cn/user/2594503168898744/posts)   |                                               |      |
| [秦子帅](https://juejin.cn/user/4089838984240680/posts)      |                                               |      |
| [吴小龙同學](https://juejin.cn/user/3614849960247351/posts)  |                                               |      |
| [nanchen2251](https://juejin.cn/user/4230576473377751/posts) |                                               |      |
| [唐子玄](https://juejin.cn/user/3087084378135613/posts)      |                                               |      |
| [北斗星_And](https://juejin.cn/user/3966693684811662/posts)  |                                               |      |
| [却把清梅嗅](https://juejin.cn/user/1503787635450584/posts)  |                                               |      |
| [KunMinX](https://juejin.cn/user/1081575170900958/posts)     |                                               |      |
| [全世界_Coder](https://juejin.cn/user/1890815727121005/posts) |                                               |      |
| [xuyisheng](https://juejin.cn/user/43636194286093/posts)     | 《Android群英传》                             |      |
| [codelang](https://juejin.cn/user/184373682638727/posts)     |                                               |      |
| [Android轮子哥](https://www.jianshu.com/u/f7bb67d86765)      |                                               |      |
| [床长人工智能教程](https://www.captainbed.net/)              | 人工智能科普教程                              |      |

## 有趣的、好看的博客

收藏别人家好看、有趣的博客主题。借鉴博客设计

| 标题                                              | 描述                                                | 地址 |
| ------------------------------------------------- | --------------------------------------------------- | ---- |
| [GitHub博客](https://github.blog/)                | GitHub博客。包含GitHub的发布信息、介绍、开发者API等 |      |
| [云游君的小站](https://www.yunyoujun.cn/)         | 有趣的博客！前端开发、二次元大佬                    |      |
| [卜卜口](https://mouto.org/)                      | 有趣的博客！前端开发，二次元大佬、小工具            |      |
| [麋鹿鲁哟](https://www.cnblogs.com/miluluyo/)     | 好看的博客，前端开发                                |      |
| [EYHN](https://huaji8.top/)                       | 前端开发、二次元大佬、hexo博客、live2d卡通人物      |      |
| [Airing的小屋](https://me.ursb.me/)               | 好看的博客，腾讯前端工程师，Flutter学习             |      |
| [TIMEGG](https://timegg.top/)                     | 有趣的博客，游戏开发者，分享生活、想法              |      |
| [JEROEN MOLS](https://jeroenmols.com/)            | Google开发专家，一位比利时大叔的博客                |      |
| [月半兄的小站](https://yueban.github.io/)         | Android开发                                         |      |
| [bugstack虫洞栈](https://bugstack.cn/)            | 后端开发                                            |      |
| [默默的点滴](https://www.mobibrw.com/)            | 数量庞大，感觉啥都会                                |      |
| [屈定's Blog](https://mrdear.cn/)                 | 好看的博客，Java后端开发                            |      |
| [毛若昕的个人主页](https://maorx.cn/)             | 个人作品：营销号文案生成器                          |      |
| [闫肃的博客](http://yansu.org/index.html)         | 环境部署，后端开发                                  |      |
| [Aengus Blog](https://www.aengus.top/)            | Android开发                                         |      |
| [Brucezz's Corner](https://brucezz.itscoder.com/) | Android开发                                         |      |
| [银河小徐](https://blog.hasaik.com/)              | Java工程师                                          |      |
| [简页](https://jianpage.com/)                     | 好看的博客，后端开发                                |      |
| [HJiahu's Blog](https://yearn.xyz/)               | 简洁的博客                                          |      |
| [AnnatarHe](https://annatarhe.github.io/)         | 简洁的博客，前端相关                                |      |
| [Pseudoyu](https://www.pseudoyu.com/zh/)          | 区块链开发工程师                                    |      |
| [Airing的小屋](https://me.ursb.me/)               | 前端工程师                                          |      |
| [酷壳](https://coolshell.cn/)                     | 陈皓的个人博客，“左耳朵耗子”                        |      |

## 朋友

| 标题                                                 | 描述                              | 地址 |
| ---------------------------------------------------- | --------------------------------- | ---- |
| [LinJW](https://blog.islinjw.cn/)                    | 我毕业入职公司的导师，技术广博    |      |
| [Shmily](https://zhiqixu.github.io/)                 | 大学老师，似乎很久不更新          |      |
| [王鹏的CSDN博客](https://blog.csdn.net/qq_28587263)  | 实验室一位学长，Java后端工程师    |      |
| [熔岩的CSDN博客](https://blog.csdn.net/rongyan97718) | 实验室的同学，Android开发的领路人 |      |
| [吃猫猫的鱼](https://cmmdy.github.io/)               | 大学同学，Android同行             |      |
| [自学路漫漫](https://blog.fxcdev.com/)               | 前同事，已经从打工人晋升为老板了  |      |

# 学习网站

| 标题                                                         | 描述                                                 | 地址                                       |
| ------------------------------------------------------------ | ---------------------------------------------------- | ------------------------------------------ |
| [菜鸟教程](https://www.runoob.com/)                          | 各种语言基础技术教程，手册                           |                                            |
| [w3school](https://www.w3school.com.cn/)                     | 全面的Web开发者教程和资源                            |                                            |
| [牛客](https://www.nowcoder.com/)                            | 刷题                                                 |                                            |
| [力扣](https://leetcode.cn/)                                 | 刷题                                                 |                                            |
| [书栈网](https://www.bookstack.cn/)                          | 开源书籍和文档站点                                   |                                            |
| [Java & Android面试文档](https://www.kancloud.cn/smartsean/android/1106138) | Java&Android面试文档，部署到看云                     |                                            |
| [Java工程师成神之路](https://hollischuang.github.io/toBeTopJavaer) | 顾名思义。作者Hollis，阿里巴巴技术专家               |                                            |
| [Android面试](https://dongchuan.gitbooks.io/android-interview/content/) | Android面试知识点，部署到Gitbook                     |                                            |
| [计算机学习笔记](https://github.com/CyC2018/CS-Notes)        | 包含算法、操作系统、网络、数据库、Java、工具等笔记   |                                            |
| [免费的编程中文书籍索引](https://github.com/justjavac/free-programming-books-zh_CN) | 免费的编程中文书籍索引                               |                                            |
| [阮一峰的网络日志](https://www.ruanyifeng.com/blog/)         | 书籍翻译、技术文章，周刊                             |                                            |
| [廖雪峰的官方网站](https://www.liaoxuefeng.com/)             | Git、Python、SQL教程等                               |                                            |
| [Java Guide](https://snailclimb.gitee.io/javaguide/#/)       | Java学习+面试指南                                    |                                            |
| [LearningGit](https://learngitbranching.js.org/?locale=zh_CN) | Git学习，在线输入Git，图解预览分支信息               |                                            |
| [小林coding](https://xiaolincoding.com/)                     | 图解网络、操作系统、计算机基础。公众号大佬、画图大佬 |                                            |
| [Visualgo](https://visualgo.net/zh)                          | 数据结构和算法动态可视化学习、练习                   | https://visualgo.net/zh                    |
| [Awesome Android](https://snowdream86.gitbooks.io/awesome-android/content/) | 精选的Android库和资源                                | https://github.com/JStumpp/awesome-android |
| [Android开源库收集整理](https://github.com/XXApple/AndroidLibs) |                                                      |                                            |
| [Android校招面试指南](https://lrh1993.gitbooks.io/android_interview_guide/content/) |                                                      |                                            |
| [Android知识体系](https://github.com/feelschaotic/AndroidKnowledgeSystem) |                                                      |                                            |
| [AndroidUI开发库](https://github.com/wasabeef/awesome-android-ui) |                                                      |                                            |
| [Java程序员进阶之路](https://itwanger.gitee.io/tobebetterjavaer/#/) | 作者沉默王二                                         |                                            |
| [C语言中文网-设计模式](http://c.biancheng.net/view/1317.html) | 设计模式干货                                         |                                            |
| [掘金酱](https://e.juejin.cn/)                               | 精选文章和项目                                       |                                            |
| [泡网](https://paonet.com/)                                  | Android和Web开发资料                                 |                                            |
| [前端乱炖](https://www.html-js.com/)                         |                                                      |                                            |
| [CodingGame](https://www.codingame.com/)                     | 以玩游戏形式在线编程，页面精美                       |                                            |
| [慕课网](https://www.imooc.com/)                             | 在线课程                                             |                                            |
| [简单教程](https://www.twle.cn/)                             | IT入门教程                                           |                                            |
| [开发者头条](https://toutiao.io/)                            |                                                      |                                            |
| [GitChat](https://gitbook.cn/)                               |                                                      |                                            |
| [Web前端导航](http://www.alloyteam.com/nav/)                 | 腾讯AlloyTeam建设                                    |                                            |

# 资源下载

## 产品原型和UI设计资源素材

[设计师必逛！44 个找灵感网站推荐](https://cn.eagle.cool/blog/post/best-websites-designers-love-for-finding-design-inspirations)

| 标题                                               | 描述                  | 地址 |
| :------------------------------------------------- | :-------------------- | :--- |
| [设计导航](http://hao.shejidaren.com/)             |                       |      |
| [设计导航](https://www.designnavs.com/)            |                       |      |
| [设计导航](https://idesign.qq.com/#!index/feed)    |                       |      |
| [UpLabs](https://www.uplabs.com/templates/android) | 设计资源、模版、UIKit |      |
| [Dribble](https://dribbble.com/)                   | 设计资源              |      |
| [站酷Zcool](https://www.zcool.com.cn/)             | 设计素材，UI组件等    |      |
| [产品大牛](https://www.pmdaniu.com/explore/rplib)  | 设计素材，UI组件等    |      |
| [XD资源](https://www.adobexdcn.com/resource)       |                       |      |
| [XD中文网](https://xd.94xy.com/resources.html)     | XD教程、资源导航      |      |
| [松果互联](https://www.weidea.net/)                | UI模版，网站模版      |      |
| [25学堂](https://www.25xt.com/)                    |                       |      |

## 图标素材和工具

| 标题                                                         | 描述               | 地址 |
| :----------------------------------------------------------- | :----------------- | :--- |
| [ICONS8 - 矢量图在线编辑](https://icons8.com/iconizer)       |                    |      |
| [IconFont - 阿里巴巴矢量图标库](https://www.iconfont.cn/)    |                    |      |
| [FlatIcon - Interface icons](https://www.flaticon.com/uicons/interface-icons) |                    |      |
| [IconFinder](https://www.iconfinder.com)                     |                    |      |
| [ByteDance IconPark](https://iconpark.oceanengine.com)       |                    |      |
| [ICONS8 - Icons](https://icons8.com/icons/tiny-glyph)        |                    |      |
| [设计小咖](https://www.iamxk.com/fonts/0-0-8-1.html)         | 免费字体库、图标库 |      |
| [StickPNG](http://www.stickpng.com/)                         |                    |      |
| [CleanPNG](https://www.cleanpng.com/)                        |                    |      |
| [Png images](https://pngimg.com/)                            |                    |      |
| [Png Tree](https://pngtree.com/)                             |                    |      |
| [SVGA 在线预览1](https://svga.s-y.ren/)                      |                    |      |
| [SVGA 在线预览2](https://svga.io/svga-preview.html)          |                    |      |
| [Lottie 在线预览](https://app.lottiefiles.com/preview)       |                    |      |
| [Lottie 官网](https://lottiefiles.com/)                      |                    |      |
| [Animated icons](https://icons8.com/animated-icons)          |                    |      |
| [FlatIcon - Animated icons](https://www.flaticon.com/animated-icons-most-downloaded) |                    |      |
| [ManyPixels - gallery](https://www.manypixels.co/gallery)    |                    |      |
| [illlustrations - open source illustrations kit](https://illlustrations.co/) |                    |      |
| [IRA Design](https://iradesign.io/)                          |                    |      |
| [DrawKit - ILLUSTRATIONS](https://drawkit.com/)              |                    |      |
| [Unsplash](https://unsplash.com/)                            |                    |      |

## 配色网站

| 标题                                                         | 描述                         | 地址 |
| ------------------------------------------------------------ | ---------------------------- | ---- |
| [FlatUIColors](https://flatuicolors.com/)                    | 配色模版                     |      |
| [FlatUIColorPicker](https://www.flatuicolorpicker.com/)      |                              |      |
| [Material Design Colors Platte](https://www.materialpalette.com/colors) | MaterialDesign调色板、图标等 |      |
| [Coolors](https://coolors.co/)                               | 快速生成配色方案             |      |
| [ShutterStock - 调色板（需要翻墙）](https://www.shutterstock.com/zh/colors) |                              |      |

## Artifact(构件)

| 标题                                         | 描述                  | 地址 |
| :------------------------------------------- | :-------------------- | :--- |
| [Maven Central](https://search.maven.org/)   | Maven Central仓库搜索 |      |
| [MVN Repository](https://mvnrepository.com/) | MVN仓库               |      |

## APK下载

`Google Play`国内镜像网站，下载安卓应用，有些网址可能无法访问。实在找不到就用梯子访问`Google Play`看看吧。后面推荐梯子

| 标题                                                   | 描述        | 地址                    |
| ------------------------------------------------------ | ----------- | ----------------------- |
| [ApkPure](https://apkpure.com/cn/)                     |             | https://apkpure.com/cn/ |
| [APKDownload](https://apkdownload.cc/)                 |             |                         |
| [APKDL](https://apkdl.in/)                             |             |                         |
| [APKTurbo](https://www.apkturbo.com/)                  |             |                         |
| [观道](https://www.guandao.cc/)                        |             |                         |
| [APKPremier](https://apkpremier.com/)                  |             |                         |
| [APKRaw](https://appraw.com/)                          |             |                         |
| [APKNite](https://apknite.com/)                        |             |                         |
| [ApkMirror](https://www.apkmirror.com/)                |             |                         |
| [APKCombo](https://apkcombo.com/zh-cn/)                |             |                         |
| [SameAPK](https://sameapk.com/)                        |             |                         |
| [APKSupport](https://apk.support/zh_cn/)               | @Deprecated |                         |
| [APK-Downloader](http://apps.evozi.com/apk-downloader) | @Deprecated |                         |

# 梯子

一个矛盾：没买之前有的网站无法访问，但是无法访问就无法购买。。。

| 梯子                                                         | 费用                 | 官网                                           |
| :----------------------------------------------------------- | :------------------- | :--------------------------------------------- |
| [Express](https://www.expressvpn.com/vpn-server)             | $99.95/年            | https://www.expressvpn.com/vpn-server          |
| [Panda](https://www.pandavpnpro.com/zh-cn/)                  | $29.88/年，送一年    | https://www.pandavpnpro.com/zh-cn/             |
| [Vypr](https://vyprvpn.com)                                  | $60/3年              | [https://vyprvpn.com](https://vyprvpn.com/)    |
| [Nord](https://nordvpn.com/servers/)                         | $59.00/年            | https://nordvpn.com/servers/                   |
| [CyberGhost](https://www.cyberghostvpn.com/en_US/vpn-server) | $47.88/年            | https://www.cyberghostvpn.com/en_US/vpn-server |
| [oxylabs（Residential proxy server）](https://oxylabs.io/location-proxy) | $6480/年、$9720/年、 | https://oxylabs.io/location-proxy              |
| [飞鱼VPN](https://kk.myyuyu.me/)                             | 240/年               | https://kk.myyuyu.me/                          |

# 源码阅读

| 标题                                                         | 描述                                                         | 地址 |
| :----------------------------------------------------------- | :----------------------------------------------------------- | :--- |
| [Android Code Search](https://cs.android.com/)               | Android官方源码在线查看工具，支持代码跳转，版本切换，目录查看等。需梯子 |      |
| [AndroidXRef](http://androidxref.com/)                       | Android系统源码，Android1.6到Android 9.0                     |      |
| [AOSPXRef](http://aospxref.com/)                             | Android系统源码，Android7.1到Android13                       |      |
| [Android Git Repository](https://android.googlesource.com/)  | Android官方系统源码仓库。需梯子                              |      |
| [Android社区](https://www.androidos.net.cn/sourcecode)       | Android1.6到Android10                                        |      |
| [mobibrw默默的点滴](https://mobibrw.com/Android_10.0.0_r40/) | Android10源代码私服                                          |      |
| [AndroidX源码GitHub仓库](https://github.com/androidx/androidx) | GitHub仓库                                                   |      |
| [Android SDK Search]()                                       | Chrome插件，在地址栏输入ad + tab，然后开始搜索。需梯子       |      |
| [JavaDoc](https://www.javadoc.io/)                           | `Maven Central`仓库中的开源项目代码查看                      |      |
| [Grep Code](http://grepcode.com/)                            | @Deprecated                                                  |      |

## 其他方式

1. 使用repo或者Git下载[GoogleSource](https://android.googlesource.com/)源码到本地（可以全量下载，也可以选择性下载），使用`Source Insight`、`SublimeText`、`UnderStand`等阅读。
2. 替换AndroidSDK中`platform`路径下对应版本的`android.jar`，直接在AS中查看。

> Android SDK中包含大部分framework的源码，在`source`路径下可直接查看。只是没有编译成class文件。
>
> `android.jar`不包含`hidden-api`，可以自行编译或者使用别人编译的[android.jar下载](https://github.com/anggrayudi/android-hidden-api)

**如何下载、阅读、编译源码，见下**

1. [Android源码分析系列](https://github.com/foxleezh/AOSP)
2. [AOSP源码下载官方文档](https://source.android.com/setup/build/downloading)
3. [下载Android源码以及查看源码](http://static.kancloud.cn/alex_wsc/android_source/402530)

# Android云测平台

| 标题                                                         | 描述           | 地址 |
| :----------------------------------------------------------- | :------------- | :--- |
| [OPPO 云测平台](https://open.oppomobile.com/cloudmachine/device/list-plus) |                |      |
| [三星远程开发测试平台](http://samsung.smarterapps.cn/index.php) |                |      |
| [vivo 云测平台](https://vcl.vivo.com.cn/#/machine/picking)   | 需要企业开发者 |      |
| [小米云测平台](https://testit.miui.com/remote)               | 需要企业开发者 |      |

# 百科

| 标题                                      | 描述                                           | 地址 |
| :---------------------------------------- | :--------------------------------------------- | :--- |
| [WikiHow](https://zh.wikihow.com/)        | 教这个世界上的任何人学会做任何事情。           |      |
| [果壳网](https://www.guokr.com/)          | 泛科普科学文化平台                             |      |
| [科普中国](https://www.kepuchina.cn/)     | 提供科学、权威、准确的科普信息内容和相关资讯。 |      |
| [产品经理导航](https://www.pmbaobao.com/) |                                                |      |

# 程序员接活

| 标题                                   | 描述 | 地址 |
| :------------------------------------- | :--- | :--- |
| [程序员客栈](https://www.proginn.com/) |      |      |
| [码市](https://codemart.com/)          |      |      |
| [威客](http://www.vikecn.com/)         |      |      |
| [猪八戒](https://hangzhou.zbj.com/)    |      |      |

</div>

# 如何用Markdown显示卡片样式？

1. Markdown直接嵌入`<div>`，并添加`<style>`样式，每一个链接都需要粘贴下面的代码，比较麻烦

```html
<div class="item-list">
  <div class="item">
    <a target="_blank" href="http">
      <div class="item-title">在线工具集合</div>
      <div class="item-desc">在线工具集合</div>
      <div class="item-url">https://tool.lu/</div>
    </a>
</div>
```

2. Markdown部署之后会转为静态html文件，直接在顶部添加`<style>`样式，通过开发者工具找到对应的标签，将html表格改为卡片样式。
   1. 如果有两个表格，一个要改样式，一个不改样式，可以在表格前后添加`<div id="xxx">`标签，根据id或class选择css样式

# TODO

参考[闪击工作台](https://nav.sankki.com/#/index)UI设计
