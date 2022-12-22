# 狀態流程
from Models.statusModel import statusModel

class statusController:
    def __init__(self, path):
        self.model = statusModel(path)
        self.path = path

    
    def Times(self, text):
        result = self.model.times_counter(text)
        return result

    
    def Save(self, name):
        # self.model.write_history(text)
        self.model.add_history(name)


    def battle(self, title, battle, player, skill):
        result = self.model.battle(title, battle, player, skill)
        return result

    
    def read_history(self, title):
        # result = self.model.read_history(title)
        result = self.model.select_history(title)
        return result

    
    def support(self, title):
        result = self.model.support(title)
        return result

    
    def get_history_title(self):
        result = self.model.get_history_title()
        return result

    
    def battleSkill_init(self):
        self.model.battleSkill_init()
        result = [self.model.supporter, self.model.battleSkill]
        return result

    
    def Noble_Phantasm(self, title, battle, player):
        result = self.model.Noble_Phantasm(title, battle, player)
        return result

    
    def modify(self,old_name,  name):
        self.model.modify_history(old_name, name)


    def delete(self, name):
        self.model.delete_history(name)



        
    
    # def on_button_click(self, text, func):
    #     result = None
    #     # if func == 'get_hwnd':
    #     #     result = self.model.get_window()
    #     #     return result

    #     # if func == 'Times':
    #     #     result = self.model.times_counter(text)
    #     #     return result
            
    #     if func == 'Save':
    #         self.model.write_history(text)

    #     print('StatusModel',result)
    #     # return result

    
    # def on_combobox_click(self, title, func, player, skill):
    #     if func == 'battle1' or func == 'battle2' or func == 'battle3':
    #         result = self.model.battle(title, func, player, skill)

    #     elif func == 'read_history':
    #         result = self.model.read_history(title) 

    #     elif func == 'support':
    #         result = self.model.support(title)

    #     print('statusController:', result)
    #     return result