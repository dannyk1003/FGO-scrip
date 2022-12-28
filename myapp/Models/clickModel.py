# 點擊做法
import win32api, win32gui, win32con, win32com.client
import time
import pyautogui
import pythoncom
import json
from Models.Visual import Visual



class clickModel:
    def __init__(self, path, app):
        self.path = path
        self.app = app

        self.times = 0
        self.hwnd = ''
        self.innerHwnd = ''
        self.connect = ''
        
        self.apple = 'None'


    def doClick(self, position):
        print('click')
        x = position[0]
        y = position[1]
        hwnd = self.innerHwnd
        long_position = win32api.MAKELONG(int(x), int(y)) 
        win32gui.SendMessage(hwnd, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
        win32gui.PostMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, long_position)
        # time.sleep(0.5)
        win32gui.SendMessage(hwnd, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
        win32gui.PostMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, long_position)
        time.sleep(0.5)

    
    def doClick_pixel(self, position):
        before_img = self.Visual.get_900_506_image()
        x = position[0]
        y = position[1]
        before_pixel = self.Visual.image_pixel(before_img, x, y)

        self.doClick(position)
        time.sleep(1)

        after_img = self.Visual.get_900_506_image()
        after_pixel = self.Visual.image_pixel(after_img, x, y)

        while before_pixel == after_pixel:
            time.sleep(1)
            self.doClick(position)

            after_img = self.Visual.get_900_506_image()
            after_pixel = self.Visual.image_pixel(after_img, x, y)

    
    def doClick_cutImage(self, position, x_start, y_start, x_end, y_end):
        def click_check(before, after):
            return self.Visual.different_image_check(before, after)

        before = self.Visual.get_900_506_image()
        before_cut = self.Visual.image_cut(before, x_start, y_start, x_end, y_end)
        while True:
            self.doClick(position)
            time.sleep(1)
            after = self.Visual.get_900_506_image()
            after_cut = self.Visual.image_cut(after, x_start, y_start, x_end, y_end)
            if click_check(before_cut, after_cut):
                break
            time.sleep(1)


    def window_to_front(self):
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.SendKeys('%')
        win32gui.SetForegroundWindow(self.hwnd)

    
    def status_init(self, now_status_support, now_status_skill, apple, hwnd, innerHwnd):
        pythoncom.CoInitialize()
        self.hwnd = hwnd
        self.innerHwnd = innerHwnd
        self.apple = apple

        self.Visual = Visual(self.hwnd, self.innerHwnd, self.path, self.app)
        
        self.position()
        if now_status_support != '':
            self.supporter = now_status_support
        else:
            with open(rf'{self.path}\Configs\support_init.json','r') as fr:
                self.supporter = json.load(fr)
                
        if now_status_skill != '':
            self.battleSkill = now_status_skill
        else:
            with open(rf'{self.path}\Configs\battleSkill_init.json','r') as fr:
                self.battleSkill = json.load(fr)
        
        self.window_to_front()


    def now_step(self):
        self.step = 0
        n1 = self.CheckBattleCount(1)
        n2 = self.CheckBattleCount(2)
        n3 = self.CheckBattleCount(3)
        n = self.Visual.locateOnImage('clothes')
        if n != None:
            print(n1, n2, n3)
            if n1 != None:
                self.step = 1
            if n2 != None:
                self.step = 2
            if n3 != None:
                self.step = 3
        print('now step is', self.step)


    def runScrip(self):

        while self.step != 4:
            if self.step == 0:
                self.go_again()

            if self.step == 0:
                self.over_limit()

            if self.step == 0:
                self.AP_recovery()

            if self.step == 0:
                self.select_support()
                self.step += 1
            
            if  self.step == 1:
                self.Battle(1)
                self.step += 1

            if  self.step == 2:
                self.Battle(2)
                self.step += 1

            if  self.step == 3:
                self.Battle(3)
                self.step += 1
            
            if self.step == 4:
                print('battle end')
                self.step = 0
                break   
    

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


    def Battle(self, n): # battle n
        self.main_screen(5)        
        print('now is battle', n)

        while True:
            battle_count_position = self.CheckBattleCount(n)
            print(battle_count_position)

            if battle_count_position == None: # 不是 battle n 就離開
                break

            else:
                for i in range(4):
                    for j in range(1, 4, 1):
                        p = 'b' + str(n) + 'p' + str(i) + 's' + str(j)
                        m = self.battleSkill[p]

                        if m != 'None':
                            self.useSkill(i, j, m)
                            time.sleep(1)

                while True:
                    self.main_screen(5)
                    self.useAttack(n)
                    self.main_screen(5)
                    battle_count_position = self.CheckBattleCount(n)
                    with_servant_connect_position = self.Visual.locateOnImage('with_servant_connect')

                    if battle_count_position == None:
                        break
                    elif with_servant_connect_position != None:
                        break
                break
            
        print('battle ', n, ' end')

    
    def endBattle(self):
        if self.main_screen(5) == 'with_servant_connect':
            while True:
                with_servant_connect_position = self.Visual.locateOnImage('with_servant_connect')
                self.doClick(with_servant_connect_position)

                time.sleep(1)
                masterEXP_position = self.Visual.locateOnImage('masterEXP')                   



    def main_screen(self, t):
        clothes_position = self.Visual.locateOnImage('clothes')
        with_servant_connect_position = self.Visual.locateOnImage('with_servant_connect')

        while True:
            if clothes_position != None: # 畫面上有 '御主技能'
                return 'clothes'
            elif with_servant_connect_position != None: # 畫面上有 '與從者的羈絆'
                return 'with_servant_connect'
            else:
                time.sleep(t)
                clothes_position = self.Visual.locateOnImage('clothes')
                with_servant_connect_position = self.Visual.locateOnImage('with_servant_connect')


    def useSkill_(self, p, n, m): # player p 的第 n 個技能, 給player m
        if m != 'None':
            player = 'p' + str(p) + 's' + str(n)
            print(player)
            if p == 0:
                clothes_position = self.Visual.locateOnImage('clothes')
                while True:
                    if clothes_position != None:
                        time.sleep(1.5)
                        # self.doClick(self.clothes)
                        self.sure_doClick(self.clothes)
                        time.sleep(1)
                        break
                    else:
                        time.sleep(0.5)
                        clothes_position = self.Visual.locateOnImage('clothes')
            
            # self.doClick(self.playerSkill[player])
            self.sure_doClick(self.playerSkill[player])
            time.sleep(4)

            if self.skill_used_check() != None:
                self.doClick(self.skill_used_check())
                time.sleep(2)
                if p == 0:
                    # self.doClick(self.clothes)
                    self.sure_doClick(self.clothes)
                    time.sleep(1)
            else:
                Please_select_object_position = self.Visual.locateOnImage('Please_select_object')
                if Please_select_object_position != None:
                    # self.doClick(self.toPlayer[m])
                    self.sure_doClick(self.toPlayer[m])
                time.sleep(4)

    
    def useSkill(self, p, n, m):
        if m != 'None':

            if p == 0:
                self.useClothesSkill(n, m)

            else:
                self.usePlayerSkill(p, n, m)
        print('finish one skill')

    
    def useClothesSkill(self, n, m):
        player = 'p0s' + str(n)

        self.main_screen(2)
        print('click clothes')
        time.sleep(2)
        self.doClick_cutImage(self.clothes, 600, 200, 800, 250)
        time.sleep(2)

        # self.doClick_pixel(self.playerSkill[player])
        self.doClick(self.playerSkill[player])
        time.sleep(4)

        # while True:

        if self.please_select_object() != None:
            self.sure_doClick(self.toPlayer[m])
            # break

        elif self.skill_used_check() != None:
            self.sure_doClick(self.skill_used_check())
            self.doClick_cutImage(self.clothes, 600, 200, 800, 250)
            # break

            # else:
            #     self.doClick_cutImage(self.playerSkill[player], 600, 200, 800, 250)
            #     time.sleep(2)
        

    def usePlayerSkill(self, p, n, m):
        player = 'p' + str(p) + 's' + str(n)

        self.main_screen(2)
        before_pixel = self.position_pixel(self.playerSkill[player])
        self.doClick(self.playerSkill[player])
        time.sleep(2)
        after_pixel = self.position_pixel(self.playerSkill[player])

        while True:

            if self.please_select_object() != None:
                self.sure_doClick(self.toPlayer[m])
                break

            elif self.skill_used_check() != None:
                self.sure_doClick(self.skill_used_check())
                break

            elif before_pixel != after_pixel:
                break

            else:
                self.doClick(self.playerSkill[player])
                time.sleep(2)
                after_pixel = self.position_pixel(self.playerSkill[player])


    
    def please_select_object(self):
        Please_select_object_position = self.Visual.locateOnImage('Please_select_object')
        if Please_select_object_position != None:
            return Please_select_object_position
        else:
            return None
    

    def skill_used_check(self):
        # Now = self.Visual.get_900_506_image()
        # cancel = rf'{self.path}\img\cancel.png'

        cancel_position = self.Visual.locateOnImage('cancel')
        if cancel_position != None:
            return cancel_position
        else:
            return None

        # if pyautogui.locate(cancel, Now, confidence=0.8) != None :
        #     print(pyautogui.locate(cancel, Now, confidence=0.8))
        #     x = pyautogui.locate(cancel, Now, confidence=0.8)[0]
        #     y = pyautogui.locate(cancel, Now, confidence=0.8)[1]
        #     return [x, y]
        # else:
        #     return None


    def position_pixel(self, position):
        pixel = self.Visual.get_pixel(position)
        return pixel

        
    def useAttack(self, n):
        self.position()

        p1np = 'b' + str(n) + 'p1NP'
        p2np = 'b' + str(n) + 'p2NP'
        p3np = 'b' + str(n) + 'p3NP'
        np_list = [self.battleSkill[p1np], self.battleSkill[p2np],self.battleSkill[p3np]]
     

        while True:
            self.doClick(self.attack)
            time.sleep(2)
        
            for i, p in enumerate(np_list):
                if p == 'ON':
                    self.doClick(self.big[i])
                    time.sleep(1)

            for j in range(3):
                self.doClick(self.small[j])
                time.sleep(1)
            
            go_back = self.wait_until('go_back', 5, 1)
            if go_back != None:
                self.sure_doClick(go_back)
                time.sleep(2)

            else:
                time.sleep(10)
                break

    
    def CheckBattleCount(self, count):
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
        

    def select_support(self):
        while True:
            time.sleep(2)
            # support_choose_position = self.locateOnImage(rf"\Support\support_choose", 'ScreenShot')

            support_choose_position = self.Visual.locateOnImage(rf"\Support\support_choose")

            if support_choose_position != None:
                break

        # support_type_position = self.locateOnImage(rf"\Support\{self.supporter['type']}", 'ScreenShot')
            
        support_type_position = self.Visual.locateOnImage(rf"\Support\{self.supporter['type']}")

        self.doClick(support_type_position)

        # supporter_position = self.locateOnImage(rf"\Support\{self.supporter['type']}\{self.supporter['supporter']}", 'ScreenShot')

        supporter_position = self.Visual.locateOnImage(rf"\Support\{self.supporter['type']}\{self.supporter['character']}")

        print(supporter_position)

        if supporter_position != None:
            time.sleep(1)
            self.doClick(supporter_position)
        else:
            i = 0
            while i != 5:
                i += 1
                # go_down_position = self.locateOnImage(rf"\Support\go_down", 'ScreenShot')

                go_down_position = self.Visual.locateOnImage(rf"\Support\go_down")

                if go_down_position == None:
                    # re_new_list_position = self.locateOnImage(rf"\Support\re_new_list", 'ScreenShot')

                    re_new_list_position = self.Visual.locateOnImage(rf"\Support\re_new_list")

                    self.doClick(re_new_list_position)
                    time.sleep(1)
                    # yes_position = self.locateOnImage(rf"\Support\yes", 'ScreenShot')

                    yes_position = self.Visual.locateOnImage(rf"\Support\yes")

                    self.doClick(yes_position)
                    time.sleep(5)
                    i = 0

                    support_type_position = self.Visual.locateOnImage(rf"\Support\{self.supporter['type']}")

                    self.doClick(support_type_position)

                else:
                    self.doClick(go_down_position)
                    time.sleep(2)
                
                # supporter_position = self.locateOnImage(rf"\Support\{self.supporter['type']}\{self.supporter['supporter']}", 'ScreenShot')

                supporter_position = self.Visual.locateOnImage(rf"\Support\{self.supporter['type']}\{self.supporter['character']}")

                if supporter_position != None:
                    time.sleep(1)
                    self.doClick(supporter_position)
                    break
        time.sleep(1)
        # mission_start_position = self.locateOnImage(rf"\Support\mission_start", 'ScreenShot')

        mission_start_position = self.Visual.locateOnImage(rf"\Support\mission_start")
        clothes_position = self.Visual.locateOnImage('clothes')

        while True:

            if mission_start_position != None:
                self.doClick(mission_start_position)
                break
            elif clothes_position != None:
                break
            else:
                time.sleep(0.5)
                mission_start_position = self.Visual.locateOnImage(rf"\Support\mission_start")
                clothes_position = self.Visual.locateOnImage('clothes')
        
        print('select end')


    def go_again(self):
        while True:
            go_again_position = self.Visual.locateOnImage(rf"go_again")
            close_position = self.Visual.locateOnImage(rf"close")
            last_time_position = self.Visual.locateOnImage(rf"last_time")

            if go_again_position == None: # 沒有連續出擊
                if close_position == None: # 沒有關閉
                    self.doClick(self.next)
                    time.sleep(0.5)

                else: # 有關閉 -> 選關頁面
                    last_time_position = self.Visual.locateOnImage(rf"last_time")

                    if last_time_position == None: # 沒有上次執行
                        self.doClick(self.mission) # 按最上面那一關
                        break
                    else: # 有上次執行
                        self.doClick(last_time_position) # 按上次執行
                        break
            else: # 有連續出擊
                self.doClick(go_again_position) # 按連續出擊
                break

    
    def over_limit(self):
        over_limit_position = self.Visual.locateOnImage(rf"over_limit")
        if over_limit_position != None:
            print('over limit')
            self.step = 4
            return True


    def AP_recovery(self):

        AP_position = self.Visual.locateOnImage(rf"\AP_Recovery\AP")

        if AP_position != None:
            if self.apple == 'None':
                self.step = 4
            
            else:
                go_down_position = self.wait_until(rf"\AP_Recovery\go_down", 5, 1)
                if go_down_position != None:
                    self.sure_doClick(go_down_position)
                    time.sleep(1)

                    apple_position = self.Visual.locateOnImage(rf"\AP_Recovery\{self.apple}")
                    if apple_position != None:
                        self.sure_doClick(apple_position)
                        sure_position = self.wait_until(rf"\AP_Recovery\sure", 10, 1)
                        self.sure_doClick(sure_position)
                
                else:
                    self.step = 0

        
    def wait_until(self, item, n, t):
        item_position = self.Visual.locateOnImage(item)

        for i in range(n):
            if item_position != None:
                return item_position
            else:
                time.sleep(t)
                item_position = self.Visual.locateOnImage(item)
        
        return None


    def sure_doClick(self, position):
        def click_check(before, after, ):
            return self.Visual.different_image_check(before, after)

        before = self.Visual.get_900_506_image()
        while True:
            self.doClick(position)
            after = self.Visual.get_900_506_image()
            # before.show()
            # after.show()
            if click_check(before, after):
                break
            time.sleep(1)

    
    def no_control(self, innerHwnd):
        win32gui.EnableWindow(innerHwnd, False)
        print('F')

    def control(self, innerHwnd):
        win32gui.EnableWindow(innerHwnd, True)
        print('T')