# Insert your code here.
import pyperclip
import requests
from lxml import etree
import os
import time
import i18n
import yaml


def download():
    class MyLoader(i18n.loaders.YamlLoader):
        loader = yaml.FullLoader

    i18n.register_loader(MyLoader, ["yml", "yaml"])

    # 选择语言
    i18n.load_path.append("i18n")

    print("Please select language:")
    print("""
    1 English
    2 简体中文
    3 Français
    4 日本語
    5 Deutsch
    6 Español
    """)
    language = int(input())

    languages = {
        1: "en",
        2: "zh",
        3: "fr",
        4: "ja",
        5: "de",
        6: "es"
    }

    if language in languages:
        selected_language = languages[language]
        i18n.set("locale", selected_language)
    else:
        print("Input error, exiting")

    print(
        f"""--------------------------------------
{i18n.t('locale.script-name')}
{i18n.t('locale.gtihub-repo')}
{i18n.t('locale.author')}
--------------------------------------"""
    )

    def check_name(file_name, keyword1):
        keyword2 = "_neutral_"
        if (keyword1 in file_name) or (keyword2 in file_name):
            return 1
        else:
            return 0

    name = input(
        f"""{i18n.t('locale.selective-architecture')}:
1 arm
2 arm64
3 x64
4 x86
:"""
    )

    name = int(name)
    name -= 1

    #  架构列表
    keyword_list = ["_arm_", "_arm64_", "_x64_", "_x86_"]

    save_path_root = "Download"
    # 如果文件不存在则创建
    if not os.path.exists(save_path_root):
        os.mkdir(save_path_root)

    api_url = "https://store.rg-adguard.net/api/GetFiles"
    store_url = "https://www.microsoft.com/store/productId/9WZDNCRFJBMP"
    success_text = (
        "<p>The links were successfully received from the Microsoft Store server.</p>"
    )

    # 代理
    is_proxy = input(f"{i18n.t('locale.proxy')}:\n:")
    if is_proxy == "y":
        http = input(f"{i18n.t('locale.input_proxy')}:\n")
        proxies = {"http": http, "https": http}
    elif is_proxy == "n":
        proxies = {}
        print(f"{i18n.t('locale.no-proxy-required')}")
    else:
        print(f"{i18n.t('locale.input-error')}")
        exit()

    print(f"{i18n.t('locale.in-the-request')}")

    # 爬虫
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {"type": "url", "url": store_url}

    # API请求
    response = requests.post(
        url=api_url, data=data, headers=headers, proxies=proxies, verify=True
    )

    response.encoding = "utf-8"

    if response.status_code == 200:
        print(f"{i18n.t('locale.request-successful')}")
    else:
        print(f"{i18n.t('locale.request-failed')}")
        exit()

    html = etree.HTML(response.content.decode())  # 传字符串
    link = html.xpath("//a/@href")
    link_text = html.xpath("//a/text()")
    li = ["BlockMap", "eappxbundle", "emsixbundle"]

    # 下载代码
    if len(link) == len(link_text):
        for i in range(len(link)):
            li2 = [0 for p in li if (p in link_text[i])]
            if len(li2) == 0:
                if check_name(link_text[i], keyword_list[name]):
                    try:
                        f = requests.get(link[i])
                        with open(f"{save_path_root}/{link_text[i]}", "wb") as code:
                            code.write(f.content)
                        print(
                            f"{link_text[i]} {i18n.t('locale.download-successfully')}"
                        )
                    except:
                        print(f"{link_text[i]} {i18n.t('locale.download-failure')}")

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
        print(i18n.t("locale.creating-an-installation-script"))
        with open(f"{save_path_root}/install_ms-store.ps1", "w") as install_file:
            install_file.write(install_file_content)
            install_file.close()
    else:
        print(i18n.t("locale.the-installation-script-already-exists"))

    pyperclip.copy(
        "Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope LocalMachine -Force"
    )
    print(
        f"""
{i18n.t('locale.installation-instructions')}
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope LocalMachine -Force

{i18n.t('locale.command-copied')}
"""
    )
    print(i18n.t("locale.open-download-folder"))

    time.sleep(5)
    os.startfile(save_path_root)


if __name__ == "__main__":
    download()
