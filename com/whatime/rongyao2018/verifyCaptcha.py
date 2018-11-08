import requests

def verifyCaptcha(phone,pic_code,session):
    headers = {
        'Host' : 'rongyao2018.huobanys.com',
        'Connection' : 'keep-alive',
        'Content-Length' : '0',
        'Accept' : 'application/json, text/plain, */*',
        'Origin' : 'https://rongyao2018.huobanys.com',
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
        'Referer' : 'https://rongyao2018.huobanys.com/',
        'Accept-Encoding' : 'gzip, deflate, br',
        'Accept-Language' : 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cookie' : 'UM_distinctid=166eeb3e335a04-0de89b0de05dd5-b79193d-1fa400-166eeb3e336b6b; CNZZDATA1274785530=1838531496-1541599276-%7C1541599276; rongyao_session=FoWxt7hm23FaH7AuZWEbN4RyKFc7s3cYHRfQTGvl'
    }
    data = {"pic_code": pic_code,"phone_number": phone}
    url = 'https://rongyao2018.huobanys.com/api/doctor/userLogin'
    response = session.post(url,data=data,headers=headers)

    print("验证图形验证码："+response.text)

    return response