# 點擊做法
import win32api, win32gui, win32con
import numpy as np
import time

class Model:
    def __init__(self):
        self.times = 0
        self.window = 'BlueStacks App Player'
        self.innerWindow = 'Qt5154QWindowIcon'
        self.hwnd = ''
        self.innerHwnd = ''

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
            return 'Fail'

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
            return 'Success'


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


    def doClick(self, x, y):
        hwnd = self.innerHwnd
        long_position = win32api.MAKELONG(x, y) 
        win32gui.PostMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, long_position)
        time.sleep(2)
        win32gui.PostMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, long_position)


