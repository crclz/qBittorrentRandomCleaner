# qBittorrent Random Cleaner / qBittorrent 随机清理

## Random / 随机

Why do we need random cleaning? Because randomness is simple enough—it only requires control via one parameter, delete_probability (with a value range of 0-1), which helps avoid the difficulty of making choices. Otherwise, when the disk is full, we would have to comprehensively decide which torrents to delete based on metrics like Ratio, Seeds, Peers, and Last Activity.

为什么需要随机清理？因为随机足够简单，只需要1个参数 delete_probability (0-1) 控制，避免选择困难症。否则，当磁盘满了的时候，我们需要根据分享率(Ratio)、Seeds、Peers、Last Activity来综合决定哪些需要删除。

If everyone uses similar cleaning strategies—for instance, deleting torrents where the Ratio is greater than a certain value (e.g., Ratio > xx)—then less popular torrents may end up becoming dead torrents. Random cleaning helps make torrents more equal to each other and reduces the risk of torrents becoming dead.

如果大家都按照相似的策略进行清理，例如分享率>xx，那么冷门资源就可能变成死种。随机清理能让种子之间变得更加平等，减少死种的风险。


## Environment Setup / 环境配置

1. Install Git and the latest version of Python. (Refer to online tutorials for guidance)
2. Clone this repository using Git: `git clone <repository-url>`
3. Install the required Python packages: `pip install -r requirements.txt`

The project was developed using uv. If you are a uv user, run `uv sync` instead of directly installing from requirements.txt. If you're unfamiliar with uv, you can ignore this section.


1. 安装 Git 和最新版本的 Python。（可参考网上教程）
2. 使用 Git 克隆本仓库：git clone `<仓库地址>`
3. 安装所需的 Python 包：`pip install -r requirements.txt`

本项目基于 uv 开发。如果您是 uv 用户，请运行 `uv sync`，而非直接从 requirements.txt 安装。如果您不了解 uv，可以忽略此部分。


## Do cleaning / 进行清理

1. Run `python main.py` (for uv users: `uv run main.py`. If you do not know what is uv, just ignore this.)


2. The script will ask you these things: webui port, directory to clean, delete_probability. After showing the torrents to be cleaned, it will ask you whether to continue. Just carefully read what the python program output, and follow the instruction, you can finally do cleaning.



TODO: uv china mainland tutorial


