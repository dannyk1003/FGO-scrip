import win32gui
title = dict()

def get_all_title(hwnd, mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        title.update({hwnd:win32gui.GetWindowText(hwnd)})
mouse = 0
win32gui.EnumWindows(get_all_title,mouse)

for hwnd, title in title.items():
    if title != "":
        print(hwnd, title)


from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import *
import sys

def get_key(dict, value):
    keys = []
    for k, v in dict.items():
        if v == value:
            keys.append(k)
        return keys

hwnd = get_key(title, "123")[0]
app = QApplication(sys.argv)
screen = QApplication.primaryScreen()
img = screen.grabWindow(hwnd).toImage()
img.save("screenshot.jpg")
print(hwnd)
