---
layout: post
title: js或ts语法笔记
date: 2018-12-12
description: 前端语法笔记，老实说我分不清哪些是es6的哪些是ts的语法，只是看到代码中有用到过，做个笔记，比较杂
categories: 前端
tags: 
- 前端
---

## javascript

* `==`和`===`

  * ==会自动转换类型比较
  * ===严格比较，类型需要相同
  * !=和!==同理
* `success?.() `相当于`success && success()`，判断不为空再执行
* (+”1”)把字符串转换成整数

### 

### prototype 

prototype 属性允许您向对象添加属性和方法

**注意：** Prototype 是全局属性，适用于所有的Javascript对象。

```javascript
function employee(name,jobtitle,born)
{
	this.name=name;
	this.jobtitle=jobtitle;
	this.born=born;
}
var fred=new employee("Fred Flintstone","Caveman",1970);
employee.prototype.salary=null;
fred.salary=20000;
document.write(fred.salary);
```

给employee函数添加了salary属性，可以.出来



### argument

在函数代码中，使用特殊对象 arguments，开发者无需明确指出参数名，就能访问它们。

```
function howManyArgs() {
  alert(arguments.length);
}
howManyArgs("string", 45);    //2
howManyArgs();    //0
howManyArgs(12);    //1

```

注意：与其他程序设计语言不同，ECMAScript 不会验证传递给函数的参数个数是否等于函数定义的参数个数。开发者定义的函数都可以接受任意个数的参数（根据 Netscape 的文档，最多可接受 255 个），而不会引发任何错误。任何遗漏的参数都会以 undefined 传递给函数，多余的函数将忽略。

### pipeline写法

```
data 
|> fnx
|> fny
|> fnz
```

相当于fnz(fny(fnx(data)))，pipeline写法

### 纯函数

### 高阶函数

### 函数柯里化

```javascript
function connect(a,b){
 var func=function(c){}
 return func;
}
```

connect（a,b）=func（c）

connect(mapStateToProps,mapDispatchToProps)(MainPage)

实际上是这样func(c)(MainPage);

MainPage是赋值给里面的c，而不是对应a，b



