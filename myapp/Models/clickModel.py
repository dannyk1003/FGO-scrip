# 點擊做法
import win32api, win32gui, win32con, win32com.client
import numpy as np
import time
import pyautogui
from PIL import Image, ImageQt
from PyQt5.QtWidgets import QApplication
import sys
import cv2
import pythoncom
from Models.Visual import Visual


class clickModel:
    def __init__(self):
        self.path = sys.path[0]

        self.times = 0
        self.window = 'BlueStacks App Player'
        self.innerWindow = 'Qt5154QWindowIcon'
        self.hwnd = ''
        self.innerHwnd = ''
        self.connect = ''
        

        self.battleSkill = {'b1p0s1': None, 'b1p1s1': None, 'b1p2s1': None, 'b1p3s1': None, 
                            'b1p0s2': None, 'b1p1s2': None, 'b1p2s2': None, 'b1p3s2': None, 
                            'b1p0s3': None, 'b1p1s3': None, 'b1p2s3': None, 'b1p3s3': None,
                            'b2p0s1': None, 'b2p1s1': None, 'b2p2s1': None, 'b2p3s1': None,
                            'b2p0s2': None, 'b2p1s2': None, 'b2p2s2': None, 'b2p3s2': None,
                            'b2p0s3': None, 'b2p1s3': None, 'b2p2s3': None, 'b2p3s3': None,
                            'b3p0s1': None, 'b3p1s1': None, 'b3p2s1': None, 'b3p3s1': None,
                            'b3p0s2': None, 'b3p1s2': None, 'b3p2s2': None, 'b3p3s2': None,
                            'b3p0s3': None, 'b3p1s3': None, 'b3p2s3': None, 'b3p3s3': None,
                            }
        self.apple = ''


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

            self.Visual = Visual(self.hwnd, self.innerHwnd)

            self.connect = 'Success'
            self.position()
        
        return self.connect


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
        time.sleep(0.5)

   
    def window_to_front(self):
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.SendKeys('%')
        win32gui.SetForegroundWindow(self.hwnd)


    def runScrip(self, now_status_support, now_status_skill):
        pythoncom.CoInitialize()
        self.supporter = now_status_support
        self.battleSkill = now_status_skill
        self.times = 1

        # while True:
        #     time.sleep(1)
        #     print('on going')

        if self.connect == 'Success': # 連線成功

            self.window_to_front()

            # self.doClick(self.mission)
            # time.sleep(1)
            # for times in range(self.times): # 次數大於一次時
            self.go_again()

            # print('剩餘次數', self.times)
            # print('第', times, '次')

            self.AP_recovery()

            self.select_support()


            for i in range(1, 4):
                self.startBattle(i)
                
            print('battle end')
            
            # self.go_again()
            # self.times -= 1            

            print('success')


    def position(self):
        x = win32gui.GetWindowRect(self.innerHwnd)[0]
        y = win32gui.GetWindowRect(self.innerHwnd)[1]
        x_long = win32gui.GetWindowRect(self.innerHwnd)[2] - win32gui.GetWindowRect(self.innerHwnd)[0]
        y_long = win32gui.GetWindowRect(self.innerHwnd)[3] - win32gui.GetWindowRect(self.innerHwnd)[1]


        self.playerSkill = {'p0s1': [x_long * 0.705, y_long * 0.425], 'p0s2':[x_long * 0.775, y_long * 0.425], 'p0s3': [x_long * 0.845, y_long * 0.425],
                            'p1s1': [x_long * 0.055, y_long * 0.8], 'p1s2': [x_long * 0.125, y_long * 0.8], 'p1s3': [x_long * 0.195, y_long * 0.8],
                            'p2s1': [x_long * 0.305, y_long * 0.8], 'p2s2': [x_long * 0.375, y_long * 0.8], 'p2s3': [x_long * 0.445, y_long * 0.8],
                            'p3s1': [x_long * 0.555, y_long * 0.8], 'p3s2': [x_long * 0.625, y_long * 0.8], 'p3s3': [x_long * 0.695, y_long * 0.8]}

        self.attack = [x_long * 0.89, y_long * 0.8]
        self.clothes = [x_long * 0.935, y_long * 0.425]

        self.toPlayer = {'player1': [x_long * 0.265, y_long * 0.655],'player2': [x_long * 0.5, y_long * 0.655],'player3': [x_long * 0.735, y_long * 0.655]}
        self.clothesSkill = [[x_long * 0.705, y_long * 0.425], [x_long * 0.775, y_long * 0.425], [x_long * 0.845, y_long * 0.425]]
        self.big = [[x_long * 0.325, y_long * 0.32], [x_long * 0.5, y_long * 0.32], [x_long * 0.675, y_long * 0.32]]
        self.small = [[x_long * 0.1, y_long * 0.743], [x_long * 0.3, y_long * 0.743], [x_long * 0.5, y_long * 0.743], [x_long * 0.7, y_long * 0.743], [x_long * 0.9, y_long * 0.743]]
        self.middle = [x_long * 0.5, y_long * 0.5]
        self.next = [x_long * 0.87, y_long * 0.895]
        self.mission = [x_long * 0.7, y_long * 0.26]


    def startBattle(self, n): # battle n
        self.main_screen()
        
        print('now is battle', n)
        self.position()

        while True:
            battle_count_position = self.CheckBattleCount(n)
            print(battle_count_position)

            if battle_count_position == None:
                break

            else:
                for i in range(4):
                    for j in range(1, 4, 1):
                        p = 'b' + str(n) + 'p' + str(i) + 's' + str(j)
                        print(p)
                        self.useSkill(i, j, self.battleSkill[p])


                while True:
                    self.main_screen()
                    self.useAttack()
                    self.main_screen()
                    battle_count_position = self.CheckBattleCount(n)
                    # with_servent_connect_position = self.locateOnImage('with_servent_connect', 'FGO_ScreenShot')

                    with_servent_connect_position = self.Visual.locateOnImage('with_servent_connect')

                    if battle_count_position == None:
                        break
                    elif with_servent_connect_position != None:
                        break
                break
            

        print('battle ', n, ' end')


    def main_screen(self):
        # clothes_position = self.locateOnImage('clothes', 'ScreenShot')
        # with_servent_connect_position = self.locateOnImage('with_servent_connect', 'FGO_ScreenShot')
        clothes_position = self.Visual.locateOnImage('clothes')
        with_servent_connect_position = self.Visual.locateOnImage('with_servent_connect')

        while True:
            if clothes_position != None:
                break
            elif with_servent_connect_position != None:
                break
            else:
                time.sleep(5)
                # clothes_position = self.locateOnImage('clothes', 'ScreenShot')
                # with_servent_connect_position = self.locateOnImage('with_servent_connect', 'FGO_ScreenShot')
                clothes_position = self.Visual.locateOnImage('clothes')
                with_servent_connect_position = self.Visual.locateOnImage('with_servent_connect')


    def useSkill(self, p, n, m): # player p 的第n個技能, 給player m
        if m != None:
            player = 'p' + str(p) + 's' + str(n)
            print(player)
            if p == 0:
                self.doClick(self.clothes)
                time.sleep(1)
            
            self.doClick(self.playerSkill[player])
            time.sleep(4)
            # img = pyautogui.locateOnScreen(r'img\Please_select_object.png')

            if self.skill_used_check() != None:
                self.doClick(self.skill_used_check())
                time.sleep(2)
                if p == 0:
                    self.doClick(self.clothes)
                    time.sleep(1)
            else:
                # img = self.locateOnImage('Please_select_object', 'FGO_ScreenShot')
                img = self.Visual.locateOnImage('Please_select_object')
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
        
        time.sleep(20)

    
    def CheckBattleCount(self, count):
        # win32gui.MoveWindow(self.hwnd, True, True, 960, 540, True)
        # time.sleep(0.5)

        # Now = self.get_image('Now')
        # Now = self.get_900_506_image('Now')
        # Now_cut = rf'{self.path}\img\screenShot\Now_cut_{count}.png'
        # Now_cut_black = rf'{self.path}\img\screenShot\Now_cut_{count}_black.png'
        # BattleCount = rf'{self.path}\img\BattleCount\Battle{count}.png'
        # self.image_cut(Now, Now_cut, 620, 0, 633, 30)
        # self.WordToBlack(Now_cut, Now_cut_black)

        Now = self.Visual.get_900_506_image()
        Now_cut = self.Visual.image_cut(Now, 620, 0, 633, 30)
        Now_cut_black = self.Visual.WordToBlack(Now_cut)
        BattleCount = rf'{self.path}\img\BattleCount\Battle{count}.png'


        if pyautogui.locate(Now_cut_black, BattleCount, confidence=0.8) != None :

            x = pyautogui.locate(Now_cut_black, BattleCount, confidence=0.8)[0]
            y = pyautogui.locate(Now_cut_black, BattleCount, confidence=0.8)[1]
            return [x, y]
        else:
            return None
        

    def skill_used_check(self):
        # Now = self.get_image('Now')
        # Now = self.get_900_506_image('Now')
        # cancel = rf'{self.path}\img\cancel.png'

        Now = self.Visual.get_900_506_image()
        cancel = rf'{self.path}\img\cancel.png'

        if pyautogui.locate(cancel, Now, confidence=0.8) != None :
            print(pyautogui.locate(cancel, Now, confidence=0.8))
            x = pyautogui.locate(cancel, Now, confidence=0.8)[0]
            y = pyautogui.locate(cancel, Now, confidence=0.8)[1]
            return [x, y]
        else:
            return None

    
    def select_support(self):
        while True:
            time.sleep(2)
            # support_choose_position = self.locateOnImage(rf"\Support\support_choose", 'ScreenShot')

            support_choose_position = self.Visual.locateOnImage(rf"\Support\support_choose")

            if support_choose_position != None:
                break

        # support_type_location = self.locateOnImage(rf"\Support\{self.supporter['type']}", 'ScreenShot')
            
        support_type_location = self.Visual.locateOnImage(rf"\Support\{self.supporter['type']}")

        self.doClick(support_type_location)

        # supporter_location = self.locateOnImage(rf"\Support\{self.supporter['type']}\{self.supporter['supporter']}", 'ScreenShot')

        supporter_location = self.Visual.locateOnImage(rf"\Support\{self.supporter['type']}\{self.supporter['supporter']}")

        print(supporter_location)

        if supporter_location != None:
            time.sleep(1)
            self.doClick(supporter_location)
        else:
            i = 0
            while i != 10:
                i += 1
                # go_down_location = self.locateOnImage(rf"\Support\go_down", 'ScreenShot')

                go_down_location = self.Visual.locateOnImage(rf"\Support\go_down")

                if go_down_location == None:
                    # re_new_list_location = self.locateOnImage(rf"\Support\re_new_list", 'ScreenShot')

                    re_new_list_location = self.Visual.locateOnImage(rf"\Support\re_new_list")

                    self.doClick(re_new_list_location)
                    time.sleep(1)
                    # yes_location = self.locateOnImage(rf"\Support\yes", 'ScreenShot')

                    yes_location = self.Visual.locateOnImage(rf"\Support\yes")

                    self.doClick(yes_location)
                    time.sleep(1)
                    i = 0
                else:
                    self.doClick(go_down_location)
                    time.sleep(1)
                
                # supporter_location = self.locateOnImage(rf"\Support\{self.supporter['type']}\{self.supporter['supporter']}", 'ScreenShot')

                supporter_location = self.Visual.locateOnImage(rf"\Support\{self.supporter['type']}\{self.supporter['supporter']}")

                if supporter_location != None:
                    time.sleep(1)
                    self.doClick(supporter_location)
                    break
        time.sleep(1)
        # mission_start_position = self.locateOnImage(rf"\Support\mission_start", 'ScreenShot')

        mission_start_position = self.Visual.locateOnImage(rf"\Support\mission_start")

        while True:

            if mission_start_position != None:
                self.doClick(mission_start_position)
                break
            else:
                time.sleep(0.5)
                mission_start_position = self.Visual.locateOnImage(rf"\Support\mission_start")
        
        print('select end')


    def go_again(self):
        while True:
            # go_again_position = self.locateOnImage(rf"go_again", 'ScreenShot')
            # close_position = self.locateOnImage(rf"close", 'ScreenShot')

            go_again_position = self.Visual.locateOnImage(rf"go_again")
            close_position = self.Visual.locateOnImage(rf"close")

            if go_again_position == None:
                if close_position == None:
                    self.doClick(self.next)
                    time.sleep(0.5)
                else:
                    # last_time_position = self.locateOnImage(rf"last_time", 'ScreenShot')

                    last_time_position = self.Visual.locateOnImage(rf"last_time")

                    if last_time_position == None:
                        self.doClick(self.mission)
                        break
                    else:
                        self.doClick(last_time_position)
                        break
            else:
                self.doClick(go_again_position)
                break


    def AP_recovery(self):
        self.apple = 'bronze'
        # gold_position = self.locateOnImage(rf"\AP_Recovery\gold", 'ScreenShot')

        gold_position = self.Visual.locateOnImage(rf"\AP_Recovery\gold")

        if gold_position != None:
            while True:
                # apple_position = self.locateOnImage(rf"\AP_Recovery\{self.apple}", 'ScreenShot')

                apple_position = self.Visual.locateOnImage(rf"\AP_Recovery\{self.apple}")

                if apple_position != None:
                    self.doClick(apple_position)
                    time.sleep(1)
                    # sure_position = self.locateOnImage(rf"\AP_Recovery\sure", 'ScreenShot')

                    sure_position = self.Visual.locateOnImage(rf"\AP_Recovery\sure")

                    self.doClick(sure_position)
                    break
                else:
                    # go_down_position = self.locateOnImage(rf"\AP_Recovery\go_down", 'ScreenShot')

                    go_down_position = self.Visual.locateOnImage(rf"\AP_Recovery\go_down")

                    self.doClick(go_down_position)
                    time.sleep(1)


'''

    def WordToBlack(self, before, after):
        img = cv2.imread(before)

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

        cv2.imwrite(after, imgToBlack)


    def image_cut(self, before, after, x_start, y_start, x_end, y_end): # 620, 0, 633, 30 這個位置是battle幾
        img = Image.open(before)
        new_img = img.crop((x_start, y_start, x_end, y_end))  # (left, upper, right, lower)
        new_img.save(after)


    def SizeTest(self, text):
        img = Image.open(rf'{self.path}\img\screenShot\{text}.png')
        # img = self.screenShot
        return img.size


    def get_image(self, text):
        app = QApplication(sys.argv)
        screen = QApplication.primaryScreen()
        img = screen.grabWindow(self.innerHwnd).toImage()
        img.save(rf'{self.path}\img\screenShot\{text}.png')
        # self.screenShot = ImageQt.fromqimage(img)

        return rf'{self.path}\img\screenShot\{text}.png'


    def get_900_506_image(self, text):
        self.get_image(text)
        while True:
            if self.SizeTest(text) != (900, 506):
                win32gui.MoveWindow(self.hwnd, True, True, 934, 540, True)
                time.sleep(0.5)
                self.get_image(text)
            else:
                break
        return rf'{self.path}\img\screenShot\{text}.png'

    
    def locateOnImage(self, item, image):

        self.get_900_506_image(image)
        if pyautogui.locate(rf'{self.path}\img\{item}.png', rf'{self.path}\img\screenShot\{image}.png', confidence=0.95) != None:
            # x = pyautogui.locate(rf'img\{item}.png', rf'img\screenShot\{image}.png', confidence=0.95)[0]
            # y = pyautogui.locate(rf'img\{item}.png', rf'img\screenShot\{image}.png', confidence=0.95)[1]
            x, y = pyautogui.center(pyautogui.locate(rf'{self.path}\img\{item}.png', rf'{self.path}\img\screenShot\{image}.png', confidence=0.95))
            return [x, y]
        else:
            return None

'''