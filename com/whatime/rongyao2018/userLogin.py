import requests

def login(phone,pic_code,smsCode,session):
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
    data = {"pic_code": pic_code,"sms_code":smsCode,"phone_number": phone}
    url = 'https://rongyao2018.huobanys.com/api/doctor/userLogin'
    response = session.post(url,data=data,headers=headers)

    if "200" == response.json()["status"]:
        requests.utils.add_dict_to_cookiejar(session.cookies, response.json()["data"])#将返回信息的User_token和type加入到session的Cookies中
        print("登陆成功："+response.json()["data"])  #a2bb978218b6dab74bb1d019790fdecf
    else:
        print("登陆失败："+response.text)

    return response