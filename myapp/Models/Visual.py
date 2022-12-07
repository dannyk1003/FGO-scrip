import win32gui
import numpy as np
import time
import pyautogui
from PIL import Image, ImageQt
from PyQt6.QtWidgets import QApplication
import sys


class Visual:
    def __init__(self, hwnd, innerHwnd):
        self.path = sys.path[0]
        self.hwnd = hwnd
        self.innerHwnd = innerHwnd
        self.app = QApplication(sys.argv)


    def get_image(self):
        print('get_image')
        screen = self.app.primaryScreen()
        img = screen.grabWindow(self.innerHwnd).toImage()
        # print(type(img))
        # print(img)
        self.screenShot = ImageQt.fromqimage(img)
        return self.screenShot
    

    def get_900_506_image(self):
        self.get_image()
        while True:
            if self.SizeTest() != (900, 506):
                win32gui.MoveWindow(self.hwnd, True, True, 934, 540, True)
                time.sleep(0.5)
                self.get_image()
            else:
                break
        return self.screenShot


    def SizeTest(self):
        img = self.screenShot
        return img.size


    def locateOnImage(self, item):

        self.get_900_506_image()
        if pyautogui.locate(rf'{self.path}\img\{item}.png', self.screenShot, confidence=0.95) != None:
            x, y = pyautogui.center(pyautogui.locate(rf'{self.path}\img\{item}.png', self.screenShot, confidence=0.95))
            return [x, y]
        else:
            return None

    
    def WordToBlack(self, img):

        img = np.asarray(img)
        imgToBlack = np.array(img)

        for i in range(len(img)):
            for j in range(len(img[i])):
                if (img[i][j][0] == img[i][j][1]) & (img[i][j][1] == img[i][j][2]) & (img[i][j][0] >= 80):
                    imgToBlack[i][j][0] = 0
                    imgToBlack[i][j][1] = 0
                    imgToBlack[i][j][2] = 0
                else:
                    imgToBlack[i][j][0] = 255
                    imgToBlack[i][j][1] = 255
                    imgToBlack[i][j][2] = 255

        imgToBlack = Image.fromarray(imgToBlack)
        return imgToBlack
    
    
    def image_cut(self, img, x_start, y_start, x_end, y_end): # 620, 0, 633, 30 這個位置是battle幾
        new_img = img.crop((x_start, y_start, x_end, y_end))  # (left, upper, right, lower)
        return new_img
    

    