# 點擊做法
import win32api, win32gui, win32ui
import numpy as np

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

    
    def use_skill(self, title):
        pass
