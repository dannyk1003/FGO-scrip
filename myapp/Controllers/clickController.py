# 點擊流程
import sys
sys.path.append('..')

from Models.clickModel import Model
from Views.view import View

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)


    def main(self):
        self.view.main()


    def on_button_click(self, text, func):
        if func == 'get_hwnd':
            result = self.model.get_window()
            self.view.get_hwnd.set(result)
        elif func == 'Times':
            result = self.model.times_counter(text)
            self.view.times.set(result)
        print(result)
    

    def on_checkbutton_click(self, text, func, check):
        if func == 'clothes':
            result = self.model.use_clothes(text, check)
        

        print(result)

    
    def on_combobox_click(self, title, func, player, skill):
        if func == 'battle1' or func == 'battle2' or func == 'battle3':
            result = self.model.battle(title, func, player, skill)
            print(result)
        
    
