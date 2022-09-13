# Windows LTSC 2021 Microsoft Store安装

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

鼠标右键使用PowerShell运行`install-Microsoft-Store.ps1`