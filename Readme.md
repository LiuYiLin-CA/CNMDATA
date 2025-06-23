# CNMDATA

通过青龙面板自动爬取云图

#### 使用方法

1.1订阅此仓库，自动完成文件架构

1.2手动构建

1. 青龙面板-脚本管理，创建空文件CNMDATA.py和CNMDATA_BACKUP.py，将相关代码复制粘贴
2. 创建空文件./Pull/last_success.json

2.在CNMDATA.py中填写Bark api以启用bark推送

```python
BARK_API = ""  # 这里可以配置自己的bark api
```

3.添加python依赖项 request

4.创建CNMDATA定时任务

- 名称：CNMDATA
- 命令：python CNMDATA.py
- 定时规则：\* * * * *

5.创建CNMDATA_BACKUP定时任务

- 名称：CNMDATA_BACKUP
- 命令：python CNMDATA_BACKUP.py
- 定时规则：0 0 0 * * *

---

> [luyii-code-1/CNMDATA: CNM雷达反射率图自动爬取](https://github.com/luyii-code-1/CNMDATA)

