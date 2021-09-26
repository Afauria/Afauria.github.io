---
layout: post
title: 命令行笔记
date: 2018-10-04
categories: 笔记
tags: 
- 笔记
description: 命令行笔记
keywords: [mac , cli]
---

windows命令行工具推荐cmder，cmder

windows和mac下命令有所区别，使用cmder的别名功能可以进行统一

mac系统基于unix内核，linux是类unix系统，因此两者命令基本一样，有细微差别



| 作用                 | Linux/Mac         | windows                              |
| -------------------- | ----------------- | ------------------------------------ |
| 打开文件或文件夹     | open [path]       | explorer.exe [path]、explorer [path] |
| 列出当前目录文件     | ls                | ls                                   |
| 列出当前目录文件详情 | ll                | ls -alF、dir。（-R：递归遍历）       |
| 打印当前目录路径     | pwd               | pwd                                  |
| 拷贝文本             | pbcopy（mac专有） | 无                                   |
| 查看系统信息         | sw_vers           | winver                               |
| 计算器               | bc                | calc                                 |
| 查看ip               | ifconfig          | ipconfig                             |
| 匹配字符串           | grep              | find                                 |
| 创建文件夹           | mkdir             | mkdir、md                            |
| 创建文件             | touch             | type、touch                          |
| 查看应用安装路径     | which             | where                                |
| 查看系统磁盘使用情况 | df                | df                                   |
| 查看目录或文件大小   | du                | du                                   |
|                      |                   |                                      |
|                      |                   |                                      |
|                      |                   |                                      |
|                      |                   |                                      |
|                      |                   |                                      |

* `cd /d c:\Users\41001\Desktop`：`/d`表示直接进入该盘符