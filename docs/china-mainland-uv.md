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

运行uv sync，尝试下载python解释器，如果不是特别缓慢，就可以跳过了，因为下载解释器是一次性的工作。
- 可以等它下完
- 也可以开一个翻墙软件，并且合理配置HTTP_PROXY, HTTPS_PROXY环境变量，尝试下载

如果无法解决，那么我们需要让uv向conda借一个解释器。

例如，你需要的python版本是3.8。

1. 前往anaconda官网，下载miniconda或者anaconda: https://www.anaconda.com/download/success
    - 如果无法访问，可与从tuna镜像下载miniconda。https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/ 如果不知道下载哪一个，首先网页ctrl+f搜索`miniconda3-py313`，然后选择适合你操作系统的、版本号最新的。如果后续python更新了python3.14或者更高版本，那么也可以将`miniconda3-py313`中的313替换为314或者更高版本，来找到最新的miniconda.
2. 安装conda，并确保conda在PATH中，并正确处理conda init等前置操作。（在这里不赘述，请自行搜索）
3. 替换conda源：参考 https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/ 这个页面，创建`.condarc`文件并在里面添加tuna源的地址。
4. 新建目标环境（这里假设你想使用的是python3.8）: 
    - `conda create -n py38 python=3.8`
    - 激活环境：`conda activate py38`
5. 运行uv sync，uv就会识别到PATH中有python3.8解释器，就会将解释器复制到uv项目的`.venv`目录下。


