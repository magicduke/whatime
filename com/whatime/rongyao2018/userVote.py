import requests

def vote(candidate_id,award_id,session):
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
    data = {"candidate_id": candidate_id,"award_id":award_id}
    url = 'https://rongyao2018.huobanys.com/api/vote/userVote'
    response = session.post(url,data=data,headers=headers)

    if "200" == response.json()["status"]:
        print("投票成功："+response.json()["data"])  #a2bb978218b6dab74bb1d019790fdecf
    else:
        print("投票失败："+response.text)

    return response