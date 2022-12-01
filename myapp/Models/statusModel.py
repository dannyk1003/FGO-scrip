# 紀錄狀態
import win32api, win32gui, win32con, win32com.client
import json
import sys

class statusModel:
    def __init__(self):
        self.path = sys.path[0]

        self.times = 0
        self.window = 'BlueStacks App Player'
        self.innerWindow = 'Qt5154QWindowIcon'
        self.hwnd = ''
        self.innerHwnd = ''
        self.connect = ''
        self.history_title = list()
        # self.select_support = {'type':'', 'supporter': ''}

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
        
        return self.connect

    
    def battle(self, title, func, player, skill):
        '''
        紀錄角色與使用技能
        '''
        k = ''
        if player == 'clothes':
            k = func[0] + func[-1] + 'p0' + skill[0] + skill[-1]
        else:
            k = func[0] + func[-1] + player[0] + player[-1] + skill[0] + skill[-1]

        self.battleSkill[k] = title

        return self.battleSkill


    def write_history(self, title):
        with open(rf'{self.path}\history\battleSkill\{title}.json','w') as fw:
            json.dump(self.battleSkill,fw)
        with open(rf'{self.path}\history\Support\{title}.json','w') as fw:
            json.dump(self.supporter,fw)
    

    def read_history(self, text):
        with open(rf'{self.path}\history\battleSkill\{text}.json','r') as fr:
            self.battleSkill = json.load(fr)
        with open(rf'{self.path}\history\Support\{text}.json','r') as fr:
            self.supporter = json.load(fr)
        print(self.supporter, self.battleSkill)
        return [self.supporter, self.battleSkill]


    def support(self, title):
        self.supporter = {'type': title[0], 'supporter': title[1]}

        return self.supporter
