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

        self._make_stringVar()
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


        self._to_another_view('Modify History', 4, 0)
        self._to_another_view('Battle Information', 4, 1)

        self._make_label('AP Recovery', 4, 2)
        self._make_apple_combobox(29, 2)

        # self._make_button('abc', 'abc', 29, 3)

        self._make_history_title_combobox(29, 0)
        self._make_button('delete', 'delete', 29, 1)

        self._make_label('Now Status', 30, 0)
        self._make_now_status_support_column(31, 0)
        self._make_now_status_skill_column(1, 33, 0)
        self._make_now_status_skill_column(2, 39, 0)
        self._make_now_status_skill_column(3, 45, 0)
        # self._make_now_status_skill_label(52,0)


    def _make_stringVar(self):
        self.times = tk.StringVar()
        self.get_hwnd_label = tk.StringVar()
        self.history_name = tk.StringVar()
        self.now_status_skill = tk.StringVar()
        self.now_status_support = tk.StringVar()
        self.now_status_support_type = tk.StringVar()
        self.now_status_support_character = tk.StringVar()

        self.battle_skill_Var = dict()
        for i in ['b1', 'b2', 'b3']:
            for j in ['p0', 'p1', 'p2', 'p3']:
                for k in ['s1', 's2', 's3', 'NP']:
                    player = i + j + k
                    self.battle_skill_Var[player] = tk.StringVar()


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
    

    def _battle_skill_Var(self):
        self.battleSkill['b1p0NP'] = ''
        self.battleSkill['b2p0NP'] = ''
        self.battleSkill['b3p0NP'] = ''

        for i in ['b1', 'b2', 'b3']:
            for j in ['p0', 'p1', 'p2', 'p3']:
                for k in ['s1', 's2', 's3', 'NP']:
                    player = i + j + k
                    self.battle_skill_Var[player].set(self.battleSkill[player])
    
    
    def set_current_status(self):
        if self.history_title_combobox.get() == '':
            self.supporter = ''
            self.battleSkill = ''
            self.now_status_support.set(self.supporter)
            self.now_status_support_type.set(self.supporter['type'])
            self.now_status_support_character.set(self.supporter['character'])
            self.now_status_skill.set(self.battleSkill)
            self._battle_skill_Var()

        else:
            self.now_history_name = self.history_title_combobox.get()
            self.supporter = self.statusController.read_history(self.now_history_name)[0]
            self.battleSkill = self.statusController.read_history(self.now_history_name)[1]

            self.now_status_support.set(self.supporter)
            self.now_status_support_type.set(self.supporter['type'])
            self.now_status_support_character.set(self.supporter['character'])
            self.now_status_skill.set(self.battleSkill)
            self._battle_skill_Var()
        

    def _to_another_view(self, text, x, y):
        def button_event():
            if text == 'Battle Information':
                if self.BattleInformationViewOpen == False:
                    self.BattleInformationViewOpen = True
                    BattleInformationView(self).main()
                    print('view: BattleInformationView end')

            elif text == 'Modify History':
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
    

    def _make_now_status_support_column(self, x, y):
        self._make_label('support_type', x, y)
        self._make_label('support_character', x, y+1)
        support_type_column = tk.Label(self.root, textvariable=self.now_status_support_type, state='disabled')
        support_type_column.grid(row=x+1, column=y)
        support_character_column = tk.Label(self.root, textvariable=self.now_status_support_character, state='disabled')
        support_character_column.grid(row=x+1, column=y+1)
    
    def _make_now_status_skill_column(self, battle, x, y):
        self._make_label(f'Battle{battle}', x, y)
        self._make_label('Skill1', x, y+1)
        self._make_label('Skill2', x, y+2)
        self._make_label('Skill3', x, y+3)
        self._make_label('Noble Phantasm ', x, y+4)
        self._make_label('Clothes', x+1, y)
        self._make_label('Player1', x+2, y)
        self._make_label('Player2', x+3, y)
        self._make_label('Player3', x+4, y)
        m = 1
        n = 1
        for i in ['p0', 'p1', 'p2', 'p3']:
            for j in ['s1', 's2', 's3', 'NP']:
                player = 'b' + str(battle) + i + j
                battle_label = tk.Label(self.root, textvariable=self.battle_skill_Var[player], state='disabled')
                # battle_label = tk.Label(self.root, textvariable='A', state='disabled')
                battle_label.grid(row=x+m, column=y+n)
                n +=1
            n = 1
            m += 1
        self._make_label('', x+5, y)


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
