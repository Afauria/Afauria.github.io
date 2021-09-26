---
layout: post
title: 单例模式
date: 2018-11-17
categories: 架构和设计模式
tags: 
- 设计模式
- 架构
description: 单例模式笔记
---

## 介绍

单例类通过在内部创建自己的实例，并提供给外部，保证外部访问的都是同一个对象。外部不需要实例化该类的对象（构造方法私有）

### 特点

* 自己创建自己的实例
* 将这个实例提供给外部
* 只能有一个实例

### 优点

* 减少内存开销，避免频繁创建和销毁实例
* 避免对资源的多重占用

### 缺点

* 与单一职责原则冲突：一个类应该只关心内部逻辑，而不关心外面怎么样来实例化。
* 没有接口，不能继承

## 实现

### 懒汉式，线程不安全

```java
public class Singleton {  
    private static Singleton instance;  
    private Singleton (){}  
    public static Singleton getInstance() {  
    if (instance == null) {  
        instance = new Singleton();  
    }  
    return instance;  
    }  
}
```

### 懒汉式，线程安全

```java
public class Singleton {  
    private static Singleton instance;  
    private Singleton (){}
    //使用synchronized加锁，影响效率
    public static synchronized Singleton getInstance() {  
    if (instance == null) {  
        instance = new Singleton();  
    }  
    return instance;  
    }  
}
```

### 饿汉式

```java
public class Singleton {
    private static Singleton instance = new Singleton();  
    private Singleton (){}  
    //类加载时进行实例化，浪费内存
    //通过classloader保证初始化时只有一个线程，因此是线程安全的
    public static Singleton getInstance() {  
        return instance;
    }
}
```

### 登记式/静态内部类

```java
public class Singleton {  
    //通过classloader保证初始化时只有一个线程，是线程安全的
    //通过静态内部类实现懒汉式加载
    //即使Singleton类被加载了也不会进行实例化，如调用Singleton其他方法触发Singleton类加载
    //只有显示调用getInstance()时才会加载Holder类
    private static class SingletonHolder {  
    	private static final Singleton INSTANCE = new Singleton();  
    }  
    private Singleton (){}  
    public static final Singleton getInstance() {  
    	return SingletonHolder.INSTANCE;  
    }  
}
```

### 双检锁/双重校验锁（DCL，即 double-checked locking）

```java
public class Singleton {
    //volatile保证每次从内存中读取，跳过cpu缓存
    //正常情况下，线程从内存拷贝变量到cpu缓存，每个线程可能在不同的cpu上，变量的修改是不可见的，可能会造成数据不同步
    //volatile保证可见性（一个线程的修改对另一个线程可见），不能保证原子性，不会使线程阻塞，更轻量的同步机制
    //synchronized保证可见性和原子性
    private volatile static Singleton singleton;  
    private Singleton (){}  
    //效率比第二种要高
    public static Singleton getSingleton() {  
    	if (singleton == null) {
        	synchronized (Singleton.class) {  
            	if (singleton == null) {  
                	singleton = new Singleton();  
            	}  
        	}  
    	}  
    	return singleton;  
    }  
}
```

**补充**

类加载的时机：和虚拟机有关，可能是饿汉式、也可能是懒汉式，并且受JLS保证（当有初始化需求时）

类的初始化，加载完类就进行初始化，可能由以下几种情况触发：

* 使用new关键字实例化对象，或者class.forName()反射
* 读取一个类的静态字段（被final修饰、已在编译期把结果放在常量池的静态字段除外）
* 设置一个类的静态字段（被final修饰、已在编译期把结果放在常量池的静态字段除外）
* 调用一个类的静态方法