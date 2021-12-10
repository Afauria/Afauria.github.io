---
layout: post
title: Hexo介绍
date: 2018-10-18
categories: 工具
tags: 
- 工具
- Hexo
- 博客
description: Hexo一些概念、命令、配置等
---

# Hexo目录

```
.
├── _config.yml 	//站点配置文件
├── package.json	//npm配置
├── scaffolds		//模版 文件夹。当您新建文章时，Hexo 会根据 scaffold 来建立文件。
├── source			//子文件夹相当于一个个页面(page)，每个页面对应一个布局文件，可以修改主题里的配置文件改变样式
|   ├── _drafts		//草稿页面：存放所有草稿
|   ├── _posts		//文章页面：存放所有文章，所有文章都是同一个布局
|   ├── about		//关于页面
|   ├── categories	//分类页面
|   ├── tags		//标签页面
|   └──………………
└── themes			//主题
```



# Hexo一些基本概念

## Front-matter

前页（扉页、版权页、目次等），位于文章最上方`---`分隔的区域，做一些变量声明和配置。也可以用json格式，使用`;;;`分隔

| 参数 | 描述 | 默认值 |
| --- | --- | --- |
| `layout`     | 布局 |              |
| `title`      | 标题 |              |
| `date`       | 建立日期 | 文件建立日期 |
| `updated`    | 更新日期 | 文件更新日期 |
| `comments`   | 开启文章的评论功能   | true |
| `tags`       | 标签（不适用于分页），无顺序 |       |
| `categories` | 分类（不适用于分页），有顺序 |       |
| `permalink`  | 覆盖文章网址 |   |

## 模板（Scaffold）

模板决定了网站内容的呈现方式，可以根据模板生成初始化文章

| 模板 | 用途 | 回调 |
| --- | --- | ---|
| index | 首页 | post |
| post | 文章 | index |
| page | 分页 | index |
| archive | 归档 | index |
| category | 分类归档 | archive |
| tag | 标签归档 | archive |

## 局部模版（Partial）

可以在不同模板之间共享相同的组件，例如页首（Header）、页脚（Footer）或侧边栏（Sidebar）等，可利用局部模板功能分割为个别文件，让维护更加便利

## 布局（Layout）

如果页面结构类似，例如两个模板都有页首（Header）和页脚（Footer），您可考虑通过「布局」让两个模板共享相同的结构。一个布局文件必须要能显示 body 变量的内容，如此一来模板的内容才会被显示

## 变量

### 全局变量

| 变量           | 描述                                                         |
| -------------- | ------------------------------------------------------------ |
| `site`         | [网站变量](https://hexo.io/zh-cn/docs/variables#%E7%BD%91%E7%AB%99%E5%8F%98%E9%87%8F) |
| `page`         | 针对该页面的内容以及 front-matter 所设定的变量。             |
| `config`       | 网站配置                                                     |
| `theme`        | 主题配置。继承自网站配置。                                   |
| `_` (单下划线) | [Lodash](http://lodash.com/) 函数库                          |
| `path`         | 当前页面的路径（不含根路径）                                 |
| `url`          | 当前页面的完整网址                                           |
| `env`          | 环境变量                                                     |

### 网站变量

| 变量              | 描述     |
| ----------------- | -------- |
| `site.posts`      | 所有文章 |
| `site.pages`      | 所有分页 |
| `site.categories` | 所有分类 |
| `site.tags`       | 所有标签 |

### 页面变量

#### 页面（page）

| 变量               | 描述                                                         |
| ------------------ | ------------------------------------------------------------ |
| `page.title`       | 页面标题                                                     |
| `page.date`        | 页面建立日期（[Moment.js](http://momentjs.com/) 对象）       |
| `page.updated`     | 页面更新日期（[Moment.js](http://momentjs.com/) 对象）       |
| `page.comments`    | 留言是否开启                                                 |
| `page.layout`      | 布局名称                                                     |
| `page.content`     | 页面的完整内容                                               |
| `page.excerpt`     | 页面摘要                                                     |
| `page.more`        | 除了页面摘要的其余内容                                       |
| `page.source`      | 页面原始路径                                                 |
| `page.full_source` | 页面的完整原始路径                                           |
| `page.path`        | 页面网址（不含根路径）。我们通常在主题中使用 `url_for(page.path)`。 |
| `page.permalink`   | 页面的完整网址                                               |
| `page.prev`        | 上一个页面。如果此为第一个页面则为 `null`。                  |
| `page.next`        | 下一个页面。如果此为最后一个页面则为 `null`。                |
| `page.raw`         | 文章的原始内容                                               |
| `page.photos`      | 文章的照片（用于相簿）                                       |
| `page.link`        | 文章的外部链接（用于链接文章）                               |

#### 文章（post）：和 `page` 布局类似，但是添加了下列变量。

| Variable          | Description              |
| ----------------- | ------------------------ |
| `page.published`  | 如果该文章已发布则为True |
| `page.categories` | 该文章的所有分类         |
| `page.tags`       | 该文章的所有标签         |

#### 首页（index）

| 变量               | 描述                                                         |
| ------------------ | ------------------------------------------------------------ |
| `page.per_page`    | 每页显示的文章数量                                           |
| `page.total`       | 总文章数                                                     |
| `page.current`     | 目前页数                                                     |
| `page.current_url` | 目前分页的网址                                               |
| `page.posts`       | 本页文章                                                     |
| `page.prev`        | 上一页的页数。如果此页是第一页的话则为 `0`。                 |
| `page.prev_link`   | 上一页的网址。如果此页是第一页的话则为 `''`。                |
| `page.next`        | 下一页的页数。如果此页是最后一页的话则为 `0`。               |
| `page.next_link`   | 下一页的网址。如果此页是最后一页的话则为 `''`。              |
| `page.path`        | 当前页面的路径（不含根目录）。我们通常在主题中使用 `url_for(page.path)`。 |

#### 归档 (archive)：与 `index` 布局相同，但新增以下变量。

| 变量           | 描述                         |
| -------------- | ---------------------------- |
| `page.archive` | 等于 `true`                  |
| `page.year`    | 年份归档 (4位)               |
| `page.month`   | 月份归档 (没有前导零的2位数) |

#### 分类 (category)：与 `index` 布局相同，但新增以下变量。

| 变量            | 描述     |
| --------------- | -------- |
| `page.category` | 分类名称 |

#### 标签 (tag)：与 `index` 布局相同，但新增以下变量。

| 变量       | 描述     |
| ---------- | -------- |
| `page.tag` | 标签名称 |

# Hexo常用命令

## 安装插件

| 命令                                 | 解释            |
| ------------------------------------ | --------------- |
| npm install -g hexo-cli              | 安装hexo插件    |
| npm update -g hexo-cli               | 升级            |
| npm install hexo-deployer-git --save | 安装部署git插件 |
| hexo --version、hexo -v              | 查看版本        |
| hexo list <type>                     | 列出网站资料    |

## 简写

| 简写              | 完整                | 解释                      |
| ----------------- | ------------------- | ------------------------- |
| hexo n "我的博客" | hexo new "我的博客" | 新建文章                  |
| hexo p            | hexo publish        | 发表草稿                  |
| hexo g            | hexo generate       | 生成，                    |
| hexo s            | hexo server         | 启动服务预览              |
| hexo d            | hexo deploy         | 将.deploy目录部署到GitHub |

## 基本流程

| 命令                       | 解释                                                         |
| -------------------------- | ------------------------------------------------------------ |
| hexo init [folder]         | 新建站点。如果没有设置 `folder` ，Hexo 默认在目前的文件夹建立站点。 |
| hexo server                | 启动服务，监视文件变动并自动更新，无须重启服务器。默认地址：http://localhost:4000/ |
| hexo server -s             | 静态模式，只使用静态文件                                     |
| hexo server -p 5000        | 指定服务端口启动，默认4000                                   |
| hexo server -i 192.168.1.1 | 自定义 IP，默认localhost                                     |
| hexo server -l             | 启动日记记录，使用覆盖记录格式                               |
| hexo clean                 | 清除缓存文件 (`db.json`) 和已生成的静态文件 (`public`)。     |
| hexo g                     | 生成静态网页至public目录                                     |
| hexo g --watch             | 监视文件变动                                                 |
| hexo d                     | 部署网站                                                     |

## 写作

`hexo new [layout] <title>`：新建文章。如果指定设置 `layout` 的话，默认使用站点配置文件 [_config.yml](https://hexo.io/zh-cn/docs/configuration) 中的 `default_layout` 参数（默认为post）代替。如果标题包含空格的话，使用引号括起来。

* hexo new post 文章名：新建文章，会在`source/_post/`目录下新建文件
* hexo new draft 草稿名：新建草稿，会在`source/_draft/`目录下新建文件
* hexo new page 页面名：新建页面，会生成`source/页面名/index.md`，如关于、分类、标签

可以自定义模版，在`scaffolds`目录下新建或修改模版文件，`hexo new `会从`scaffolds`文件夹下找到对应的模版，生成文件。

## 其他选项

| 命令                     | 解释                                                         |
| ------------------------ | ------------------------------------------------------------ |
| hexo --safe              | 在安全模式下，不会载入插件和脚本。安装新插件遭遇问题时，可以尝试以安全模式重新执行 |
| hexo --debug             | 在终端中显示调试信息并记录到 `debug.log`                     |
| hexo --silent            | 隐藏终端信息                                                 |
| hexo --config custom.yml | 自定义配置文件的路径，执行后将不再使用 `_config.yml`         |
| hexo --draft             | 显示 `source/_drafts` 文件夹中的草稿文章                     |
| hexo --cwd /path/to/cwd  | 自定义当前工作目录（Current working directory）的路径。      |

# Hexo配置参数说明

站点配置文件：`站点根目录/_config.yml`

| 字段        | 说明                                |
| ----------- | ----------------------------------- |
| title       | 网站标题                            |
| subtitle    | 副标题                              |
| description | 描述、签名                          |
| keywords    | 博客关键字，利于SEO（搜索引擎优化） |
| author      | 作者、昵称                          |
| language    | 语言，如zh-Hans                     |
| timezone    | 时区                                |
| theme       | 主题                                |
| deploy      | 部署网站                            |
| permalink   | 永久链接                            |

```
deploy: 
    type: 部署方式，如git
    repo: 仓库地址
    branch: 分支名
```

permalink配置示例：
使用`hexo new post "文章"`生成文章时会自动命名，并且生成静态文件时会生成相应的文件夹路径。
| 参数                            | 结果                        |
| ------------------------------- | --------------------------- |
| `:year/:month/:day/:title/`     | 2013/07/14/hello-world      |
| `:year-:month-:day-:title.html` | 2013-07-14-hello-world.html |
| `:category/:title`              | foo/bar/hello-world         |

permalink变量
| 变量          | 描述                                                       |
| ------------- | ---------------------------------------------------------- |
| `:year`       | 文章的发表年份（4 位数）                                   |
| `:month`      | 文章的发表月份（2 位数）                                   |
| `:i_month`    | 文章的发表月份（去掉开头的零）                             |
| `:day`        | 文章的发表日期 (2 位数)                                    |
| `:i_day`      | 文章的发表日期（去掉开头的零）                             |
| `:title`      | 文件名称                                                   |
| `:post_title` | 文章标题                                                   |
| `:id`         | 文章 ID                                                    |
| `:category`   | 分类。如果文章没有分类，则是 `default_category` 配置信息。 |

# Hexo图片路径配置

Hexo Markdown文章中使用图片需要将图片放到`source/images`文件夹下，通过`![](/images/图片名称)`引用。

这种方式在**Typora中无法预览图片**

解决方案：

1. 修改_config.yml文件：`post_asset_folder: true`
   1. 使用`hexo new post 文章名称`时，会创建相同名称的文件夹
   2. 将要引用的图片放到该文件夹下
2. 安装插件：`npm install https://github.com/CodeFalling/hexo-asset-image`
3. 文章中引用图片路径：`![](文件夹名称/图片名称)`

# Hexo支持mermaid图表

1. 安装插件：`npm install hexo-filter-mermaid-diagrams`
2. 旧版本配置步骤多一点
3. 新版本直接在**主题配置文件**中启用mermaid即可

```yml
# theme/next/_config.yml
# Mermaid tag
mermaid:
  enable: true
  # Available themes: default | dark | forest | neutral
  theme: forest
```

# 结束语

参考[Hexo官方文档](https://hexo.io/zh-cn/docs/)，下篇介绍Hexo更换主题：以NexT为例，并进行简单的配置。