#coding:utf-8
#本实例用于获取国内高匿免费代理服务器
import requests
from bs4 import BeautifulSoup

def getdata(html):  #从字符串中安装正则表达式获取值
    allproxy = []  # 所有的代理服务器信息
    soup = BeautifulSoup(html, 'html.parser')
    alltr = soup.find_all("tr", class_="")[1:]   #获取tr ，第一个是标题栏，去除

    for tr in alltr:
        alltd =tr.find_all('td')
        oneproxy ={
            'IP地址':alltd[1].get_text(),
            '端口号': alltd[2].get_text(),
            # '服务器地址': alltd[3].a.get_text(),
            '是否匿名': alltd[4].get_text(),
            '类型': alltd[5].get_text(),
            '速度': alltd[6].div['title'],
            '连接时间': alltd[7].div['title'],
            '存活时间': alltd[8].get_text(),
            '验证时间': alltd[9].get_text(),
        }
        allproxy.append(oneproxy)

    alltr = soup.find_all("tr", class_="odd")[1:]  # 获取tr ，第一个是标题栏，去除

    for tr in alltr:
        alltd = tr.find_all('td')
        oneproxy = {
            'IP地址': alltd[1].get_text(),
            '端口号': alltd[2].get_text(),
            # '服务器地址': alltd[3].a.get_text(),
            '是否匿名': alltd[4].get_text(),
            '类型': alltd[5].get_text(),
            '速度': alltd[6].div['title'],
            '连接时间': alltd[7].div['title'],
            '存活时间': alltd[8].get_text(),
            '验证时间': alltd[9].get_text(),
        }
        allproxy.append(oneproxy)
    return allproxy




#根据一个网址，获取该网址中符合指定正则表达式的内容
def getallproxy(url='http://www.xicidaili.com/nn'):
    try:
        # 构造 Request headers
        agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER'
        headers = {  # 这个http头，根据审查元素，监听发包，可以查看
            "Host": "www.xicidaili.com",
            "Referer": "http://www.xicidaili.com/",
            'User-Agent': agent
        }
        response = requests.get(url, headers=headers)  # 创建一个请求
        html = response.text  #读取返回html源码
        return getdata(html)
    except requests.exceptions.ConnectionError as e:
        print("获取代理错误")
        return []



#allproxy = getallproxy()
#print(allproxy)