import requests

def getXiGuaProxy(orderId,num,filter):
    filterStr = ''
    numStr = ''
    if filter == True:
        filterStr = '&filter=on'
    else:
        filterStr = ''

    if num >= 1:
        numStr = '&num='+str(num)
    else:
        numStr = ''
    url = 'http://api3.xiguadaili.com/ip/?tid='+str(orderId)+numStr+filterStr
    r = requests.get(url)
    ips = r.text
    ipsArr = ips.splitlines()

    return ipsArr

def main():
    ips = []
    ips.extend(getXiGuaProxy(559234731394746, 10, True))
    print(ips)

if __name__ == '__main__':
    main();