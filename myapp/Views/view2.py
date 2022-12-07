import tkinter as tk
from tkinter import ttk
import sys


class view2:
    def __init__(self, view):
        self.view = view
        self.root = tk.Tk()
        self.root.title('Battle Skill')
        self.root.protocol('WM_DELETE_WINDOW', self.exit)
        self.view2open = True

        self._support_area(0, 'support')
        self._make_label('Select your Battle Skill', 3, 0)
        self._battle_area('Battle1', 'battle1', 4)
        self._battle_area('Battle2', 'battle2', 11)
        self._battle_area('Battle3', 'battle3', 18)
        
        self._make_Save_area(25, 0)
        self._make_button('Done', 26, 3)
        
        
    def main(self):
        self.root.mainloop()
        print('view 2 end')

    def _make_Save_area(self, x, y):
        self._make_label('Remember me', x, 0)
        def button_event():
            print('func')
            print(entry.get())
            print(entry)
            if entry.get() != '':
                text = entry.get()
                # self.statusController.on_button_click(text, func)
                print(text)
                self.view.statusController.Save(text)

        entry = tk.Entry(self.root)
        entry.grid(row=x+1, column=y)

        myButton = tk.Button(self.root, text = 'Save', command=button_event)
        myButton.grid(row=x+1, column=y+1)

    
    def _support_area(self, x, func):
        self._make_label('Select your Support', x, 0)
        def type_func(event):
            support_type = combobox_type.get()

            combobox_supporter['values'] = self.view.supporter[support_type]
            combobox_supporter.current(0)
            print(self.view.supporter[support_type])
            
        def supporter_func(event):
            supporter = combobox_supporter.get()
            # self.support = self.statusController.on_combobox_click([combobox_type.get(), supporter], func, None, None)
            self.view.support = self.view.statusController.support([combobox_type.get(), supporter])
            self.view.now_status_support.set(self.view.support)

        combobox_type = ttk.Combobox(self.root, state='readonly')
        combobox_type['values'] = self.view.support_type
        combobox_type.grid(row=x+1, column=0)
        combobox_type.current(0)
        combobox_type.bind("<<ComboboxSelected>>", type_func)

        combobox_supporter = ttk.Combobox(self.root, state='readonly')
        combobox_supporter.grid(row=x+1, column=1)
        combobox_supporter['values'] = self.view.supporter[combobox_type.get()]
        combobox_supporter.current(0)
        combobox_supporter.bind("<<ComboboxSelected>>", supporter_func)


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
                self.view.skill = self.view.statusController.battle(title, func, player, skill)
                self.view.now_status_skill.set(self.view.skill)

            elif func == 'read_history':
                self.view.support = self.view.statusController.read_history(title)[0]
                self.view.skill = self.view.statusController.read_history(title)[1]
                self.view.now_status_support.set(self.view.support)
                self.view.now_status_skill.set(self.view.skill)

        combobox = ttk.Combobox(self.root, state='readonly')
        combobox['values'] = text
        combobox.grid(row=x, column=y)
        combobox.current(0)

        combobox.bind("<<ComboboxSelected>>", combobox_func)


    def _make_button(self, text, x, y):

        def button_event():
            self.exit()
            

        button_Text = tk.StringVar()
        button = ttk.Button(self.root, text=button_Text, command=button_event)
        button['text'] = text
        button.grid(row=x, column=y)

    
    def exit(self):
        # sys.exit(0)
        self.view.view2open = False
        self.root.destroy()