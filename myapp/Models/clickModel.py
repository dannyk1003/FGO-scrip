# 點擊做法
import win32api, win32gui, win32con, win32com.client
import numpy as np
import time
import pyautogui
from PIL import Image
import pytesseract
import json
from PyQt5.QtWidgets import QApplication
import sys


class Model:
    def __init__(self):
        self.times = 0
        self.window = 'BlueStacks App Player'
        self.innerWindow = 'Qt5154QWindowIcon'
        self.hwnd = ''
        self.innerHwnd = ''
        self.connect = ''
        self.history_title = list()

        self.battle1_clothes = [0, 0, 0]
        self.battle2_clothes = [0, 0, 0]
        self.battle3_clothes = [0, 0, 0]
        # self.battleSkill = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.battleSkill = {'b1cs1': None, 'b1p1s1': None, 'b1p2s1': None, 'b1p3s1': None, 
                            'b1cs2': None, 'b1p1s2': None, 'b1p2s2': None, 'b1p3s2': None, 
                            'b1cs3': None, 'b1p1s3': None, 'b1p2s3': None, 'b1p3s3': None,
                            'b2cs1': None, 'b2p1s1': None, 'b2p2s1': None, 'b2p3s1': None,
                            'b2cs2': None, 'b2p1s2': None, 'b2p2s2': None, 'b2p3s2': None,
                            'b2cs3': None, 'b2p1s3': None, 'b2p2s3': None, 'b2p3s3': None,
                            'b3cs1': None, 'b3p1s1': None, 'b3p2s1': None, 'b3p3s1': None,
                            'b3cs2': None, 'b3p1s2': None, 'b3p2s2': None, 'b3p3s2': None,
                            'b3cs3': None, 'b3p1s3': None, 'b3p2s3': None, 'b3p3s3': None,
                            }  
        



    def main(self):
        print('here is model')


    def times_counter(self, text):
        if text == '-5':
            self.times -= 5
        elif text == '-1':
            self.times -= 1
        elif text == '+1':
            self.times += 1
        elif text == '+5':
            self.times += 5

        
        if self.times <= 0:
            self.times = 0

        return self.times


    def get_window(self):
        self.hwnd = win32gui.FindWindow(None, self.window)

        if self.hwnd == 0:
            self.connect = 'Fail'

        else:

            def get_inner_windows(hwnd):
                def callback(hwnd, hwnds):
                    if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
                        hwnds[win32gui.GetClassName(hwnd)] = hwnd
                    return True
                hwnds_dict = dict()
                win32gui.EnumChildWindows(hwnd, callback, hwnds_dict)

                return hwnds_dict

            self.innerHwnd = get_inner_windows(self.hwnd)[self.innerWindow]
            print(self.hwnd, self.innerHwnd)
            self.connect = 'Success'
            self.position()
        
        return self.connect


    def start_scrip(self):
        pass


    def use_clothes_check(self, text, check):
        if check == 0:
            if text == 'A':
                self.battle1_clothes[0] = 0
            elif text == 'B':
                self.battle1_clothes[1] = 0
            elif text == 'C':
                self.battle1_clothes[2] = 0
        elif check == 1:
            if text == 'A':
                self.battle1_clothes[0] = 1
            elif text == 'B':
                self.battle1_clothes[1] = 1
            elif text == 'C':
                self.battle1_clothes[2] = 1            
        
        return self.battle1_clothes

    
    def battle(self, title, func, player, skill):
        k = ''
        if player == 'clothes':
            k = func[0] + func[-1] + player[0] + skill[0] + skill[-1]
        else:
            k = func[0] + func[-1] + player[0] + player[-1] + skill[0] + skill[-1]

        self.battleSkill[k] = title
        return self.battleSkill


    def doClick(self, position):
        x = position[0]
        y = position[1]
        hwnd = self.innerHwnd
        long_position = win32api.MAKELONG(int(x), int(y)) 
        win32gui.SendMessage(hwnd, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
        win32gui.PostMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, long_position)
        time.sleep(0.5)
        win32gui.SendMessage(hwnd, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
        win32gui.PostMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, long_position)


    def doDrag(self, position1, position2):
        x1, x2 = position1[0], position2[0]
        y1, y2 = position1[1], position2[1]
        hwnd = self.innerHwnd
        long_position1 = win32api.MAKELONG(int(x1), int(y1)) 
        long_position2 = win32api.MAKELONG(int(x2), int(y2)) 

        win32gui.PostMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, long_position1)
        time.sleep(2)
        win32gui.PostMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, long_position2)

    
    def runScrip(self):

        if self.connect == 'Success':
            shell = win32com.client.Dispatch("WScript.Shell")
            shell.SendKeys('%')
            hwnd = self.hwnd
            innerHwnd = self.innerHwnd
            win32gui.SetForegroundWindow(hwnd)
            win32gui.MoveWindow(innerHwnd, 0, 0, 1000, 600, True)
            time.sleep(2)


            while self.times > 0:
                print(self.times)

                self.startBattle(1)
                time.sleep(20)
                while True:
                    battle1Img = pyautogui.locateOnScreen(r'img\Battle1-3.png', confidence=0.9)
                    if battle1Img == None:
                        print('next')
                        break
                    self.useAttack()
                    time.sleep(20)
                
                self.startBattle(2)
                time.sleep(20)

                while True:
                    battle2Img = pyautogui.locateOnScreen(r'img\Battle2-3.png', confidence=0.9)
                    if battle2Img == None:
                        print('next')
                        break
                    self.useAttack()
                    time.sleep(20)

                self.startBattle(3)
                time.sleep(20)

                while True:
                    battle3Img = pyautogui.locateOnScreen(r'img\Battle3-3.png', confidence=0.9)
                    if battle3Img == None:
                        print('next')
                        break
                    self.useAttack()
                    time.sleep(20)

                with_servent_connect = pyautogui.locateOnScreen(r'img\with_servent_connect.png', confidence=0.95)
                while with_servent_connect != None:
                    self.doClick(self.middle)
                    time.sleep(5)
                    with_servent_connect = pyautogui.locateOnScreen(r'img\with_servent_connect.png', confidence=0.95)
                
                masterEXP = pyautogui.locateOnScreen(r'img\masterEXP.png', confidence=0.95)
                while masterEXP != None:
                    self.doClick(self.middle)
                    time.sleep(5)
                    masterEXP = pyautogui.locateOnScreen(r'img\masterEXP.png', confidence=0.95)
                
                click_to_see_result = pyautogui.locateOnScreen(r'img\click_to_see_result.png', confidence=0.95)
                while click_to_see_result != None:
                    self.doClick(self.next)
                    time.sleep(5)
                    click_to_see_result = pyautogui.locateOnScreen(r'img\click_to_see_result.png', confidence=0.95)

                self.times -= 1
                if self.times > 0:
                    go_again = pyautogui.locateOnScreen(r'img\go_again.png', confidence=0.95)
                    if go_again != None:
                        go_again_x = pyautogui.center(go_again)[0] - win32gui.GetWindowRect(self.innerHwnd)[0]
                        go_again_y = pyautogui.center(go_again)[1] - win32gui.GetWindowRect(self.innerHwnd)[1]
                        go_again_position = [go_again_x, go_again_y]
                        self.doClick(go_again_position)
                
                    time.sleep(10)
                    
                    support = pyautogui.locateOnScreen(r'img\Scathach.png', confidence=0.95)
                    while support == None:
                        go_down = pyautogui.locateOnScreen(r'img\go_down.png', confidence=0.95)
                        go_down_x = pyautogui.center(go_down)[0] - win32gui.GetWindowRect(self.innerHwnd)[0]
                        go_down_y = pyautogui.center(go_down)[1] - win32gui.GetWindowRect(self.innerHwnd)[1]
                        go_down_position = [go_down_x, go_down_y]
                        self.doClick(go_down_position)
                        time.sleep(2)
                        support = pyautogui.locateOnScreen(r'img\Scathach.png', confidence=0.95)

                    support_x = pyautogui.center(support)[0] - win32gui.GetWindowRect(self.innerHwnd)[0]
                    support_y = pyautogui.center(support)[1] - win32gui.GetWindowRect(self.innerHwnd)[1]
                    support_position = [support_x, support_y]
                    self.doClick(support_position)
                    time.sleep(5)

                    time.sleep(10)
                    
                    
                
                







    def position(self):
        x = win32gui.GetWindowRect(self.innerHwnd)[0]
        y = win32gui.GetWindowRect(self.innerHwnd)[1]
        x_long = win32gui.GetWindowRect(self.innerHwnd)[2] - win32gui.GetWindowRect(self.innerHwnd)[0]
        y_long = win32gui.GetWindowRect(self.innerHwnd)[3] - win32gui.GetWindowRect(self.innerHwnd)[1]


        self.playerSkill = {'p1s1': [x_long * 0.055, y_long * 0.8], 'p1s2': [x_long * 0.125, y_long * 0.8], 'p1s3': [x_long * 0.195, y_long * 0.8],
                            'p2s1': [x_long * 0.305, y_long * 0.8], 'p2s2': [x_long * 0.375, y_long * 0.8], 'p2s3': [x_long * 0.445, y_long * 0.8],
                            'p3s1': [x_long * 0.555, y_long * 0.8], 'p3s2': [x_long * 0.625, y_long * 0.8], 'p3s3': [x_long * 0.695, y_long * 0.8]}

        self.attack = [x_long * 0.89, y_long * 0.8]
        self.clothes = [x_long * 0.935, y_long * 0.425]

        self.toPlayer = {'player1': [x_long * 0.265, y_long * 0.655],'player2': [x_long * 0.5, y_long * 0.655],'player3': [x_long * 0.735, y_long * 0.655]}
        self.clothesSkill = [[x_long * 0.705, y_long * 0.425], [x_long * 0.775, y_long * 0.425], [x_long * 845, y_long * 0.425]]
        self.big = [[x_long * 0.325, y_long * 0.32], [x_long * 0.5, y_long * 0.32], [x_long * 0.675, y_long * 0.32]]
        self.small = [[x_long * 0.1, y_long * 0.743], [x_long * 0.3, y_long * 0.743], [x_long * 0.5, y_long * 0.743], [x_long * 0.7, y_long * 0.743], [x_long * 0.9, y_long * 0.743]]
        self.middle = [x_long * 0.5, y_long * 0.5]
        self.next = [x_long * 0.87, y_long * 0.895]

    def startBattle(self, n): # battle n
        # player1 = self.toPlayer[0]
        # player2 = self.toPlayer[1]
        # player3 = self.toPlayer[2]
        # if self.battleSkill['b1cs1'] != None:
        #     self.useClothes(1,self.battleSkill['b1cs1'])
        # if self.battleSkill['b1cs2'] != None:
        #     self.useClothes(1,self.battleSkill['b1cs2'])
        # if self.battleSkill['b1cs3'] != None:
        #     self.useClothes(1,self.battleSkill['b1cs3'])
        
        self.position()
        self.useClothes(1, self.battleSkill['b' + str(n) + 'cs1'])
        self.useClothes(2, self.battleSkill['b' + str(n) + 'cs2'])
        self.useClothes(3, self.battleSkill['b' + str(n) + 'cs3'])
        # self.useSkill(1, 1, self.battleSkill['b1p1s1'])
        # self.useSkill(1, 2, self.battleSkill['b1p1s2'])
        # self.useSkill(1, 3, self.battleSkill['b1p1s3'])

        time.sleep(4)
        for i in range(1, 4, 1):
            for j in range(1, 4, 1):
                p = 'b' + str(n) + 'p' + str(i) + 's' + str(j)
                self.useSkill(i, j, self.battleSkill[p])

        time.sleep(2)
        
        self.useAttack()




    def useClothes(self, n, m): # 第n個clothes技能, 給player m
        if m == None:
            print('None')
        else:
            # clothes = [950, 250]
            clothes = self.locateOnImage('clothes', 'FGO_ScreenShot')
            if clothes != None:
                self.doClick(clothes)
                time.sleep(2)
                self.doClick(self.clothesSkill[n-1])
                time.sleep(2)
                self.doClick(self.toPlayer[m])
                time.sleep(2)


    def useSkill(self, p, n, m): # player p 的第n個技能, 給player m
        if m == None:
            pass
        else:
            player = 'p' + str(p) + 's' + str(n)
            self.doClick(self.playerSkill[player])
            time.sleep(4)
            # img = pyautogui.locateOnScreen(r'img\Please_select_object.png')
            img = self.locateOnImage('Please_select_object', 'FGO_ScreenShot')
            if img != None:
                self.doClick(self.toPlayer[m])
            time.sleep(4)

    def useAttack(self):
        self.position()

        self.doClick(self.attack)
        time.sleep(2)
        
        for i in range(3):
            self.doClick(self.big[i])
            time.sleep(2)

        for j in range(3):
            self.doClick(self.small[j])
            time.sleep(2)


    def write_history(self, title):
        with open(rf'history\{title}.json','w') as fw:
            json.dump(self.battleSkill,fw)
    

    def read_history(self, text):
        with open(rf'history\{text}.json','r') as fr:
            self.battleSkill = json.load(fr)
        print(self.battleSkill)
        

    def get_image(self, text):
        app = QApplication(sys.argv)
        screen = QApplication.primaryScreen()
        img = screen.grabWindow(self.innerHwnd).toImage()
        img.save(rf'img\screenShot\{text}.png')

    
    def locateOnImage(self, item, image):
        self.get_image(image)
        if pyautogui.locate(rf'img\{item}.png', rf'img\screenShot\{image}.png', confidence=0.95) != None:
            x = pyautogui.locate(rf'img\{item}.png', rf'img\screenShot\{image}.png', confidence=0.95)[0]
            y = pyautogui.locate(rf'img\{item}.png', rf'img\screenShot\{image}.png', confidence=0.95)[1]
            return [x, y]
        else:
            return None





