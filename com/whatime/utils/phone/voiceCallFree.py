import requests
import datetime  #处理日期和时间的标准库
from random import choice
import com.whatime.utils.proxy.getPorxyFromUrl
import com.whatime.utils.proxy.getProxy

ua_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60",
        "Opera/8.0 (Windows NT 5.1; U; en)",
        "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
        "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2 ",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36"
    ]

def postPhone(phone):
    print("你所拨打的电话号码是："+phone)
    #requests.post("http://www.ucpaas.com/checkcode/voiceExtCode",data="",json="",proxies=proxies,headers=headers)
    date = datetime.datetime.now().strftime('%H:%M:%S')

    headers = {
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'Host':'www.ucpaas.com',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Origin': 'http://www.ucpaas.com',
        'Referer': 'http://www.ucpaas.com/experience',
        'Cookie': 'Hm_lvt_086fa6bc6f48b55eb534c7f49010d8cd=1541552820; c__utma=821849481.482618456.948871748.1541552820.1541552820.1; c__utmc=821849481.482618456; IESESSION=alive; 53revisit=1541552820818; 53kf_72170610_from_host=www.ucpaas.com; 53kf_72170610_keyword=; 53kf_72170610_land_page=http%253A%252F%252Fwww.ucpaas.com%252Fproduct%252Fvoice-code.html%253Bjsessionid%253D511DCC2C4C9653DC0EA5DE73C0C4A224.tomcat100; kf_72170610_land_page_ok=1; _qddaz=QD.gou8ax.sx4t0j.jo6gqxa0; _qdda=3-1.1; _qddab=3-7zb78q.jo6gqxa0; pgv_pvi=9893013504; pgv_si=s6329611264; _qddamta_4007776698=3-0; c__utmb=821849481.482618456.1541552820.1541552830.2; tencentSig=1829529600; Hm_lpvt_086fa6bc6f48b55eb534c7f49010d8cd=1541552836; JSESSIONID=1FEACCC545FC99619AAB2DA5915C9022.tomcat100',
        'X-Requested-With':'XMLHttpRequest',
        'User-Agent': choice(ua_list)
    }
    data={'phone':phone,'type':3}
    try:
        result = requests.post("http://www.ucpaas.com/checkcode/voiceExtCode", data=data, headers=headers)
    except requests.exceptions.ConnectionError:
        print(u"[%s]：发送失败 %s " % (date, result.text))
    else:
        print(u"[%s]：发送%s " % (date, result.text))

def postPhoneProxy(phone):
    print("你所拨打的电话号码是："+phone)
    #requests.post("http://www.ucpaas.com/checkcode/voiceExtCode",data="",json="",proxies=proxies,headers=headers)
    date = datetime.datetime.now().strftime('%H:%M:%S')

    ips= com.whatime.utils.proxy.getProxy.getXiGuaProxy(559234731394746, 1, True)
    proxies = {
        'http': choice(ips)
    }
    headers = {
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'Host':'www.ucpaas.com',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Origin': 'http://www.ucpaas.com',
        'Referer': 'http://www.ucpaas.com/experience',
        'Cookie': 'Hm_lvt_086fa6bc6f48b55eb534c7f49010d8cd=1541552820; c__utma=821849481.482618456.948871748.1541552820.1541552820.1; c__utmc=821849481.482618456; IESESSION=alive; 53revisit=1541552820818; 53kf_72170610_from_host=www.ucpaas.com; 53kf_72170610_keyword=; 53kf_72170610_land_page=http%253A%252F%252Fwww.ucpaas.com%252Fproduct%252Fvoice-code.html%253Bjsessionid%253D511DCC2C4C9653DC0EA5DE73C0C4A224.tomcat100; kf_72170610_land_page_ok=1; _qddaz=QD.gou8ax.sx4t0j.jo6gqxa0; _qdda=3-1.1; _qddab=3-7zb78q.jo6gqxa0; pgv_pvi=9893013504; pgv_si=s6329611264; _qddamta_4007776698=3-0; c__utmb=821849481.482618456.1541552820.1541552830.2; tencentSig=1829529600; Hm_lpvt_086fa6bc6f48b55eb534c7f49010d8cd=1541552836; JSESSIONID=1FEACCC545FC99619AAB2DA5915C9022.tomcat100',
        'X-Requested-With':'XMLHttpRequest',
        'User-Agent': choice(ua_list)
    }
    data={'phone':phone,'type':3}
    try:
        result = requests.post("http://www.ucpaas.com/checkcode/voiceExtCode", data=data, proxies=proxies, headers=headers)
    except requests.exceptions.ConnectionError:
        print(u"[%s]：发送失败 %s (剩余可用代理IP数：%s)" % ( date, result.text, len(ips)))
    else:
        print(u"[%s]：发送%s (剩余可用代理IP数：%s)" % ( date, result.text, len(ips)))

def postPhoneProxy2(phone):
    print("你所拨打的电话号码是："+phone)
    #requests.post("http://www.ucpaas.com/checkcode/voiceExtCode",data="",json="",proxies=proxies,headers=headers)
    date = datetime.datetime.now().strftime('%H:%M:%S')

    ips= com.whatime.utils.proxy.getPorxyFromUrl.getallproxy()
    ip = choice(ips)
    proxies = {
        'http': ip['IP地址']+":"+ip['端口号']
    }
    headers = {
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'Host':'www.ucpaas.com',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Origin': 'http://www.ucpaas.com',
        'Referer': 'http://www.ucpaas.com/experience',
        'Cookie': 'Hm_lvt_086fa6bc6f48b55eb534c7f49010d8cd=1541552820; c__utma=821849481.482618456.948871748.1541552820.1541552820.1; c__utmc=821849481.482618456; IESESSION=alive; 53revisit=1541552820818; 53kf_72170610_from_host=www.ucpaas.com; 53kf_72170610_keyword=; 53kf_72170610_land_page=http%253A%252F%252Fwww.ucpaas.com%252Fproduct%252Fvoice-code.html%253Bjsessionid%253D511DCC2C4C9653DC0EA5DE73C0C4A224.tomcat100; kf_72170610_land_page_ok=1; _qddaz=QD.gou8ax.sx4t0j.jo6gqxa0; _qdda=3-1.1; _qddab=3-7zb78q.jo6gqxa0; pgv_pvi=9893013504; pgv_si=s6329611264; _qddamta_4007776698=3-0; c__utmb=821849481.482618456.1541552820.1541552830.2; tencentSig=1829529600; Hm_lpvt_086fa6bc6f48b55eb534c7f49010d8cd=1541552836; JSESSIONID=1FEACCC545FC99619AAB2DA5915C9022.tomcat100',
        'X-Requested-With':'XMLHttpRequest',
        'User-Agent': choice(ua_list)
    }
    data={'phone':phone,'type':3}
    try:
        result = requests.post("http://www.ucpaas.com/checkcode/voiceExtCode", data=data, proxies=proxies, headers=headers)
    except requests.exceptions.ConnectionError:
        print(u"[%s]：发送失败 %s (剩余可用代理IP数：%s)" % ( date, result.text, len(ips)))
    else:
        print(u"[%s]：发送%s (剩余可用代理IP数：%s)" % ( date, result.text, len(ips)))

def main(phone):
    postPhoneProxy2(phone)

if __name__ == '__main__':
    main("18668966100");