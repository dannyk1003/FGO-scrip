# 顯示畫面
import tkinter as tk
from tkinter import ttk
import os
import sys
from Views.view2 import view2
from Views.view3 import view3



class View:
    def __init__(self, statusController, clickController, hwndController):
        self.path = sys.path[0]

        self.statusController = statusController
        self.clickController = clickController
        self.hwndController = hwndController
        self.root = tk.Tk()

        self.times = tk.StringVar()
        self.connection = tk.StringVar()
        self.history_name = tk.StringVar()
        self.now_status_skill = tk.StringVar()
        self.now_status_support = tk.StringVar()
        self.support = ''
        self.skill = ''
        self.time = 0
        self.view2open = False
        self.view3open = False
        self.get_history_title()
        self.get_support_title()

        self.window = 'BlueStacks App Player '
        self.innerWindow = 'Qt5154QWindowIcon'
        self.hwnd = ''
        self.innerHwnd = ''

        self.root.title('FGO Scrip')
        self.root.geometry('1000x800')
        
        self.layout()
        
        

    def main(self):
        self.root.mainloop()


    def layout(self):
        self._make_label('Start&End', 0, 0)
        self._make_button('get hwnd', 'get_hwnd', 1, 0)
        self._make_get_hwnd_label(1, 1)
        self._make_button('Start', 'start', 1, 2)
        self._make_button('End', 'end', 1, 3)
        self._make_label('Times', 2, 0)
        self._make_times_label(3, 0)
        self._make_button('-5', 'Times', 3, 1)
        self._make_button('-1', 'Times', 3, 2)
        self._make_button('+1', 'Times', 3, 3)
        self._make_button('+5', 'Times', 3, 4)
        self._make_button('unlimited', 'Times', 3, 5)


        self._to_another_view('Battle Information', 4, 0)

        self._make_combobox(self.history_title, 'read_history', 29, 0)

        self._make_label('Now Status', 30, 0)
        self._make_now_status_support_label(31, 0)
        self._make_now_status_skill_label(32, 0)


    def _make_main_frame(self):
        self.main_frm = ttk.Frame(self.root)
        self.main_frm.pack()

    
    def _make_area_frame(self):
        frm = ttk.Frame(self.main_frm)
        frm.pack()


    def _make_button(self, text, func, x, y):

        def button_event():
            print(func)
            if func == 'get_hwnd':
                connection = self.hwndController.connection(self.window, self.innerWindow)
                hwnd = self.hwndController.get_hwnd(self.window)
                self.connection.set(connection)
                print(connection)
                if connection == 'Fail':
                    if self.view3open == False:
                        self.view3open = True
                        view3(self).main()

            elif func == 'Times':
                self.time = self.statusController.Times(text)
                self.times.set(self.time)
            elif func == 'Save':
                self.get_history_title()
            elif func == 'start':
                connection = self.hwndController.connection(self.window, self.innerWindow)
                self.connection.set(connection)
                if connection == 'Success':
                    self.hwnd = self.hwndController.get_hwnd(self.window)
                    self.innerHwnd = self.hwndController.get_inner_hwnd(self.window, self.innerWindow)
                    self.clickController.start(self.support, self.skill, self.time, self.hwnd, self.innerHwnd)
            elif func == 'end':
                self.clickController.end()
                self.time = self.statusController.Times(func)
                self.times.set(self.time)
            

        button_Text = tk.StringVar()
        button = ttk.Button(self.root, text=button_Text, command=button_event)
        button['text'] = text
        button.grid(row=x, column=y)

    
    def _to_another_view(self, text, x, y):
        def button_event():
            if self.view2open == False:
                self.view2open = True
                view2(self).main()
                print('kk')
                
            

        button_Text = tk.StringVar()
        button = ttk.Button(self.root, text=button_Text, command=button_event)
        button['text'] = text
        button.grid(row=x, column=y)  


    def _make_label(self, text, x, y):

        label_Text = tk.StringVar()
        label = ttk.Label(self.root, text=label_Text)
        label['text'] = text
        label_Text.set(text)
        label.grid(row=x, column=y)


    def _make_times_label(self, x, y):
        times = ttk.Entry(self.root, textvariable=self.times, state='disabled')
        times.grid(row=x, column=y)


    def _make_get_hwnd_label(self, x, y):
        get_hwnd = ttk.Entry(self.root, textvariable=self.connection, state='disabled')
        get_hwnd.grid(row=x, column=y)


    def _make_now_status_support_label(self, x, y):
        now_status_support = tk.Label(self.root, textvariable=self.now_status_support, state='disabled', wraplength=600)
        now_status_support.grid(row=x, column=y, columnspan=4)


    def _make_now_status_skill_label(self, x, y):
        now_status_skill = tk.Label(self.root, textvariable=self.now_status_skill, state='disabled', wraplength=600)
        now_status_skill.grid(row=x, column=y, columnspan=4)

    
    def _make_checkbutton(self, text, func, x, y):
        def checkbutton_event():
            self.statusController.on_checkbutton_click(text, func, var.get())
            print(text, var.get())

        checkbutton_Text = tk.StringVar()
        var = tk.IntVar()
        checkbutton = tk.Checkbutton(self.root, text = checkbutton_Text, variable=var, command=checkbutton_event)
        checkbutton['text'] = text
        checkbutton.grid(row=x, column=y)


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


    def _support_area(self, x, func):
        self._make_label('Support', x, 0)
        def type_func(event):
            support_type = combobox_type.get()

            combobox_supporter['values'] = self.supporter[support_type]
            print(self.supporter[support_type])
            
        def supporter_func(event):
            supporter = combobox_supporter.get()
            # self.support = self.statusController.on_combobox_click([combobox_type.get(), supporter], func, None, None)
            self.support = self.statusController.support([combobox_type.get(), supporter])
            self.now_status_support.set(self.support)

        combobox_type = ttk.Combobox(self.root, state='readonly')
        combobox_type['values'] = self.support_type
        combobox_type.grid(row=x+1, column=0)
        combobox_type.bind("<<ComboboxSelected>>", type_func)

        combobox_supporter = ttk.Combobox(self.root, state='readonly')
        combobox_supporter.grid(row=x+1, column=1)
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


    def _make_Save_area(self, x, y):

        def button_event():
            print(entry_text.get())
            if entry_text.get() != '':
                text = entry_text.get()
                print(text)
                # self.statusController.on_button_click(text, func)
                self.statusController.Save(text)

        entry_text = tk.StringVar()
        entry = tk.Entry(self.root, textvariable=entry_text)
        entry.grid(row=x, column=y)

        myButton = tk.Button(self.root, text = 'Save', command=button_event)
        myButton.grid(row=x, column=y+1)


    def get_history_title(self):
        self.history_title = list()
        if os.path.isdir(rf'{self.path}\history\battleSkill'):
            title = os.listdir(rf'{self.path}\history\battleSkill')
            for i in title:
                self.history_title.append(i.rstrip('.json'))
        else:
            self.history_title.append(None)


    
    def get_support_title(self):
        self.support_type = ['all', 'saber', 'archer', 'lancer', 'rider', 'caster', 'assassin', 'berserker', 'other', 'mix']
        self.supporter = {'all': list(), 'saber': list(), 'archer': list(), 'lancer': list(), 'rider': list(), 'caster': list(), 'assassin': list(), 'berserker': list(), 'other': list(), 'mix': list()}
        # title = os.listdir(rf'.\img\Support\{type}')
        if os.path.isdir(rf'{self.path}\img\Support'):
            for i in self.support_type:
                title = os.listdir(rf'{self.path}\img\Support\{i}')
                for j in title:
                    self.supporter[i].append(j.rstrip('.png'))
        else:
            for i in self.support_type:
                self.supporter[i].append(None)
            print('No Supporter')
