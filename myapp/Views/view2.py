import tkinter as tk
from tkinter import ttk
import sys


class view2:
    def __init__(self, view):
        self.view = view
        self.root = tk.Tk()
        self.root.title('Battle Skill')
        self.root.protocol('WM_DELETE_WINDOW', self.print)
        self.view2open = True

        self._battle_area('Battle1', 'battle1', 0)
        self._battle_area('Battle2', 'battle2', 7)
        self._battle_area('Battle3', 'battle3', 14)
    
        
    def main(self):
        self.root.mainloop()
        print('delete')


    def _battle_area(self, text, func, x):
        c = 'clothes'
        p1 = 'player1'
        p2 = 'player2'
        p3 = 'player3'
        to_who = ['None', p1, p2, p3]
        s1 = 'skill1'
        s2 = 'skill2'
        s3 = 'skill3'

        self._make_label(text, x, 0)
        self._make_label('clothesS1', x+1, 0)
        self._make_combobox(to_who, func, x+2, 0, c, s1)
        self._make_label('P1S1', x+1, 1)
        self._make_combobox(to_who, func, x+2, 1, p1, s1)
        self._make_label('P2S1', x+1, 2)
        self._make_combobox(to_who, func, x+2, 2, p2, s1)
        self._make_label('P3S1', x+1, 3)
        self._make_combobox(to_who, func, x+2, 3, p3, s1)
        self._make_label('clothesS2', x+3, 0)
        self._make_combobox(to_who, func, x+4, 0, c, s2)
        self._make_label('P1S2', x+3, 1)
        self._make_combobox(to_who, func, x+4, 1, p1, s2)
        self._make_label('P2S2', x+3, 2)
        self._make_combobox(to_who, func, x+4, 2, p2, s2)
        self._make_label('P3S2', x+3, 3)
        self._make_combobox(to_who, func, x+4, 3, p3, s2)
        self._make_label('clothesS3', x+5, 0)
        self._make_combobox(to_who, func, x+6, 0, c, s3)
        self._make_label('P1S3', x+5, 1)
        self._make_combobox(to_who, func, x+6, 1, p1, s3)
        self._make_label('P2S3', x+5, 2)
        self._make_combobox(to_who, func, x+6, 2, p2, s3)
        self._make_label('P3S3', x+5, 3)
        self._make_combobox(to_who, func, x+6, 3, p3, s3)   

    def _make_label(self, text, x, y):

        label_Text = tk.StringVar()
        label = ttk.Label(self.root, text=label_Text)
        label['text'] = text
        label_Text.set(text)
        label.grid(row=x, column=y)

    

    def _make_combobox(self, text, func, x, y, player = None, skill = None):
        def combobox_func(event):
            title = combobox.get()
            if func == 'battle1' or func == 'battle2' or func == 'battle3':
                # self.skill = self.statusController.on_combobox_click(title, func, player, skill)
                self.skill = self.statusController.battle(title, func, player, skill)
                self.now_status_skill.set(self.skill)

            elif func == 'read_history':
                # self.support = self.statusController.on_combobox_click(title, func, player, skill)[0]
                # self.skill = self.statusController.on_combobox_click(title, func, player, skill)[1]
                self.support = self.statusController.read_history(title)[0]
                self.skill = self.statusController.read_history(title)[1]
                self.now_status_support.set(self.support)
                self.now_status_skill.set(self.skill)

        combobox = ttk.Combobox(self.root, state='readonly')
        combobox['values'] = text
        combobox.grid(row=x, column=y)
        combobox.current(0)

        combobox.bind("<<ComboboxSelected>>", combobox_func)

    
    def print(self):
        # sys.exit(0)
        self.view.view2open = False
        self.root.destroy()