# -*- coding: utf-8 -*-
# python3.5

# 易码短信服务平台开放接口范例代码
# 语言版本：python版
# 官方网址：www.51ym.me
# 技术支持QQ：2114927217
# 发布时间：217-12-11

from urllib import parse, request
import time
import re

header_dict = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}

def getToken(username,password):
# 登陆/获取TOKEN
#username = 'ma********ke'  # 账号
#password = 'L**********8123'  # 密码
    url =  'http://api.fxhyd.cn/UserInterface.aspx?action=login&username=' + \
        username+'&password='+password
    TOKEN1 = request.urlopen(request.Request(url=url, headers=header_dict)).read().decode(encoding='utf-8')

    if TOKEN1.split('|')[0] == 'success':
        TOKEN = TOKEN1.split('|')[1]
        print('TOKEN是'+TOKEN)
        return TOKEN,True
    else:
        print('获取TOKEN错误,错误代码'+TOKEN1+'。代码释义：1001:参数token不能为空;1002:参数action不能为空;1003:参数action错误;1004:token失效;1005:用户名或密码错误;1006:用户名不能为空;1007:密码不能为空;1008:账户余额不足;1009:账户被禁用;1010:参数错误;1011:账户待审核;1012:登录数达到上限')

        return '获取TOKEN错误,错误代码'+TOKEN1+'。代码释义：1001:参数token不能为空;1002:参数action不能为空;1003:参数action错误;1004:token失效;1005:用户名或密码错误;1006:用户名不能为空;1007:密码不能为空;1008:账户余额不足;1009:账户被禁用;1010:参数错误;1011:账户待审核;1012:登录数达到上限',False



TOKEN = '0071210**********250401'  # 输入TOKEN

def getAccount(token):
    # 获取账户信息
    url = 'http://api.fxhyd.cn/UserInterface.aspx?action=getaccountinfo&token='+token+'&format=1'
    ACCOUNT1 = request.urlopen(request.Request(
        url=url, headers=header_dict)).read().decode(encoding='utf-8')
    if ACCOUNT1.split('|')[0] == 'success':
        ACCOUNT = ACCOUNT1.split('|')[1]
        print(ACCOUNT)
        return ACCOUNT,True
    else:
        print('获取TOKEN错误,错误代码'+ACCOUNT1)
        return '获取TOKEN错误,错误代码'+ACCOUNT1,False


ITEMID = '11938'  # 项目编号
EXCLUDENO = ''  # 排除号段170_171

def getPhoneNum(token,itemid,excludeno):
    # 获取手机号码
    url = 'http://api.fxhyd.cn/UserInterface.aspx?action=getmobile&token=' + \
          token+'&itemid='+itemid+'&excludeno='+excludeno
    MOBILE1 = request.urlopen(request.Request(
        url=url, headers=header_dict)).read().decode(encoding='utf-8')
    if MOBILE1.split('|')[0] == 'success':
        MOBILE = MOBILE1.split('|')[1]
        print('获取号码是:\n'+MOBILE)
        return MOBILE,True
    else:
        print('获取TOKEN错误,错误代码'+MOBILE1)
        return '获取TOKEN错误,错误代码'+MOBILE1,False

def getCodeSMS(TOKEN,ITEMID,MOBILE,WAIT=60):
    # 获取短信，注意线程挂起5秒钟，每次取短信最少间隔5秒
    #TOKEN = TOKEN  # TOKEN
    #ITEMID = ITEMID  # 项目id
    #MOBILE = MOBILE  # 手机号码
    #WAIT = 100  # 接受短信时长60s
    url = 'http://api.fxhyd.cn/UserInterface.aspx?action=getsms&token=' + \
        TOKEN+'&itemid='+ITEMID+'&mobile='+MOBILE+'&release=1'
    text1 = request.urlopen(request.Request(
        url=url, headers=header_dict)).read().decode(encoding='utf-8')
    TIME1 = time.time()
    TIME2 = time.time()
    ROUND = 1
    while (TIME2-TIME1) < WAIT and not text1.split('|')[0] == "success":
        time.sleep(5)
        text1 = request.urlopen(request.Request(
            url=url, headers=header_dict)).read().decode(encoding='utf-8')
        TIME2 = time.time()
        ROUND = ROUND+1

    ROUND = str(ROUND)
    if text1.split('|')[0] == "success":
        text = text1.split('|')[1]
        TIME = str(round(TIME2-TIME1, 1))
        print('短信内容是'+text+'\n耗费时长'+TIME+'s,循环数是'+ROUND)
        return text,True
    else:
        print('获取短信超时，错误代码是'+text1+',循环数是'+ROUND)
        return '获取短信超时，错误代码是'+text1,False

def releasePhoneNUm(TOKEN,ITEMID,MOBILE):
    # 释放号码
    url = 'http://api.fxhyd.cn/UserInterface.aspx?action=release&token=' + \
        TOKEN+'&itemid='+ITEMID+'&mobile='+MOBILE
    RELEASE = request.urlopen(request.Request(
        url=url, headers=header_dict)).read().decode(encoding='utf-8')
    if RELEASE == 'success':
        print('号码成功释放')
    return

def getNumCode(text):
    # 提取短信内容中的数字验证码
    pat = "[0-9]+"
    IC = 0
    IC = re.search(pat, text)
    if IC:
        print("验证码是:\n"+IC.group())
        return IC.group(),True
    else:
        print("请重新设置表达式")
        return "请重新设置表达式",False


def main(token,itemid,excludeno):
    phoneNum,phoneNumStatus = getPhoneNum(token,itemid,excludeno)
    if phoneNumStatus == True :
        print("手机号码是："+phoneNum)
        smsText,smsTextStatus = getCodeSMS(TOKEN=token,ITEMID=itemid,MOBILE=phoneNum,WAIT=100)
        if smsTextStatus == True:
            print("手机短信是："+smsText)
            code,codeStatus = getNumCode(smsText)
            print("验证码是："+code)
            releasePhoneNUm(TOKEN=token,ITEMID=itemid,MOBILE=phoneNum)
        else:
            print("手机短信获取失败："+smsText)
            releasePhoneNUm(TOKEN=token,ITEMID=itemid,MOBILE=phoneNum)

    else:
        print("手机号码获取失败："+phoneNum)
    return

if __name__ == '__main__':
    #项目ID 2542 为启信宝登陆短信验证项目ID
    main(token="00712107f9b0327557c681c9e6f8c2ed1547d0250401",itemid="2542",excludeno="171.172.174.177")