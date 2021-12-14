---
layout: post
title: 丘山月夜
date: 2018-04-14
description: 个人简介
---
<div class="poem-wrap">
  <div class="poem-border poem-left"></div>
  <div class="poem-border poem-right"></div>
  <div class="poem-title">念两句诗</div>
  <p id="poem">挑选中...</p>
	<p id="info"></p>
  <script src="https://sdk.jinrishici.com/v2/browser/jinrishici.js" charset="utf-8"></script>
  <script defer>
    jinrishici.load(function(result) {
      poem.innerHTML = result.data.content
      info.innerHTML = '【' + result.data.origin.dynasty + '】' + result.data.origin.author + '《' + result.data.origin.title + '》'
  });
  </script>
</div>

# 关于我

学海无涯，见啥爱啥

编程动漫小说游戏电视剧手工绘画戏曲等等，坐标广州

[个人简历]()

# 联系我

QQ：410013112

邮箱：afauria@foxmail.com

微信：Afauria

# 知识体系

计划将一些基础知识和体系逐步整理到GitBook中，不发布在博客里面：[GitBook-Learner](/GitBook-Learner/)

# 博客平台

使用框架：Hexo+GitPage+NexT。通过 Hexo生成，部署在 [Github](https://github.com/Afauria)，主题使用 [NexT](http://theme-next.iissnan.com/) 。

主要用于记录个人笔记，技术分享、工具使用、收藏站点，以及记录一些杂七杂八的事。

评论区已建立，欢迎留言讨论、互链、加V。也可以GitHub上提Issue。如果喜欢我的博客，可以在GitHub上点赞哦！

菜鸟上路，多多包涵。

如有侵权，请告知删除。

