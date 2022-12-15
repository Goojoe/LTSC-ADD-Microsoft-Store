# Insert your code here.
import pyperclip
import requests
from lxml import etree
import os
import time

def download():
    print("""--------------------------------------
脚本名称:LTSC 微软商店 最新版下载脚本
Github项目地址:https://github.com/Goojoe/LTSC-ADD-Microsoft-Store
作者:咕咕乔
--------------------------------------""")

    def check_name(file_name,keyword1):
        keyword2="_neutral_"
        if (keyword1 in file_name) or (keyword2 in file_name):
            return 1
        else:
            return 0

    name =input("""请选择架构(输入数字):
1 arm
2 arm64
3 x64
4 x86
:""")

    name =int(name)
    name -=1

    #  架构列表
    keyword_list=["_arm_","_arm64_","_x64_","_x86_"]

    save_path_root = input("输入保存路径:\n:")

    # 如果文件不存在则创建
    if not os.path.exists(save_path_root):
        os.mkdir(save_path_root)

    api_url = "https://store.rg-adguard.net/api/GetFiles"
    store_url = "https://www.microsoft.com/store/productId/9WZDNCRFJBMP"
    success_text = "<p>The links were successfully received from the Microsoft Store server.</p>"

    # 代理
    is_proxy = input("是否需要配置HTTP代理(y/n):\n:")
    if is_proxy == "y":
        http = input("请输入HTTP代理例子:(127.0.0.1:1080):\n")
        proxies = {
        "http": http,
        "https": http
    }
    elif is_proxy == "n":
        proxies = {}
        print("不需要代理")
    else:
        print("输入错误,退出")
        exit()

    print("请求中,请等待,失败可尝试配置代理")

    # 爬虫
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "type":"url",
        "url":store_url
    }

    # API请求
    response = requests.post(url=api_url,data=data,headers=headers,proxies=proxies)

    response.encoding = "utf-8"

    if response.status_code == 200:
        print("请求成功,请耐心等待1-10分钟下载文件")
    else:
        print("网络请求失败")
        exit()


    html = etree.HTML(response.content.decode()) # 传字符串
    link = html.xpath("//a/@href")
    link_text = html.xpath("//a/text()")
    li=["BlockMap","eappxbundle","emsixbundle"]

    # 下载代码
    if len(link) == len(link_text):
        for i in range(len(link)):
            li2=[0 for p in li if (p in link_text[i])]
            if len(li2)==0:
                if check_name(link_text[i],keyword_list[name]):
                    try:
                        f = requests.get(link[i])
                        with open(f"{save_path_root}/{link_text[i]}","wb") as code:
                            code.write(f.content)
                        print("{} 下载成功".format(link_text[i]))
                    except:
                        print("{} 下载失败".format(link_text[i]))

    # 安装脚本
    install_file_content = """Add-AppxPackage *.Appx
Add-AppxPackage *.AppxBundle
Add-AppxPackage *.Msixbundle
Write-Output "==========================================="
Write-Output "    The Microsoft Store was installed      "
Write-Output "==========================================="
pause
"""
    if not os.path.exists(f"{save_path_root}/install_ms-store.ps1"):
        print("创建安装脚本")
        with open(f"{save_path_root}/install_ms-store.ps1", "w") as install_file:
            install_file.write(install_file_content)
            install_file.close()
    else:
        print("安装脚本已存在,停止创建")

    pyperclip.copy("Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope LocalMachine -Force")
    print("""
右键使用Powershell执行install_ms-store.ps1即可,若出现:
--------------------
禁止在此系统执行脚本
--------------------
请以<管理员>权限打开Powershell,执行:
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope LocalMachine -Force

命令已复制到剪贴板
可以Ctrl + V 或鼠标右键PowerShell窗口粘贴
""")
    print("下载完成,10秒后自动打开文件夹")

    time.sleep(10)
    os.startfile(save_path_root)

if __name__ == "__main__":
    download()