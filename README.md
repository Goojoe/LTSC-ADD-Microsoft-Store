## Windows LTSC Microsoft Store 最新版下载安装脚本
- Windows LTSC 2021
- Windows LTSC 2019

测试通过

---

### 1.安装Python

- [镜像下载](https://mirror.bjtu.edu.cn/python/3.10.8/)
- [官方下载](https://www.python.org/downloads/)

安装时需勾选`Add Python 3.10 to PATH`

<img src="https://i0.hdslb.com/bfs/album/470bd8fff34b02f858814bf43afe4542c51d3127.png" referrerpolicy="no-referrer">

## 🔽下载软件包

```
pip install ltscaddstore -i https://mirror.sjtu.edu.cn/pypi/web/simple/
```

### 2.运行脚本

```
# 写入文件
echo "import ltscaddstore" > ltscaddstore.py
echo "ltscaddstore.download()" >> ltscaddstore.py
# 运行
python ltscaddstore.py
```



## 软件来源

> 所有软件来自https://store.rg-adguard.net/
>
> Url(Link) `https://www.microsoft.com/store/productId/9WZDNCRFJBMP` RP

## 关于转载

版权属于`Microsoft`,禁止商用

⚠️不允许转载后的内容需要”回复“、”登录“、”关注公众号“、”积分购买“以及其他任何不能直接下载的形式展现
