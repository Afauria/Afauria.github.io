---
layout: post
title: java反射
date: 2019-1-14
description: Java反射
categories: Java
tags: 
- Java
---

# 1. 反射介绍

1、在运行状态中，对于任意一个类，都能够知道这个类的属性和方法。

2、对于任意一个对象，都能够调用它的任何方法和属性。

这种动态获取信息以及动态调用对象的方法的功能称为JAVA的反射。

JAVA语言编译之后会生成一个.class文件，反射就是通过字节码文件找到某一个类、类中的方法以及属性等。

# 2. 反射的作用

在JAVA中，只有给定类的名字，就可以通过反射机制来获取类的所有信息，可以动态的创建对象和编译。

# 3. 反射的原理

首先明确的概念: 一切皆对象----类也是对象.

其次明白加载: 当Animal.class在硬盘中时,是一个文件,当载入到内存中,可以认为是一个对象,是java.lang.class的对象.

类对象（字节码对象）：当JVM加载一个类时，会为这个类创建一个class对象。所有的类，都存在一个类对象，用于提供类本身的信息，比如有几种构造方法， 有多少属性，有哪些普通方法。

类的对象（实例化对象）：类的实例化

类中的内容包括：modifier  constructor  field  method.

反射的实现主要借助以下几个类：

Class：类的对象

Constructor：类的构造方法

Field：类中的属性对象

Method：类中的方法对象

Modifier

虚拟机允许两个相同类名的class被不同的ClassLoader加载，在运行时也会被认为是两个不同的类，因此需要注意不能相互赋值， 不然会抛出ClassCastException。

# 4. 代码实现

//todo待补充：https://www.jianshu.com/p/02bb399023f7