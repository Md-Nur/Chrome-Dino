# import pyautogui

# while True:
#     pyautogui.keyDown('n')
#     pyautogui.keyDown('u')
#     pyautogui.keyDown('r')

# import time
# print(time)

import datetime
a = datetime.datetime.now()
for i in range(20):
    print('khela')
b = datetime.datetime.now()
c = b - a

c
datetime.timedelta(0, 4, 316543)
print(c.days)
print(c.seconds)
print(c.microseconds/1000)