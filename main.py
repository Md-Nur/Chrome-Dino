import pyautogui
from PIL import Image, ImageGrab
import time
import datetime
# from numpy import asarray


a = datetime.datetime.now()

incre = 300

i = 0


def hit(key):
    pyautogui.keyDown(key)


def isObj(data):
    for x in range(200, int(incre)):
        for y in range(412, 475):
            if (i <= 700 or i >= 900) and data[x, y] < 100:
                return True
            elif (900 >= i >= 700) and data[x, y] > 100:
                return True
    return False


def snapShot():
    img = ImageGrab.grab().convert('L')
    return img


if __name__ == "__main__":
    print("The Dino game is start in 3 second...")
    time.sleep(3)
    hit('up')
    while True:
        img = snapShot()
        data = img.load()
        # print(asarray(img))
        if isObj(data):
            hit('up')
            print(i)
        b = datetime.datetime.now()
        c = b-a
        incre += ((c.microseconds/1000000000)/5)
        i += (c.microseconds/1000000)
        if(i > 900):
            i = 500
        # print(incre,i)
        # for x in range(250, 275):
        #     for y in range(412, 475):
        #         data[x, y] = 0

        # img.show()
        # break
