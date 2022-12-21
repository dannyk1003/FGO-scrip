# 紀錄狀態
import win32api, win32gui, win32con, win32com.client
import json
import ast
from Models.historyDB import historyDB

class statusModel:
    def __init__(self, path):
        self.path = path

        self.times = 0
        self.window = 'BlueStacks App Player '
        self.innerWindow = 'Qt5154QWindowIcon'
        self.hwnd = ''
        self.innerHwnd = ''
        self.connect = ''
        self.history_title = list()
        self.historyDB = historyDB(self.path)

        self.battleSkill_init()
        # self.battleSkill = {'b1p0s1': None, 'b1p1s1': None, 'b1p2s1': None, 'b1p3s1': None, 
        #                     'b1p0s2': None, 'b1p1s2': None, 'b1p2s2': None, 'b1p3s2': None, 
        #                     'b1p0s3': None, 'b1p1s3': None, 'b1p2s3': None, 'b1p3s3': None,
        #                     'b2p0s1': None, 'b2p1s1': None, 'b2p2s1': None, 'b2p3s1': None,
        #                     'b2p0s2': None, 'b2p1s2': None, 'b2p2s2': None, 'b2p3s2': None,
        #                     'b2p0s3': None, 'b2p1s3': None, 'b2p2s3': None, 'b2p3s3': None,
        #                     'b3p0s1': None, 'b3p1s1': None, 'b3p2s1': None, 'b3p3s1': None,
        #                     'b3p0s2': None, 'b3p1s2': None, 'b3p2s2': None, 'b3p3s2': None,
        #                     'b3p0s3': None, 'b3p1s3': None, 'b3p2s3': None, 'b3p3s3': None,
        #                     }  
        self.apple = ''

    
    def battleSkill_init(self):
        with open(rf'{self.path}\Configs\support_init.json','r') as fr:
            self.supporter = json.load(fr)
                

        with open(rf'{self.path}\Configs\battleSkill_init.json','r') as fr:
            self.battleSkill = json.load(fr)


    def times_counter(self, text):
        if text == '-5':
            self.times -= 5
        elif text == '-1':
            self.times -= 1
        elif text == '+1':
            self.times += 1
        elif text == '+5':
            self.times += 5
        elif text == 'unlimited':
            self.times += 100
        elif text == 'end':
            self.times = 0

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
            if get_inner_windows(self.hwnd) == {}:
                self.connect = 'Fail'
            else:
                self.innerHwnd = get_inner_windows(self.hwnd)[self.innerWindow]
                print(self.hwnd, self.innerHwnd)
                self.connect = 'Success'
        
        return self.connect

    
    def battle(self, title, battle, player, skill):
        '''
        紀錄角色與使用技能
        '''
        k = ''
        if player == 'clothes':
            k = battle[0] + battle[-1] + 'p0' + skill[0] + skill[-1]
        else:
            k = battle[0] + battle[-1] + player[0] + player[-1] + skill[0] + skill[-1]

        self.battleSkill[k] = title

        return self.battleSkill

    
    def Noble_Phantasm(self, title, battle, player):
        k = battle[0] + battle[-1] + player[0] + player[-1] + 'NP'
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

    
    def add_history(self, name):
        self.historyDB.insert(name, self.supporter, self.battleSkill)


    def modify_history(self, name):
        self.historyDB.delete(name)
        self.historyDB.insert(name, self.supporter, self.battleSkill)


    def delete_history(self, name):
        self.historyDB.delete(name)


    def select_history(self, name):
        history = self.historyDB.select()

        history_name = history.get(name, history['first'])
        self.supporter = ast.literal_eval(history_name['Support'])
        self.battleSkill = ast.literal_eval(history_name['battleSkill'])

        

        return [self.supporter, self.battleSkill]

    
    def get_history_title(self):
        history = self.historyDB.select()
        self.history_title = history.keys()

        return list(self.history_title)
        

    def support(self, title):
        self.supporter = {"type": title[0], "character": title[1]}

        return self.supporter
