import requests
import re
import base64
from io import BytesIO
from PIL import Image


def base64ToImg(base64_str):
    base64_data = re.sub('^data:image/.+;base64,', '', base64_str)
    byte_data = base64.b64decode(base64_data)
    image_data = BytesIO(byte_data)
    img = Image.open(image_data)
    img.show()


def getCaptcha(session):
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
    data = {}
    url = 'https://rongyao2018.huobanys.com/api/doctor/showCaptcha'
    response = session.post(url,data=data,headers=headers)

    print("图形Base64编码为："+response.text)
    return response.text


def main():
    s = requests.session()
    captchaBase64 = getCaptcha(s)
    base64ToImg(captchaBase64)
    pic_code = input("请输入验证码:")
    print("图形验证码为:"+pic_code)


if __name__ == '__main__':
    main()