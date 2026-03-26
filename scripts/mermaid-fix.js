hexo.extend.filter.register('after_post_render', function(data) {
  if (!hexo.config.mermaid || !hexo.config.mermaid.enable) {
    return;
  }

  data.content = data.content.replace(
    /<pre class="mermaid">([\s\S]*?)<\/pre>/g,
    '<pre><code class="mermaid">$1</code></pre>'
  );
});