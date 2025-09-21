# 中国大陆如何使用uv

中国大陆使用uv，面临以下问题：
- pypi源下载问题：和pip相同的问题，解决方案也类似，解决方案也比较简单
- python解释器下载问题：如果.python-version定义的python版本在本地没有，那么uv会下载解释器，非常缓慢

## pypi源下载问题
这个问题解决方案比较简单，但是网上容易找到错误的资料。

请认准官方文档：https://docs.astral.sh/uv/concepts/configuration-files/

首先，你需要建立一个uv.toml文件，内容如下。注意，第一行不是`[[tool.uv.index]]`

```toml
[[index]]
url = "https://test.pypi.org/simple"
default = true
```

然后，你需要将uv.toml放到合适的位置，来应用于你电脑上所有的uv项目。按照官方文档，简单来说，Linux和MacOS会需要放到`~/.config/uv/uv.toml`, Windows需要放到`%APPDATA%\uv\uv.toml`

## python解释器下载问题


