---
layout: post
title: Android工具使用常见问题（占坑）
date: 2019-3-1
description: Android工具，常见问题
categories: Android
tags: 
- Android
keywords: [android]
---

# 1. 模拟器

## 1.1. Windows运行Android模拟器

### 1.1.1. Intel CPU

Intel CPU使用HAXM（Hardware Accelerated Execution Manager）技术，使用基于 Intel(R) Virtualization Technology (VT) 的硬件加速，实现 Android 模拟器加速。

需要在BIOS中开启硬件支持VT，并且Android sdk需要安装Intel x86 Emulator Accelerator（HAXM）扩展。

### 1.1.2. AMD CPU

AMD通过Android Studio运行模拟器会报错，如提示CPU不支持，或者建议使用x86模拟器。在BIOS中开启虚拟化也没用。

解决办法：

* 使用GenyMotion模拟器，并且在Android Studio上安装GenyMotion插件。
  * 问题：GenyMotion使用Virtual Box虚拟化技术，而我的电脑运行了Docker，Docker在Windows上使用的是Hyper-V虚拟化技术，两个一起开会出问题。
* 官方在Android Emulator 27.3.1上给出了解决方案，结合了Win10的Hyper-V技术。
  * Win10系统
  * 在Android sdk中安装Android Emulator 27.3.1以上的版本
  * 安装x86的镜像，x86_64（打开很慢）和armeabi-v7a（更慢）
  * 在控制面板->程序->启用或关闭Windows功能中，打开**indows虚拟机监控程序平台（Windows Hypervisor Platform）**
  * 重启电脑

### 1.1.3. 总结

* 如果是IntelCPU还是建议使用HAXM，支持硬件加速。
* 如果是AMD CPU建议使用Win10的Hyper-V技术
* 建议使用x86模拟器，速度能快很多倍

参考[Android模拟器安装](https://android-developers.googleblog.com/2018/07/android-emulator-amd-processor-hyper-v.html)