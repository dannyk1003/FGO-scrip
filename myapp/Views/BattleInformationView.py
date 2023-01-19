import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
# from Views.new_supportView import new_supportView


class BattleInformationView:
    def __init__(self, view):
        self.view = view
        self.root = tk.Tk()
        self.root.title('Battle Information')
        self.root.protocol('WM_DELETE_WINDOW', self.exit)
        self.BattleInformationViewOpen = True
        self.new_supportViewOpen = False
        self.view.statusController.battleSkill_init()

        self._support_area(0, 'support')
        # self._make_button('new_support', 1, 2)
        self._make_label('Select your Battle Skill', 3, 0)
        self._battle_area('battle1', 4)
        self._battle_area('battle2', 13)
        self._battle_area('battle3', 22)
        
        self._make_Save_area(31, 0)
        self._make_button('Done', 32, 3)
        self._make_button('Cancel', 32, 4)
        
        
    def main(self):
        self.root.mainloop()
        print('BattleInformationView end')

    def _make_Save_area(self, x, y):
        self._make_label('Remember me', x, 0)

        def button_event():
            name = self.entry.get()
            if name == '':
                tkinter.messagebox.showerror("Name Error", "Please enter a valid name")
            elif name in self.view.history_title:
                tkinter.messagebox.showerror("Name Error", "duplicate name")
            else:
                self.view.statusController.Save(name)
                self.view.get_history_title()
                self.view.history_title_combobox.set(name)

        self.entry = tk.Entry(self.root)
        self.entry.grid(row=x+1, column=y)
        # myButton = tk.Button(self.root, text = 'Save', command=button_event)
        # myButton.grid(row=x+1, column=y+1)
    
    def _support_area(self, x, func):
        self._make_label('Select your Support', x, 0)
        def type_func(event):
            support_type = combobox_type.get()

            combobox_supporter['values'] = self.view.support_character[support_type]
            combobox_supporter.current(0)

            self.view.supporter = self.view.statusController.support([support_type, combobox_supporter.get()])
            self.view.now_status_support.set(self.view.supporter)

            print(self.view.support_character[support_type])
            
        def supporter_func(event):
            support_character = combobox_supporter.get()
            self.view.supporter = self.view.statusController.support([combobox_type.get(), support_character])
            self.view.now_status_support.set(self.view.supporter)

        combobox_type = ttk.Combobox(self.root, state='readonly')
        combobox_type['values'] = self.view.support_type
        combobox_type.grid(row=x+1, column=0)
        combobox_type.current(0)
        combobox_type.bind("<<ComboboxSelected>>", type_func)

        combobox_supporter = ttk.Combobox(self.root, state='readonly')
        combobox_supporter.grid(row=x+1, column=1)
        print('a',self.view.supporter)
        combobox_supporter['values'] = self.view.support_character[combobox_type.get()]
        combobox_supporter.current(0)
        combobox_supporter.bind("<<ComboboxSelected>>", supporter_func)


    def _battle_area(self, battle, x):
        p0 = 'player0' # clothes
        p1 = 'player1'
        p2 = 'player2'
        p3 = 'player3'
        s1 = 'skill1'
        s2 = 'skill2'
        s3 = 'skill3'

        self._make_label(battle, x, 0)
        self._make_label('clothes', x+1, 0)
        self._make_label(p1, x+2, 0)
        self._make_label(p2, x+3, 0)
        self._make_label(p3, x+4, 0)
        self._make_label(s1, x, 1)
        self._make_label(s2, x, 2)
        self._make_label(s3, x, 3)
        self._make_label('Noble Phantasm', x, 4)

        self._make_battle_combobox(battle, x+1, 1, p0, s1)
        self._make_battle_combobox(battle, x+1, 2, p0, s2)
        self._make_battle_combobox(battle, x+1, 3, p0, s3)

        self._make_battle_combobox(battle, x+2, 1, p1, s1)
        self._make_battle_combobox(battle, x+2, 2, p1, s2)
        self._make_battle_combobox(battle, x+2, 3, p1, s3)
        self._make_Noble_Phantasm_combobox(battle, p1, x+2, 4)

        self._make_battle_combobox(battle, x+3, 1, p2, s1)
        self._make_battle_combobox(battle, x+3, 2, p2, s2)
        self._make_battle_combobox(battle, x+3, 3, p2, s3)
        self._make_Noble_Phantasm_combobox(battle, p2, x+3, 4)

        self._make_battle_combobox(battle, x+4, 1, p3, s1)
        self._make_battle_combobox(battle, x+4, 2, p3, s2)
        self._make_battle_combobox(battle, x+4, 3, p3, s3)
        self._make_Noble_Phantasm_combobox(battle, p3, x+4, 4)

        self._make_label('', x+5, 0)




    def _make_label(self, text, x, y):

        label_Text = tk.StringVar()
        label = ttk.Label(self.root, text=label_Text)
        label['text'] = text
        label_Text.set(text)
        label.grid(row=x, column=y)

    
    def _make_battle_combobox(self, battle, x, y, player, skill):
        def battle_combobox_func(event):
            title = combobox.get()
            self.view.battleSkill = self.view.statusController.battle(title, battle, player, skill)
            self.view.now_status_skill.set(self.view.battleSkill)
        


        combobox = ttk.Combobox(self.root, state='readonly')
        combobox['values'] = ['None', 'player1', 'player2', 'player3']
        combobox.grid(row=x, column=y)
        combobox.current(0)

        combobox.bind("<<ComboboxSelected>>", battle_combobox_func)


    def _make_Noble_Phantasm_combobox(self, battle, player, x, y):
        def Noble_Phantasm_func(event):
            title = combobox.get()
            self.view.battleSkill = self.view.statusController.Noble_Phantasm(title, battle, player)
            self.view.now_status_skill.set(self.view.battleSkill)


        combobox = ttk.Combobox(self.root, state='readonly')
        combobox['values'] = ['OFF', 'ON']
        combobox.grid(row=x, column=y)
        combobox.current(0)

        combobox.bind("<<ComboboxSelected>>", Noble_Phantasm_func)

    
    def _make_button(self, text, x, y):
        def Done():
            name = self.entry.get()
            if name == '':
                tkinter.messagebox.showerror("Name Error", "Please enter a valid name")

            elif name in self.view.history_title:
                tkinter.messagebox.showerror("Name Error", "duplicate name")
                
            else:
                self.view.statusController.Save(name)
                self.view.get_history_title()
                self.view.history_title_combobox.set(name)
                self.view.set_current_status()
                self.exit()
        
        def Cancel():
            self.view.history_title_combobox.set('')
            self.view.set_current_status()
            self.exit()

        
        def new_support():
            if self.new_supportViewOpen == False:
                self.new_supportViewOpen = True
                new_supportView(self).main()


        def button_event():
            if text == 'Done':
                name = self.entry.get()
                if name == '':
                    tkinter.messagebox.showerror("Name Error", "Please enter a valid name")
                elif name in self.view.history_title:
                    tkinter.messagebox.showerror("Name Error", "duplicate name")
                else:
                    self.view.statusController.Save(name)
                    self.view.get_history_title()
                    self.view.history_title_combobox.set(name)
                    self.view.set_current_status()
                    self.exit()

            elif text == 'Cancel':
                self.view.history_title_combobox.set('')
                self.view.set_current_status()
                self.exit()
            

        button_Text = tk.StringVar()
        button = ttk.Button(self.root, text=button_Text, command=eval(text))
        button['text'] = text
        button.grid(row=x, column=y)


    def _make_check_button(self, text, x, y):
        def check_button_func():
            title = var.get()
            print(title)

        

        var = tk.IntVar()
        check_button = tk.Checkbutton(self.root, text=text, variable=var, onvalue=1, offvalue=0, command=check_button_func)
        check_button.deselect()
        check_button.grid(row=x, column=y)


    
    def exit(self):
        # sys.exit(0)
        self.view.BattleInformationViewOpen = False
        self.view.get_history_title()
        self.view.history_title_combobox['value'] = self.view.history_title
        self.root.destroy()