---
layout: post
title: Github访问不稳定解决
date: 2021-4-12
categories: 笔记
tags: 
- 笔记
description: Github访问不稳定解决
keywords: [github]
---

### 访问慢的原因

DNS解析耗时。

* DNS（域名系统，Domain Name System）：将[域名](https://baike.baidu.com/item/域名)和[IP地址](https://baike.baidu.com/item/IP地址)相互映射的一个分布式数据库。
* DNS（域名服务器，Domain Name Server）：将域名转换为IP地址的服务器。

### 解决方案

手动修改系统hosts文件，将github域名对应的ip保存到hosts文件中，访问github的时候可以直接访问该ip，不需要dns解析。

* windows系统在`C:\Windows\System32\drivers\etc\hosts`，打开普通用户读写权限`右键-属性-安全-选择当前用户-编辑-修改权限-确认`
* mac系统在`/etc/hosts`，sudo申请权限

> Hosts是一个没有扩展名的系统文件，其作用就是保存常用的网址域名与其对应IP地址的映射，当用户在浏览器中输入一个需要登录的网址域名时，系统会首先自动从Hosts文件中寻找对应的IP地址，一旦找到，系统会立即打开对应网页，如果没有找到，则系统会将网址提交DNS服务器进行IP地址的解析，再进行访问。

步骤如下：

1. [查询github网站IP](https://github.com.ipaddress.com/)

2. [查询github域名IP](https://fastly.net.ipaddress.com/github.global.ssl.fastly.net)

3. [查询github静态资源IP](https://github.com.ipaddress.com/assets-cdn.github.com)

4. 修改hosts文件，添加如下映射。前三个步骤如果查到多个IP的话可以配置多个

   ```text
   140.82.113.4 github.com
   199.232.69.194 github.global.ssl.fastly.net
   185.199.108.153 assets-cdn.github.com
   185.199.109.153 assets-cdn.github.com
   185.199.110.153 assets-cdn.github.com
   185.199.111.153 assets-cdn.github.com
   ```

5. cmd执行命令，刷新DNS缓存：`ipconfig /flushdns`

6. 隔一段时间ip可能会变，需要重新配置

7. Github上有牛人提供了脚本，一键获取github最新的IP，并更新hosts文件，clone下来，执行index.cmd即可。https://github.com/luozheao/setHost

附：查询ip地址的网站：[ipaddress网站](https://www.ipaddress.com/)、[站长工具](http://tool.chinaz.com/dns)

### GitPage博客无法访问

同理，只需要查询博客地址对应的IP，配置hosts就可以解决了。

困扰已久的问题，一直以为是需要翻墙vpn，原来是DNS服务器限制。