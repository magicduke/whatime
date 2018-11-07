import time
from com.whatime.utils.phone.voiceCallFree import postPhone

def test10Time30sec():
    i = 0
    while i < 10:
        print("拨打第"+str(i)+"次：")
        postPhone("18668966100")
        time.sleep(30)
        i = i+1

def main():
    test10Time30sec()

if __name__ == '__main__':
    main();