---
layout: post
title: ReactNative学习
date: 2019-1-1
description: 笔记，常见问题
categories: Android
tags: 
- Android
- ReactNative
keywords: [android, reactnative]
---

# 1. 和传统前端的区别[【转】](https://www.jianshu.com/p/91dd6ae96a26)

## 1.1. 标签不同

* 容器：div——View
* 图片    img——Image
* 文字    所有双标签——Text
* 背景    background——ImageBackground

**注意:**

1. react native中所有的标签首字母必须大写，而html标签标准都是小写

2. react native中所有需要输出的文字必须使用`<Text></Text>`包裹,而HTML里面的双标签都可以包裹文字

3. react native的style中不支持使用background来定义背景，如果想要用图片做背景，必须使用`<ImageBackground source={require("bg.png")}></ImageBackground>`标签包裹，而html中的css中可以使用：`background:url("../images/bg.png")`。

4. HTML中的图片：`<img src="a.jpg"/>`，react native中的图片必须指定宽高：

   ```react
   <Image source="{{ uri: thumb }}" style="{{ width:100, height:100 }}" />
   ```

## 1.2. 布局样式不同

react native中不存在float，也不支持position:fixed，而是采用的flex布局，虽然react native支持position中的absolute和realative以及flex,都是和html中css有所不同:

* react native中的absolute默认相对于父级，就算父级没有定位，而css中的absolute是向上寻找的相对点，如果父级没有定位，一直往上找定位参考点
* react native中的flex的flexDirection默认值是:column而css中的默认值是row
* react native中的高度等于父级高度使用flex:1 ，而web的css中使用height:100%，react native中没有百分比的概念

*react native支持的属性：参考[属性](https://reactnative.cn/docs/0.49/layout-props.html#content)*

## 1.3. 结构不同

html加载的时候是自上而下的阻塞式加载，而react native根据生命周期来渲染，跟写的位置无关，而且react native文件一切皆js，无论是结构还是css还是JS逻辑，下面是react native的生命周期:

* constructor:组件被创建之前初始化数据
* componentWillMount组件已创建但是未被渲染，可以在这里面请求数据
* render:组件渲染，组件结构都写在这里
* componentDidMount:组件已渲染完,可以在这里请求数据并使用setState改变数据来触发视图自动更新
* componentWillReceiveProps:如果组件收到新的属性（props），就会调用此函数,并使用setState改变数据来触发视图自动更新
* shouldComponentUpdate当组件接收到新的属性和状态改变的话，都会触发调用 shouldComponentUpdate来判断组件是否应该更新
* componentWillUpdate如果组件状态或者属性改变，并且上的 shouldComponentUpdate(...) 返回为 true，就会开始准更新组件，并调用 componentWillUpdate()
* componentDidUpdate调用了 render() 更新完成界面之后，会调用 componentDidUpdate() 来得到通知
* componentWillUnmount当组件要被从界面上移除的时候，就会调用此函数，一般在这里取消定时器，remove监听事件

## 1.4. 页面跳转不同

html中使用a标签或者window.location.href来跳转页面，react native的路由跳转有多种方案,可以根据自身选择，官方推荐react-navigation，还有react-native-router-flux,navigator等

## 1.5. js运行环境不同

web中的js运行在浏览器，最上级是window，而react native里没有window的概念,组件化最上级是global,挂在global下面是跨组件的，例如global.a=1，那么在所有组件都能使用a，所以一般登录成功后把token挂在global上面，在其他任何页面请求数据的时候可以直接使用token，注销登录就清除token

# 2. 常见问题

## 2.1. React Native:Error: Cannot find module 'asap/raw'

安装`react-native-navigation`后出错

解决办法：重新安装依赖，执行`npm install`

## 2.2. setting.gradle路径问题

使用react-navigation：

* yarn add react-navigation
* yarn add react-native-gesture-handler
* react-native link react-native-gesture-handler （会修改setting.gradle，引入react-native-gesture-handler作为project module）

问题：路径使用`\`分割，不正确，应该修改为`/`

```shell
Settings file 'E:\AndroidStudioProjects\Demo\android\settings.gradle' line: 3

* What went wrong:
Could not compile settings file 'E:\AndroidStudioProjects\Demo\android\settings.gradle'.
> startup failed:
  settings file 'E:\AndroidStudioProjects\Demo\android\settings.gradle': 3: unexpected char: '\' @ line 3, column 133.
     s\react-native-gesture-handler\android')
```

## 2.3. VsCode格式化代码

VsCode格式化ReactNative代码的时候，标签尖括号会换行

解决办法：如果是js文件，下面不要选择JavaScript，而是JavaScript React，如图

![VsCode格式化ReactNative代码](/images/ReactNative/vscode_format.png)