# Windows LTSC Microsoft Store 安装
## 截图
LTSC2021测试通过,系统来源[Windows 10 企业版2021 LTSC 21H2 Build 19044.1865](https://www.ghxi.com/win10ltsc21h2.html)

![image](https://user-images.githubusercontent.com/78355492/189969985-bb82fbd0-c25a-41f0-89b9-3a8228d6cd1f.png)

## 下载软件包

### 1.下载压缩包

- [Github官方,较慢](https://github.com/Goojoe/LTSC-ADD-Microsoft-Store/releases/latest/download/LTSC-ADD-Microsoft-Store.zip)

✨镜像地址(国内推荐)

- [ghdl.feizhuqwq.cf](https://ghdl.feizhuqwq.cf/https://github.com/Goojoe/LTSC-ADD-Microsoft-Store/releases/latest/download/LTSC-ADD-Microsoft-Store.zip)
- [cdn.githubjs.cf](https://cdn.githubjs.cf/Goojoe/LTSC-ADD-Microsoft-Store/releases/latest/download/LTSC-ADD-Microsoft-Store.zip)
- [ghps.cc](https://ghps.cc/https://github.com/Goojoe/LTSC-ADD-Microsoft-Store/releases/latest/download/LTSC-ADD-Microsoft-Store.zip)
- [gh.gh2233.ml](https://gh.gh2233.ml/https://github.com/Goojoe/LTSC-ADD-Microsoft-Store/releases/latest/download/LTSC-ADD-Microsoft-Store.zip)
- [archive.fastgit.org](https://archive.fastgit.org/Goojoe/LTSC-ADD-Microsoft-Store/releases/latest/download/LTSC-ADD-Microsoft-Store.zip)
- [ghproxy.com](https://ghproxy.com/https://github.com/Goojoe/LTSC-ADD-Microsoft-Store/releases/latest/download/LTSC-ADD-Microsoft-Store.zip)

### 2.使用Git下载

```bash
# Github官方,较慢
git clone https://github.com/Goojoe/LTSC-ADD-Microsoft-Store.git

# 国内的镜像,任选其一
git clone https://gitclone.com/github.com/Goojoe/LTSC-ADD-Microsoft-Store.git

git clone https://kgithub.com/Goojoe/LTSC-ADD-Microsoft-Store.git

git clone https://ghproxy.com/https://github.com/Goojoe/LTSC-ADD-Microsoft-Store.git

git clone https://hub.njuu.cf/Goojoe/LTSC-ADD-Microsoft-Store.git

git clone https://hub.yzuu.cf/Goojoe/LTSC-ADD-Microsoft-Store.git
```

## 更改脚本执行策略

```powershell
# 打开powershell管理员,允许powershell(ps1)脚本
set-ExecutionPolicy RemoteSigned

执行策略更改
执行策略可帮助你防止执行不信任的脚本。更改执行策略可能会产生安全风险，如 https:/go.microsoft.com/fwlink/?LinkID=135170
中的 about_Execution_Policies 帮助主题所述。是否要更改执行策略?
[Y] 是(Y)  [A] 全是(A)  [N] 否(N)  [L] 全否(L)  [S] 暂停(S)  [?] 帮助 (默认值为“N”): A
# 输入A 按Enter键
```

## 执行脚本

鼠标右键使用 PowerShell 运行`install-Microsoft-Store.ps1`

> 所有软件来自https://store.rg-adguard.net/
>
> Url(Link) `https://www.microsoft.com/store/productId/9NBLGGH4NNS1` RP

