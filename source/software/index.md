---
layout: post
title: 软件和工具收藏
date: 2018-01-01
description: 好用的工具收藏记录。包括日常、工作、开发、设计等工具。
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
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
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
  .item-list td a {
    text-decoration: none;
    border: none;
  }
</style>

<div class="item-list">

# 工作

| 软件                              | 说明                                                         |
| --------------------------------- | ------------------------------------------------------------ |
| Typora                            | Markdown编辑器，支持实时预览，1.0以上开始收费，只能去网上找旧版本了 |
| MdNice                            | Markdown编辑器，支持微信公众号、知乎、掘金等平台文章排版     |
| [Coding.net](https://coding.net/) | 腾讯旗下。一站式协作平台，代码管理、项目管理、敏捷开发       |
| Termux                            | 安卓系统下命令行工具，可以安装node、npm、git、hexo等工具。主要用来在平板上写博客<br />apt upgrade<br />pkg install git/nodejs-lts/openssh/proot/tsu<br />配置git用户、别名、ssh key等<br />安装hexo、gitbook等插件 |

# 开发

## IDE

| 软件           | 说明                      |
| -------------- | ------------------------- |
| Android Studio | JetBrains系列，安卓开发   |
| Intellij Idea  | JetBrains系列，Java开发   |
| Webstorm       | JetBrains系列，前端开发   |
| Pycharm        | JetBrains系列，Python开发 |
| VsCode         | 代码编辑器                |
| Sublime Text   | 文本编辑器                |
| HBuilder       | 前端开发                  |
| DreamWeaver    | Adobe系列，前端开发       |

## 开发环境

| 软件        | 说明                     |
| ----------- | ------------------------ |
| Java        |                          |
| Git         |                          |
| Python      |                          |
| Mysql       |                          |
| Android SDK |                          |
| Docker      | 应用容器引擎             |
| Jenkins     | 持续集成工具             |
| Nexus       | Maven私服                |
| Gradle      |                          |
| Node        |                          |
| Flutter SDK | 配合AS Dart和Flutter插件 |
| Kotlin      |                          |
| MongoDB     | 面向文档存储数据库       |

## 开发工具

| 软件       | 说明                                                |
| ---------- | --------------------------------------------------- |
| SourceTree | 版本控制工具                                        |
| Navicat    | 数据库管理工具                                      |
| Docker     | 应用容器引擎                                        |
| Genymotion | 模拟器                                              |
| FeHelper   | Web开发者助手，包含大量工具集合，支持谷歌浏览器插件 |

## 反编译

| 软件                                                         | 说明                                 |
| ------------------------------------------------------------ | ------------------------------------ |
|[IDA](https://hex-rays.com/ida-free/)                        | iOS反汇编工具                       |
|[Hopper Disassembler](https://www.hopperapp.com/download.html) | iOS反汇编工具，试用版半小时需要重启一次 |
|[jadx](https://github.com/skylot/jadx)                        | 反编译apk，查看源码                  |
|[jd-gui](http://java-decompiler.github.io/)                   | 查看jar源码文件                      |
|[dex2jar](https://github.com/pxb1988/dex2jar)                 |                                      |
|[apktool](https://ibotpeaches.github.io/Apktool/)             | 反编译apk                            |
|[jbe](http://set.ee/jbe/)                                     | 字节码编辑器，用于查看和修改class字节码文件 |
|[CrackTool](https://github.com/Jermic/Android-Crack-Tool)     | 反编译、签名、可视化工具 |
|[smali2jar](https://github.com/demitsuri/smali2java)          | smali文件转jar文件 |
|[smali](https://github.com/JesusFreke/smali)                  | Smali转换工具    |
|[vdexExtractor](https://github.com/anestisb/vdexExtractor)    | vdex转dex  |

## AS插件

| 软件                                   | 说明                                              |
| -------------------------------------- | ------------------------------------------------- |
| Android ButterKnife Zelezny            | 根据布局id生成ButterKnife                         |
| GsonFormat                             | Json字符串转换为Java Bean                         |
| GsonOrXmlFormat                        | Gson和xml转实体类                                 |
| Android Studio Prettify                | 生成findViewById代码                              |
| Android Code Generator                 | 根据布局文件生成Activity、Fragment、Adapter等代码 |
| Android Parcelable code generator      | 生成Parcelable序列化代码                          |
| Android Material Design Icon Generator | 生成MaterialDesign图标                            |
| SelectorChapek for Android             | 根据资源文件命名自动生成selector资源              |
| Lifecycle Sorter                       | 对Activity、Fragment生命周期方法排序              |
| Android Methods Count                  | 统计依赖库方法数                                  |
| Markdown                               | 编辑Markdown，实时预览                            |
| Material Theme UI                      | 修改AS主题                                        |
| PlantUML integration                   | PlantUML生成和预览                                |
| Translation                            | 翻译工具，快捷键：Command+Control+U               |
| PsiViewer                              | Program Structure Interface，查看java文件PSI结构  |
| GenyMotion                             | 从AS启动GenyMotion模拟器                          |
| ASM Bytecode Outline                   | 查看Java字节码、ASM代码                           |
| ASM Bytecode Viewer Support Kotlin     | 查看Java字节码、ASM代码                           |
| Class Decompile                        | 查看Java字节码                                    |
| UML Support                            | 查看UML类图                                       |

## API调试、文档工具

| 软件                                      | 说明                                               |
| ----------------------------------------- | -------------------------------------------------- |
| [Eolink APIKit](https://www.eolinker.com) | 支持协作                                           |
| [RAP](http://rap2.taobao.org/)            | 支持版本管理                                       |
| [EasyAPI](https://www.easyapi.com/)       |                                                    |
| [apizza](https://www.apizza.net/)         | 支持发送http请求、生成http请求代码，markdown编辑等 |
| [showdoc](https://www.showdoc.cc/)        |                                                    |
| [DOClever](http://doclever.cn)            | 已注销                                             |
| [Apifox](https://www.apifox.cn/)          | 支持API文档、接口请求、Mock、测试等                |
| [Postman](https://www.postman.com/)       | API调试                                            |
|                                           |                                                    |

## 抓包

| 软件                                       | 说明                   |
| ------------------------------------------ | ---------------------- |
| [Charles](https://www.charlesproxy.com/)   | HTTP代理、监控         |
| [wireshark](https://www.wireshark.org/)    | 网络协议分析器         |
| [Fiddler](https://www.telerik.com/fiddler) | 改写http代理，截取数据 |

# 设计

## Adobe

| 软件        | 说明           |
| ----------- | -------------- |
| Ps          | 图片处理       |
| Ai          | 矢量图处理     |
| Pr          | 视频编辑       |
| Ae          | 视频编辑和特效 |
| DreamWeaver | 前端开发       |

## 原型设计、功能流程图

| 软件                                    | 说明                                              |
| --------------------------------------- | ------------------------------------------------- |
| axure                                   | 产品原型                                          |
| [xiaopiu](https://www.xiaopiu.com/)     | 产品原型                                          |
| [墨刀](https://modao.cc/)               | 产品原型                                          |
| [fluidui](https://www.fluidui.com/)     | web和移动应用原型                                 |
| [marvel app](https://marvelapp.com/)    | 产品原型                                          |
| Principle                               | 交互设计软件                                      |
| Sketch                                  | 矢量绘图工具                                      |
| [Figma](https://www.figma.com/)         | 产品、交互、设计、开发在线多人协作。标注、切图    |
| [蓝湖](https://lanhuapp.com/web/#/item) | 产品、交互、设计、开发在线多人协作。标注、切图    |
| visio                                   | 多种图绘制                                        |
| processOn                               | 支持多种图和模版，在线编辑。免费版限制创建9个文件 |
| Edraw                                   | 亿图，多种图绘制                                  |
| [drawio](https://app.diagrams.net/)     | 流程图、UML、架构等，支持在线编辑                 |
| [plantuml](https://plantuml.com/zh/)    | 语法绘制生成uml图                                 |
| [staruml](https://staruml.io/)          | uml绘制，客户端下载使用                           |
| XMind:Zen                               | 思维导图                                          |
| MindNote                                | 思维导图                                          |
| [GitMind](https://gitmind.cn/)          | 思维导图                                          |

# 工具

| 软件                                                         | 说明                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| 格式工厂                                                     |                                                              |
| LICEcap                                                      | 截图录屏工具                                                 |
| Shadowsocks                                                  |                                                              |
| 蓝灯                                                         |                                                              |
| 有道词典                                                     | 鼠标选中翻译                                                 |
| [uTools](https://u.tools/)                                   | 跨平台，支持多种插件，快速唤起                               |
| Cmder                                                        | Windows下命令行工具                                          |
| [Microsoft Remote Desktop](https://docs.microsoft.com/en-us/windows-server/remote/remote-desktop-services/clients/remote-desktop-clients?redirectedfrom=MSDN) | 远程桌面连接，支持多系统                                     |
| [AltStore](https://altstore.io/)                             | iOS应用签名工具，常用于在iPhone上运行模拟器APP，而不需要越狱 |

> PC端安装AltServer，填入AppleID。连接手机，为手机安装AltStore，再从AltStore中下载应用。
>
> 本质是利用Apple开发者的调试APP功能，让iPhone能够运行调试版App，并且不需要信任未知来源的企业证书。

## 梯子

一个矛盾：没买之前有的网站无法访问，但是无法访问就无法购买。。。

| 梯子                                                         | 费用                 |
| :----------------------------------------------------------- | :------------------- |
| [Express](https://www.expressvpn.com/vpn-server)             | $99.95/年            |
| [Panda](https://www.pandavpnpro.com/zh-cn/)                  | $29.88/年，送一年    |
| [Vypr](https://vyprvpn.com)                                  | $60/3年              |
| [Nord](https://nordvpn.com/servers/)                         | $59.00/年            |
| [CyberGhost](https://www.cyberghostvpn.com/en_US/vpn-server) | $47.88/年            |
| [oxylabs（Residential proxy server）](https://oxylabs.io/location-proxy) | $6480/年、$9720/年、 |
| [飞鱼VPN](https://kk.myyuyu.me/)                             | 240/年               |

# mac

| 软件                                             | 说明                                   |
| ------------------------------------------------ | -------------------------------------- |
| Alfred                                           | 搜索神器                               |
| OminiGraffle                                     | 绘图软件，类似windows的Microsoft visio |
| iTerm2+Oh My Zsh                                 | 命令行工具                             |
| MacDown                                          | markdown编辑器                         |
| [Parallel DesktopMac](https://www.parallels.cn/) | mac上使用windows软件，避免安装虚拟机   |
| [Dash](https://kapeli.com/dash)                  | 下载离线文档集，代码API文档浏览、搜索  |

# 其他

## 建模、游戏

| 软件             | 说明                                      |
| ---------------- | ----------------------------------------- |
| Unity            | 游戏引擎                                  |
| Unreal           | 虚幻游戏引擎                              |
| World Machine    | 绘制地形，导出到引擎中使用                |
| 3dMax            | 建模                                      |
| Maya             | 建模                                      |
| ZBrush           | 雕刻                                      |
| SubstancePainter | 是一款基于物理效果（PBR）的3d材质绘制工具 |
| xNormal          | 贴图制作工具                              |

## unity插件

| 软件          | 说明                   |
| ------------- | ---------------------- |
| Shader Editor | 基于节点的着色器编辑器 |
| Shader Forge  | 基于节点的着色器编辑器 |

</div>
