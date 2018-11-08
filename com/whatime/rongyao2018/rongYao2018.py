#http://rongyao2018.huobanys.com
import requests
from com.whatime.rongyao2018 import showCaptcha
from com.whatime.rongyao2018 import verifyCaptcha

def getPicCode(session):
    captchaBase64 = showCaptcha.getCaptcha(session)
    showCaptcha.base64ToImg(captchaBase64)
    pic_code = input("请输入验证码:")
    print("图形验证码为:"+pic_code)
    return pic_code


def getIndex(session):
    headers = {
        'Host' : 'rongyao2018.huobanys.com',
        'Connection' : 'keep-alive',
        'Content-Length' : '0',
        'Accept' : 'application/json, text/plain, */*',
        'Origin' : 'https://rongyao2018.huobanys.com',
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
        'Referer' : 'https://rongyao2018.huobanys.com/',
        'Accept-Encoding' : 'gzip, deflate, br',
        'Accept-Language' : 'zh-CN,zh;q=0.9,en;q=0.8'
    }
    data = {"id": "107"}
    url = 'https://rongyao2018.huobanys.com/api/vote/signUpInfoDetail'
    response = session.post(url,data=data,headers=headers)

    #print("rongyao_session:"+session.cookies.keys())
    #print("rongyao_session:"+response.headers)

    return response


def main(phone):
    s = requests.session()
    getIndex(s)
    while True:
        pic_code = getPicCode(s)
        verifyResponse = verifyCaptcha.verifyCaptcha(phone,pic_code,s)
        verifyStatus = verifyResponse.json()[u'status']
        if "200" == verifyStatus:
            break


    return


if __name__ == '__main__':
    main("18668966100")