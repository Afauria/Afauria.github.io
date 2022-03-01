---
layout: post
title: depot_tools工具介绍
date: 2022-01-04
description: 介绍depot_tools工具：gclient、gn、ninja等
categories: 工具
tags: 
- 工具
- Flutter
---

# depot_tools介绍

Google用python开发的git仓库管理工具，用于管理chromium源码。包括gclient、repo、gn和ninja等工具。是对Git的增强，大项目由几十个独立的git仓库构成，不便于下载、提交和管理。

* [下载地址](https://chromium.googlesource.com/chromium/tools/depot_tools.git)
* [简介](https://www.chromium.org/developers/how-tos/depottools)
* [使用手册](https://commondatastorage.googleapis.com/chrome-infra-docs/flat/depot_tools/docs/html/depot_tools_tutorial.html)

`gclient`：将多个git仓库组成一个`Solution`进行管理，通过gclient获取源码和依赖的仓库，类似Git submodule。

> * `git submodule`：git子仓库管理工具
> * `repo`：与`gclient`作用相同，gclient更新一点。gclient根据.gclient和DEPS配置文件检出依赖模块源码，repo根据manifest.xml配置文件检出模块源码。
> * `Solution`：包含DEPS文件的仓库
> * `DEPS`：记录Solution中的项目依赖关系
> * `roll_deps`：用于更新DEPS文件中某个依赖的代码版本
> * `Gerrit/Rietveld`：Code Review（代码审核）的系统，可以和`git/svn`集成
> * `git cl`：Change List，用于查看代码修改，类似`git diff`
> * `LKGR`（Last Known Good Revision）：记录最新的测试通过的版本

[ninja](https://ninja-build.org/)：编译工具，负责编译最终的可执行文件。依赖其他构建工具进行高级语言编译。

[gn](https://gn.googlesource.com/gn)：生成ninja所需的构建文件，可以针对不同平台生成不同的ninja构建文件。`gn help`查看帮助

## 安装

1. clone仓库：`git clone https://chromium.googlesource.com/chromium/tools/depot_tools.git`
2. 设置环境变量：`.bash_profile`文件中添加`export PATH=/{your_path}/depot_tools/:$PATH`

# gn介绍

gn工具将`xx.gn`文件转换成`.ninja`文件，ninja根据`.ninja`文件生成目标程序。类似cmake和make的关系。

官方文档主要有两篇[gn命令](https://gn.googlesource.com/gn/+/refs/heads/main/docs/reference.md)、[gn语法](https://gn.googlesource.com/gn/+/refs/heads/main/docs/language.md)，语法类似python

## gn使用

1. 在项目根目录创建`.gn`文件，用于指定构建配置文件路径，一般叫`BUILDCONFIG.gn`
2. 在构建配置文件中指定编译工具链
3. 在项目根目录创建`BUILD.gn`文件，指定编译目标、配置等。
4. 对应的依赖模块中也定义`BUILD.gn`文件

## BUILD.gn文件语法

简单介绍下，具体参考官方文档

### 添加编译参数

```
declare_args() {
  enable_test = true
}
```

### 添加宏

定义的宏可以直接在C/C++的代码中使用

```
defines = [ "AWESOME_FEATURE", "LOG_LEVEL=3" ]
```

### 添加编译单元

target是最小的编译单元，常见的target类型如

1. `executable`：生成可执行程序
2. `shared_library`：生成动态链接库，如`.dll`和`.so`文件
3. `static_library`：生成静态链接库，如`.lib`和`.a`文件
4. `source_set`：生成虚拟静态库，比`static_library`快
5. `group`：执行一组target编译
6. `action`：执行一段脚本
7. `copy`：拷贝文件

```
executable("hello_world") {
  sources = [
    "hello_world.cc",
  ]
}
```

### 添加配置

包括编译flag、include、define等，可被其他target包含

```
config("myconfig") {
  include_dirs = [ "include/common" ]
  defines = [ "ENABLE_DOOM_MELON" ]
}

executable("hello_world") {
  configs = [ ":myconfig" ]
}
```

### 添加模版

用于定义可重用的代码，一般创建一个`.gni`文件，其他文件可以通过import引入实现共享

### 添加依赖关系

```
deps = ["//xxx"]
deps += ["//xxx"]
```

## gn执行过程

以flutter engine项目为例

1. 在当前目录查找`.gn`文件，如果不存在则往上一级查找，直到找到一个为止，将`.gn`所在的目录设置为source root。解析`.gn`文件找到buildconfig文件（构建配置文件）。如下`src/.gn`文件：

   ````
   ```
   # This file is used by the experimental meta-buildsystem in src/tools/gn to
   # find the root of the source tree and to set startup options.
   
   # Use Python 3 for exec_script() calls.
   # See `gn help dotfile` for details.
   script_executable = "python3"
   
   # The location of the build configuration file.
   buildconfig = "//build/config/BUILDCONFIG.gn"
   
   # The secondary source root is a parallel directory tree where
   # GN build files are placed when they can not be placed directly
   # in the source tree, e.g. for third party source trees.
   secondary_source = "//build/secondary/"
   ```
   ````

2. 执行构建配置文件，即`//build/config/BUILDCONFIG.gn`，整个系统只有一个，设置全局变量、默认值等，对所有build文件可见

3. 执行root目录下的`BUILD.gn`文件

4. 再根据root目录下的`BUILD.gn`文件加载其依赖目录下的其他`BUILD.gn`文件，如果在指定路径找不到的话，则在`build/secondary`的相应位置查找

5. 当一个目标的依赖都解决了，编译出`.ninja`文件保存到`out_dir/dir`下，例如`out/android_debug_unopt/obj/`下

6. 最终编译出一个根`build.ninja`文件放到`out_dir`下

# 结语

gclient使用可以参考[chromium开发工具--gclient](https://www.cnblogs.com/xl2432/p/11596695.html)、[gclient 介绍](https://keyou.github.io/blog/2017/11/02/gclient/)