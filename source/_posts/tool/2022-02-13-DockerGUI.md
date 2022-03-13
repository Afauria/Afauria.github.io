---
layout: post
title: Linux容器运行GUI程序
date: 2022-02-13
description: Docker Linux容器运行GUI程序尝试。Linux安装图形环境。Docker常用操作笔记。
categories: 工具
tags: 
- 工具
- Flutter
- Docker
- Linux
---

# 背景

研究Flutter跨平台应用在Linux上运行。由于没有Linux电脑，因此尝试使用Docker容器代替Linux主机环境，将编译好的Flutter应用放到Linux容器中运行。

本文只介绍如何在Linux容器中运行GUI程序，不介绍Flutter编译相关。只演示x86_64架构Linux容器，arm和arm64步骤相同。

# Mac上运行Docker Linux GUI程序

Linux本身不带图形界面，需要安装桌面环境。有两种方式X Window和VNC：

* X Window System本身支持网络传输，本地开启X Server服务，远程X Client应用通过ssh连接到本地。
* VNC（Virtual Network Console）用于远程控制桌面，远程开启VNC服务，本地通过VNC Viewer或浏览器连接到远程。类似于Windows下的RDP（Remote Desktop Protocol）。

X Window以X Client应用为单位。VNC以桌面为单位。

> x11vnc：是一个VNC Server，通过X协议要求X Server将画面显示和控制权交给VNC Server，并且将X界面通过VNC共享给远程，默认端口为5900

## 使用X Window

原理：**Mac提供了XQuartz工具，支持在Mac上运行X11**。在主机端启动X Server，容器中启动X Client应用，建立连接，XServer将画面输出到显示器。

步骤：

1. Mac主机安装XQuartz：`brew install XQuartz`

2. 打开XQuartz：在偏好设置-安全性中，勾选"允许从网络客户端连接"，重启XQuartz

3. 运行xhost：`xhost +`

   > * `xhost +`：允许所有客户端连接，不需要认证
   > * `xhost -`：开启访问控制，只有认证的机器能够连接
   > * `xhost + IP地址`：允许某台机器连接

4. 下载Ubuntu镜像：`docker pull ubuntu`

5. 运行容器：`docker run -itd --name ubuntu-env ubuntu /bin/bash`

6. 进入Ubuntu容器，并设置DISPLAY环境变量：`docker exec -it -e DISPLAY=主机IP地址:0 ubuntu-env /bin/bash`。（或者进入容器中使用export命令设置）

7. 更新apt包管理器下载路径：`apt update`

7. 安装gnome桌面环境：`apt install gnome-core`

8. 打开GUI程序：`gnome-help`、`gnome-calculator`、`firefox`，Mac电脑上成功显示Linux GUI程序界面

无法运行`mutter`、`gnome-shell`、`gnome-session`、`gnome-control-center`等，报错如下：

```shell
root@88f72f82f080:/# mutter
Window manager warning: Unsupported session type
root@88f72f82f080:/# gnome-shell
Window manager warning: Unsupported session type
root@88f72f82f080:/# gnome-session
libGL error: No matching fbConfigs or visuals found
libGL error: failed to load driver: swrast
libGL error: No matching fbConfigs or visuals found
libGL error: failed to load driver: swrast
gnome-session-binary[3604]: WARNING: software acceleration check failed: Child process exited with code 1
gnome-session-binary[3604]: CRITICAL: We failed, but the fail whale is dead. Sorry....
root@88f72f82f080:/# gnome-control-center
libGL error: No matching fbConfigs or visuals found
libGL error: failed to load driver: swrast

(gnome-control-center:3626): Gdk-ERROR **: 19:25:07.958: The program 'gnome-control-center' received an X Window System error.
This probably reflects a bug in the program.
The error was 'BadValue (integer parameter out of range for operation)'.
  (Details: serial 173 error_code 2 request_code 149 (GLX) minor_code 24)
  (Note to programmers: normally, X errors are reported asynchronously;
   that is, you will receive the error a while after causing it.
   To debug your program, run it with the GDK_SYNCHRONIZE environment
   variable to change this behavior. You can then get a meaningful
   backtrace from your debugger if you break on the gdk_x_error() function.)
Trace/breakpoint trap
```

Flutter应用运行同样报错，尝试了很多方法还是无法解决。

## 使用VNC

直接使用`dorowu/ubuntu-desktop-lxde-vnc`镜像，不需要自己安装图形环境。

步骤：

1. 下载Ubuntu桌面镜像（大约500M）：`docker pull dorowu/ubuntu-desktop-lxde-vnc`
2. 创建并运行容器：`docker run -d --name ubuntu-desktop-lxde-vnc -p 6080:80 -p 5900:5900 -e VNC_PASSWORD=passwd -v /dev/shm:/dev/shm dorowu/ubuntu-desktop-lxde-vnc`
3. 浏览器访问：`{服务器ip地址}:6080/`
4. 输入密码passwd，成功连接Linux容器桌面。
5. 在VNC桌面上点击图标可以运行Flutter应用

> 用命令行执行，需要先`export DISPLAY=:1.0`

![](2022-02-13-DockerGUI/Linux使用VNC运行Flutter.png)

# 其他Docker操作

本节内容和要实现的目标没有关系，算是走了一些弯路和尝试，不过也是一些比较有用的知识点。

## 使用ssh登录Docker Linux容器环境

目标：使用ssh方式直接登录到本地或远程Docker容器。

* 本地Docker容器：也可以直接`docker exec`进入容器
* 远程Docker容器：也可以先使用ssh连接到服务器，再使用`docker exec`进入容器。

步骤：

1. 下载Docker官方ubuntu镜像：`docker pull ubuntu`

2. 创建并运行容器，将主机8022端口映射到容器的22端口：`docker run -it --name ubuntu-env -p 8022:22 ubuntu /bin/bash`

3. 此时进入了容器终端。使用`-d`参数可以后台运行，不进入终端。之后可以通过`docker exec -it ubuntu-env /bin/bash`命令进入

4. 容器中安装ssh服务：`apt install openssh-server openssh-client vim`

5. 修改root登录权限：`vim /etc/ssh/sshd_config`，将PermitRootLogin值改为yes，取消注释

6. 修改root密码：`passwd root`

7. 生成ssh密钥，如果已有文件则可跳过

   ```shell
   $ ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key
   $ ssh-keygen -t ecdsa -f /etc/ssh/ssh_host_ecdsa_key
   $ ssh-keygen -t ed25519 -f /etc/ssh/ssh_host_ed25519_key
   ```

8. 启动ssh服务：`service ssh start`

9. 输入exit或者`control+D`退出容器

10. 主机通过ssh登陆容器Linux环境：`ssh -p 8022 root@localhost`（也可以输入IP连接远程机器的Docker容器）

如果连不上的话可以重启下容器`docker restart ubuntu-env`再进入容器启动ssh服务

容器创建的时候没有指定端口映射，如何修改？（挂载同理）

> 方法一：制作新镜像，重新创建容器。（推荐）
>
> ```shell
> # 停止容器
> $ docker stop ubuntu-env
> # 将容器制作为镜像
> $ docker commit ubuntu-env ubuntu-env
> # 删除容器
> $ docker rm ubuntu-env
> # 使用新镜像重新创建容器
> $ docker run -it --name ubuntu-env -p 8022:22 ubuntu-env /bin/bashs
> ```
>
> 方法二：修改容器配置，重启Docker服务。（不推荐，会导致其他容器重启）
>
> 方法三：容器运行时修改端口映射：
>
> ```shell
> iptables -t nat -A DOCKER -p tcp --dport 宿主机端口 -j DNAT --to-destination 容器ip:容器端口
> ```

## 打包服务器的Docker镜像到本地机器使用

目标：将远程Linux服务器的Docker容器打包成镜像，拷贝到本地机器（MacOS）加载，避免重新安装一遍环境（gnome、ssh、git、vim等）。

步骤：

1. 将容器制作为镜像：`docker commit [container] [image]`
2. 服务器打包镜像：`docker save -o image.tar ubuntu-env:latest`
3. 本地机器开启远程登录：系统偏好设置-共享-远程登录
4. 拷贝镜像到本地机器：`scp image.tar Afauria@ip地址:/Users/Afauria/Desktop/`
5. 本地机器下载Docker，加载镜像：`docker load < image.tar`
6. 使用`docker image ls`可以看到已经成功加载镜像

# 结语

[Ubuntu镜像](https://hub.docker.com/_/ubuntu)有不同架构的版本，例如x86_64、ARM64、ARM：

* `docker pull ubuntu`
* `docker pull arm64v8/ubuntu`
* `docker pull arm32v7/ubuntu`

[Ubuntu桌面VNC镜像]((https://hub.docker.com/r/dorowu/ubuntu-desktop-lxde-vnc))只有x86_64、ARM64的版本：

* `docker pull dorowu/ubuntu-desktop-lxde-vnc`
* `docker pull dorowu/ubuntu-desktop-lxde-vnc:focal-arm64`

> 运行其他架构的容器需要利用QEMU虚拟化技术：
>
> * Mac电脑默认支持
> * Linux电脑需要手动安装：`apt install qemu-user-static`

Docker中运行GUI参考资料：

* [running-gui-apps-with-docker](http://fabiorehm.com/blog/2014/09/11/running-gui-apps-with-docker/)
* [Docker Containers on the Desktop](https://blog.jessfraz.com/post/docker-containers-on-the-desktop/)：Docker中运行GUI程序
* [StackOverflow：Can-you-run-gui-applications-in-a-linux-docker-container](https://stackoverflow.com/questions/16296753/can-you-run-gui-applications-in-a-linux-docker-container/25280523#25280523)：解决方案较全
* [issue：Allow running GNOME desktop/shell within docker](https://gitlab.gnome.org/GNOME/gnome-shell/-/issues/1545)
* [x11docker](https://github.com/mviereck/x11docker)：在Linux容器中运行GUI程序（不支持MacOS）
* [X11vnc (简体中文)](https://wiki.archlinux.org/title/X11vnc_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))