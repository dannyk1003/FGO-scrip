from time import time
import win32gui, win32con, win32api, win32ui
from win32clipboard import *
import time
import cv2

wdname = '小算盤'
handle = win32gui.FindWindow(None, wdname)
handleX = win32gui.FindWindowEx(handle, None, 'ApplicationFrameWindow', None)
# 視窗控制碼
print('handle:', handle)
print('handleX:', handleX)

click = win32api.MAKELONG(54, 467)
win32gui.SendMessage(handleX, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, click)
time.sleep(0.1)
win32gui.SendMessage(handleX, win32con.WM_LBUTTONUP, None, click)


left, top, right, bottom = win32gui.GetWindowRect(handle)
# 視窗位置
print(left, top, right, bottom)

tempt = win32api.GetCursorPos()
print('tempt',tempt)

windowRec = win32gui.GetWindowRect(handle)
print('windowRec', windowRec)

x = tempt[0] - windowRec[0]
y = tempt[1] - windowRec[1]
print('坐标为', x, y)

title = win32gui.GetWindowText(handle)
# 視窗名稱

clsname = win32gui.GetClassName(handle)
# 視窗類型

print(handle, title, clsname)

windowRec = win32gui.GetWindowRect(handle)


def doClick(cx, cy):
    long_position = win32api.MAKELONG(cx, cy)
    print(long_position)
    print('handle', handle)
    hWnd= win32gui.FindWindowEx(handle, None, None, None)
    win32api.SendMessage(handle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, long_position)
    win32api.SendMessage(handle, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, long_position)


doClick(54, 467)


