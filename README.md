# qBittorrent Random Cleaner / qBittorrent 随机清理

## Random / 随机

Why do we need random ...

为什么需要随机清理？因为随机足够简单，只需要1个参数 delete_probability (0-1) 控制，避免选择困难症。否则，当磁盘满了的时候，我们需要根据分享率(Ratio)、Seeds、Peers、Last Activity来综合决定哪些需要删除。

If every one ...

如果大家都按照相似的策略进行清理，例如分享率>xx，那么冷门资源就可能变成死种。随机清理能让种子之间变得更加平等，减少死种的风险。

