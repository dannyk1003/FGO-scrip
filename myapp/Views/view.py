# 顯示畫面
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import os
import sys
from Views.BattleInformationView import BattleInformationView
from Views.GetHwndView import GetHwndView
from Views.ReadHistoryView import ReadHistoryView



class View:
    def __init__(self, statusController, clickController, hwndController, path, logger):
        self.path = path
        self.logger = logger

        self.statusController = statusController
        self.clickController = clickController
        self.hwndController = hwndController
        self.root = tk.Tk()

        self.times = tk.StringVar()
        self.get_hwnd_label = tk.StringVar()
        self.history_name = tk.StringVar()
        self.now_status_skill = tk.StringVar()
        self.now_status_support = tk.StringVar()
        self.supporter = ''
        self.battleSkill = ''
        self.time = 0
        self.connection = ''
        self.BattleInformationViewOpen = False
        self.ReadHistoryViewOpen = False
        self.GetHwndViewOpen = False
        self.get_history_title()
        self.get_support_title()
        self.apple = 'None'

        self.window = 'BlueStacks App Player'
        self.innerWindow = 'Qt5154QWindowIcon'
        self.hwnd = ''
        self.innerHwnd = ''

        self.root.title('FGO Scrip')
        self.root.geometry('800x600')

        self.root.protocol('WM_DELETE_WINDOW', self.exit)
        
        self.layout()
        
        

    def main(self):
        self.root.mainloop()


    def layout(self):
        self._make_label('Start&End', 0, 0)
        self._make_button('get hwnd', 'get_hwnd', 1, 0)
        self._make_get_hwnd_label(1, 1)
        # self._make_button('Start', 'start', 1, 2)
        self._make_start_button(1, 2)
        self._make_button('End', 'end', 1, 3)
        self._make_label('Times', 2, 0)
        self._make_times_label(3, 0)
        self._make_button('-5', 'Times', 3, 1)
        self._make_button('-1', 'Times', 3, 2)
        self._make_button('+1', 'Times', 3, 3)
        self._make_button('+5', 'Times', 3, 4)
        self._make_button('unlimited', 'Times', 3, 5)


        self._to_another_view('Read History', 4, 0)
        self._to_another_view('Battle Information', 4, 1)

        self._make_label('AP Recovery', 4, 2)
        self._make_apple_combobox(29, 2)

        # self._make_button('abc', 'abc', 29, 3)

        self._make_history_title_combobox(29, 0)
        self._make_button('delete', 'delete', 29, 1)

        self._make_label('Now Status', 30, 0)
        self._make_now_status_support_label(31, 0)
        self._make_now_status_skill_label(32, 0)


    def _make_main_frame(self):
        self.main_frm = ttk.Frame(self.root)
        self.main_frm.pack()

    
    def _make_area_frame(self):
        frm = ttk.Frame(self.main_frm)
        frm.pack()

    
    def _make_start_button(self, x, y):
        def button_event():
            if self.connection == '' or self.connection == 'Fail':
                tkinter.messagebox.showerror("Connect Error", "Please press get hwnd!")

            elif self.connection == 'Success':
                    if self.history_title_combobox.get() == '':
                        tkinter.messagebox.showerror("History Error", "Please select history!")
                    
                    else:
                        self.set_current_status()
                        self.clickController.start(self.supporter, self.battleSkill, self.apple, self.time, self.hwnd, self.innerHwnd)
            

        button = ttk.Button(self.root, text='Start', command=button_event)
        button.grid(row=x, column=y)


    def _make_button(self, text, func, x, y):

        def button_event():
            print(func)
            if func == 'get_hwnd':
                self.connection = self.hwndController.connection(self.window, self.innerWindow)
                self.hwnd = self.hwndController.get_hwnd(self.window)
                self.innerHwnd = self.hwndController.get_inner_hwnd(self.window, self.innerWindow)
                self.get_hwnd_label.set(self.connection)
                print(self.connection)

                if self.connection == 'Fail':
                    if self.GetHwndViewOpen == False:
                        self.GetHwndViewOpen = True
                        GetHwndView(self).main()

            elif func == 'Times':
                self.time = self.statusController.Times(text)
                self.times.set(self.time)

            elif func == 'Save':
                self.get_history_title()

            elif func == 'start':
                if self.connection == '' or self.connection == 'Fail':
                    tkinter.messagebox.showerror("Connect Error", "Please press get hwnd!")
                # connection = self.hwndController.connection(self.window, self.innerWindow)
                # self.get_hwnd_label.set(connection)

                elif self.connection == 'Success':
                    # self.hwnd = self.hwndController.get_hwnd(self.window)
                    # self.innerHwnd = self.hwndController.get_inner_hwnd(self.window, self.innerWindow)
                    self.clickController.start(self.supporter, self.battleSkill, self.apple, self.time, self.hwnd, self.innerHwnd)

            elif func == 'end':
                self.clickController.end()
                self.time = self.statusController.Times(func)
                self.times.set(self.time)

            elif func == 'delete':
                deleteOrNot = tkinter.messagebox.askquestion('Prompt', 'Do you want to continue?')

                if deleteOrNot == 'yes':
                    self.statusController.delete(self.now_history_name)
                    self.get_history_title()
                    self.history_title_combobox['values'] = self.history_title
                    self.history_title_combobox.set('')
                    self.set_current_status()

                else:
                    print('dont delete')
            
            elif func == 'abc':
                self.clickController.control(self.innerHwnd)
            

        button_Text = tk.StringVar()
        button = ttk.Button(self.root, text=button_Text, command=button_event)
        button['text'] = text
        button.grid(row=x, column=y)

    
    def set_current_status(self):
        if self.history_title_combobox.get() == '':
            self.supporter = ''
            self.battleSkill = ''
            self.now_status_support.set(self.supporter)
            self.now_status_skill.set(self.battleSkill)

        else:
            self.now_history_name = self.history_title_combobox.get()
            self.supporter = self.statusController.read_history(self.now_history_name)[0]
            self.battleSkill = self.statusController.read_history(self.now_history_name)[1]

            self.now_status_support.set(self.supporter)
            self.now_status_skill.set(self.battleSkill)
        

    def _to_another_view(self, text, x, y):
        def button_event():
            if text == 'Battle Information':
                if self.BattleInformationViewOpen == False:
                    self.BattleInformationViewOpen = True
                    BattleInformationView(self).main()
                    print('view: BattleInformationView end')

            elif text == 'Read History':
                if self.ReadHistoryViewOpen == False:
                    self.now_history_name = self.history_title_combobox.get()
                    if self.history_title_combobox.get() == '':
                        tkinter.messagebox.showerror("Name Error", "Please select a valid name")
                    else:
                        self.ReadHistoryViewOpen = True
                        ReadHistoryView(self).main()
                        print('view: ReadHistoryView end')
                

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
        get_hwnd = ttk.Entry(self.root, textvariable=self.get_hwnd_label, state='disabled')
        get_hwnd.grid(row=x, column=y)


    def _make_now_status_support_label(self, x, y):
        now_status_support = tk.Label(self.root, textvariable=self.now_status_support, state='disabled', wraplength=600)
        now_status_support.grid(row=x, column=y, columnspan=4)


    def _make_now_status_skill_label(self, x, y):
        now_status_skill = tk.Label(self.root, textvariable=self.now_status_skill, state='disabled', wraplength=600)
        now_status_skill.grid(row=x, column=y, columnspan=4)


    def _make_history_title_combobox(self, x, y):
        def combobox_func(event):
            self.set_current_status()


        self.history_title_combobox = ttk.Combobox(self.root, state='readonly', values=self.history_title)
        print(self.history_title)
        self.history_title_combobox.grid(row=x, column=y)

        self.now_history_name = self.history_title_combobox.get()

        self.history_title_combobox.bind("<<ComboboxSelected>>", combobox_func)     


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

        self.history_title = self.statusController.get_history_title()


    def get_support_title(self):
        self.support_type = ['all', 'saber', 'archer', 'lancer', 'rider', 'caster', 'assassin', 'berserker', 'other', 'mix']
        self.support_character = {'all': list(), 'saber': list(), 'archer': list(), 'lancer': list(), 'rider': list(), 'caster': list(), 'assassin': list(), 'berserker': list(), 'other': list(), 'mix': list()}

        if os.path.isdir(rf'{self.path}\img\Support'):
            for i in self.support_type:
                title = os.listdir(rf'{self.path}\img\Support\{i}')
                for j in title:
                    self.support_character[i].append(j.rstrip('.png'))
        else:
            for i in self.support_type:
                self.support_character[i].append('None')
            print('No Supporter')
        print(self.path)


    def exit(self):
        print('view end')
        sys.exit(0)


    def _make_apple_combobox(self, x, y):
        def combobox_func(event):
            title = combobox.get()
            self.apple = title



        combobox = ttk.Combobox(self.root, state='readonly')
        combobox['values'] = ['None', 'Gold', 'Silver', 'Bronze']
        combobox.current(0)
        combobox.grid(row=x, column=y)
        combobox.bind("<<ComboboxSelected>>", combobox_func)     
