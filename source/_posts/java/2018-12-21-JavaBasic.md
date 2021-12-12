---
layout: post
title: java基础笔记（占坑）
date: 2018-12-21
description: 平常写代码的时候很多细节没有注意，就是凭感觉和习惯，理论很少去记，因此记录下来作为复习和回顾
categories: Java
tags: 
- Java
---

# 知识点

## 重写和重载

* 重写：子类对父类方法重新定义，具有相同的方法名，参数，返回类型，若是重写了方法，则要使用父类方法需要使用super，子类访问权限不能比父类严格，子类抛出异常范围不能比父类大（RuntimeException除外）
* 重载：参数个数、类型不同，返回值可以不同

## 数组定义

* 定义一维数组时，必须显式指明数组的长度； 
* 定义多维数组时，其一维数组的长度必须首先指明，其他维数组长度可以稍后指定； 
* 采用给定值初始化数组时，不必指明长度； `int[] a = {1, 2, 3}`
* “[]” 是数组运算符的意思，在声明一个数组时，数组运算符可以放在数据类型与变量之间，也可以放在变量之后。

二维数组声明可以如下：

```java
int a[][] = new int[10][10];
int []b[] = new int[10][10];
int [][]c = new int[10][10];
//多维数组可以先声明第一维长度，后面的长度可以稍后声明
int d[][] = new int[10]【】;
```

## 四种引用

* 强引用：普通的引用
* 软引用：内存不足时被回收
* 弱引用：除了弱引用外没有其他的引用则会被回收
* 虚引用：相当于没有引用，要与引用队列配合使用
  * 可以进行重要对象回收监听，进行日志统计
  * 系统gc监听：因为虚引用每次GC都会被回收，那么我们就可以通过虚引用来判断gc的频率，如果频率过大，内存使用可能存在问题，才导致了系统gc频繁调用

引用队列：引用的对象将要被JVM回收时，会将其加入到引用队列中。通过引用队列可以了解JVM垃圾回收情况。

# 细节

## &&和&的区别

* &&：短路与，即前面的表达式能确定结果就不执行后面的表达式，可以用来代替简单的if语句
* &：不短路与，前后表达式都需要执行

## 接口可以继承多个接口

* 类只能继承一个类，但可以实现多个接口
* 接口不可以实现接口，但可以继承多个接口（不用实现） A extends B,C

## equals和==

==判断是否是同一个对象（对于非基本类型）

equals判断的是内容是否相同，可以通过重写对象的equals方法来自定义比较规则

```java
//例
String a = new String("123");
String b = new String("123");
System.out.println(a==b);//false
System.out.println(a.equals(b));//true
```

## String常量池

```java
String a = "123";
String b = "123";
System.out.println(a==b);//true：同一个对象。
//使用双引号创建的是字符串常量，存储在常量池中
//创建常量对象的时候会先判断常量池中是否已经存在，如果存在则直接引用

String a = "123";
String b = new String("123");
System.out.println(a==b);//false
//使用new String创建对象，存放在堆中，两个引用不相等
//实际上是将常量池中的123复制到了堆中，如果常量池没有，会先再常量池中创建，如下

String a = new String("123");
//实际上创建了两个对象，一个在常量池，一个在堆中
//如果前面常量池已经有该字符串，则只创建一个对象。
```

## 继承时构造方法

* 子类构造方法总是先调用父类的构造方法，如果没有显式指明调用父类哪个构造方法，则默认调用无参构造方法
* 若父类没有无参构造方法，子类需要在自己的构造函数中显式调用父类的构造函数`super(arg);`，并且一定要在第一行调用。若不调用，编译器会报错

## 继承时初始化顺序

- 父类的静态变量
- 父类静态代码块
- 子类的静态变量
- 子类的静态代码块
- 父类的普通变量
- 父类普通代码块
- 父类无参构造函数
- 子类的普通变量
- 子类普通代码块
- 子类无参构造函数

## 自动装箱/拆箱

装箱：将8个基本类型转换成对应的包装类型。拆箱则反过来

### 基本数据类型和包装类

在Java语言中，`new`一个对象是存储在堆里的，我们通过栈中的引用来使用这些对象；所以，对象本身来说是比较消耗资源的。对于经常用到的类型，如int等，如果我们每次使用这种变量的时候都需要new一个Java对象的话，就会比较笨重。

Java是一种面向对象语言，很多地方都需要使用对象而不是基本数据类型。比如，在集合类中，我们是无法将int 、double等类型放进去的。因为集合的容器要求元素是Object类型。为了让基本类型也具有对象的特征，就出现了包装类型，它相当于将基本类型“包装起来”，使得它具有了对象的性质，并且为其添加了属性和方法，丰富了基本类型的操作。

| 基本数据类型（内置类型） | 对应的包装类型 | 大小             |
| ------------------------ | -------------- | ---------------- |
| byte                     | Byte           | 1个字节          |
| boolean                  | Boolean        | 1个字节或4个字节 |
| char                     | Character      | 4字节            |
| short                    | Short          | 2个字节          |
| int                      | Integer        | 4个字节          |
| long                     | Long           | 8个字节          |
| float                    | Float          | 4字节            |
| double                   | Double         | 8字节            |

实际上，Java中还存在另外一种基本类型`void`，它也有对应的包装类`java.lang.Void`，不过我们无法直接对它们进行操作。

**补充：数据超出范围，溢出不会抛异常，也没有任何提示。**

boolean类型占1或4个字节：理论上只需要1bit空间，但是计算机处理数据的最小单位是1个字节，实际存储的空间是：用1个字节的最低位存储，其他7位用0填补

位（bit）是计算机存储的最小单位，字节是计算机处理数据的最小单位，1字节=8位

> 《Java虚拟机规范》一书中的描述：“虽然定义了boolean这种数据类型，但是只对它提供了非常有限的支持。在Java虚拟机中没有任何供boolean值专用的字节码指令，Java语言表达式所操作的boolean值，在编译之后都使用Java虚拟机中的int数据类型来代替，而boolean数组将会被编码成Java虚拟机的byte数组，每个元素boolean元素占8位”。这样我们可以得出boolean类型占了单独使用是4个字节，在数组中又是1个字节。
>
> 使用int的原因是，对于当下32位的处理器（CPU）来说，一次处理数据是32位（这里不是指的是32/64位系统，而是指CPU硬件层面），具有高效存取的特点。

### 自动装箱、拆箱

* 在Java SE5之前，装箱：`Integer i = new Integer(10);`
* 在Java SE5中，提供了自动装箱、拆箱功能

自动装箱、拆箱原理：通过包装类的valueOf()和xxxValue();方法实现

举例：

```java
Integer i =10;  //自动装箱
int b= i;     //自动拆箱
```

将上述代码反编译后得到

```java
public static  void main(String[]args){
    Integer integer=Integer.valueOf(1); //装箱
    int i=integer.intValue(); //拆箱
}
```

### 常见场景

```java
//基本数据类型放入集合类
List<Integer> li = new ArrayList<>();
for (int i = 1; i < 50; i ++){
    li.add(i);
}
```

```java
//包装类型与基本数据类型比较
//理论上==是比较对象地址，这里实现了拆箱
Integer a=1;
System.out.println(a==1?"等于":"不等于");//等于
Boolean bool=false;
System.out.println(bool?"真":"假");//真
```

```java
//包装类型的运算
Integer i = 10;
Integer j = 20;
System.out.println(i+j);
```

```java
//三目运算符使用，当第二，第三位操作数分别为基本类型和对象时，其中的对象就会拆箱为基本类型进行操作。
boolean flag = true;
Integer i = 0;
int j = 1;
int k = flag ? i : j;//这里对i进行拆箱，如果是null，会发生NPE，拆箱：i.intValue();
```

```java
//函数参数和返回值
//自动拆箱
public int getNum1(Integer num) {
 return num;
}
//自动装箱
public Integer getNum2(int num) {
 return num;
}
```



# 参考文章

[什么是Java中的自动拆装箱](https://blog.csdn.net/wufaliang003/article/details/82347077)

[你真的知道Java中boolean类型占用多少个字节吗？](https://www.jianshu.com/p/2f663dc820d0)

待补充更新知识点：//todo

https://www.jianshu.com/p/b5b919f24f82

https://www.jianshu.com/p/2adb8fe74987

https://mp.weixin.qq.com/s/63TOcAyQL9LIEX9UHLtmyw