# 紀錄狀態
import win32api, win32gui, win32con, win32com.client
import json
import ast
from Models.historyDB import historyDB

class statusModel:
    def __init__(self, path):
        self.path = path

        self.times = 0
        self.connect = ''
        self.history_title = list()
        self.historyDB = historyDB(self.path)

        self.battleSkill_init()

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

    
    def add_history(self, name):
        self.historyDB.insert(name, self.supporter, self.battleSkill)


    def modify_history(self, old_name, name):
        self.historyDB.delete(old_name)
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
