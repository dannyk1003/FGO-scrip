# 點擊流程
import sys

sys.path.append('..')

from Models.statusModel import statusModel

class statusController:
    def __init__(self):
        self.model = statusModel()


    def on_button_click(self, text, func):
        result = None
        if func == 'get_hwnd':
            result = self.model.get_window()
            return result

        elif func == 'Times':
            result = self.model.times_counter(text)
            return result
            
        elif func == 'Save':
            self.model.write_history(text)

        print(result)
        # return result

    
    def on_combobox_click(self, title, func, player, skill):
        if func == 'battle1' or func == 'battle2' or func == 'battle3':
            result = self.model.battle(title, func, player, skill)

        elif func == 'read_history':
            result = self.model.read_history(title) 

        elif func == 'support':
            result = self.model.support(title)

        print('statusController:', result)
        return result
        
    
