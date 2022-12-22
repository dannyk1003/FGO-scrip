import tkinter as tk
from tkinter import ttk
import tkinter.messagebox


class ReadHistoryView:
    def __init__(self, view):
        self.view = view
        self.root = tk.Tk()
        self.root.title(f'Read History - {self.view.now_history_name}')
        self.root.protocol('WM_DELETE_WINDOW', self.exit)
        self.ReadHistoryViewOpen = True

        self._support_area(0, 'support')
        self._make_label('Select your Battle Skill', 3, 0)
        self._battle_area('battle1', 4)
        self._battle_area('battle2', 13)
        self._battle_area('battle3', 22)
        
        self._make_modify_area(31, 0)
        self._make_button('Done', 32, 3)
        
        
    def main(self):
        self.root.mainloop()
        print('ReadHistoryView end')

    def _make_Save_area(self, x, y):
        self._make_label('Remember me', x, 0)
        def button_event():
            print('func')
            print(entry.get())
            print(entry)
            if entry.get() != '':
                text = entry.get()
                print(text)
                self.view.statusController.Save(text)

        entry = tk.Entry(self.root)
        entry.insert(0, self.view.now_history_name)
        entry.grid(row=x+1, column=y)

        myButton = tk.Button(self.root, text = 'modify', command=button_event)
        myButton.grid(row=x+1, column=y+1)

    
    def _make_modify_area(self, x, y):
        def button_event():
            name = entry.get()
            if name == '':
                tkinter.messagebox.showerror("Name Error", "Please enter a valid name")
            elif name in self.view.history_title:
                if name != self.view.now_history_name:
                    tkinter.messagebox.showerror("Name Error", "duplicate name")
                else:
                    self.view.statusController.modify(self.view.now_history_name, name)
                    self.view.history_title_combobox.set(name)
            else:
                self.view.statusController.modify(self.view.now_history_name, name)
                self.view.history_title_combobox.set(name)


        entry = tk.Entry(self.root)
        entry.insert(0, self.view.now_history_name)
        entry.grid(row=x+1, column=y)

        myButton = tk.Button(self.root, text = 'modify', command=button_event)
        myButton.grid(row=x+1, column=y+1)

    
    def _support_area(self, x, func):
        self._make_label('Select your Support', x, 0)
        def type_func(event):
            support_type = combobox_type.get()

            combobox_character['values'] = self.view.support_character[support_type]
            combobox_character.current(0)
            print(self.view.support_character[support_type])
            
        def supporter_func(event):
            support_character = combobox_character.get()
            self.view.supporter = self.view.statusController.support([combobox_type.get(), support_character])
            self.view.now_status_support.set(self.view.supporter)


        combobox_type = ttk.Combobox(self.root, state='readonly')
        combobox_type['values'] = self.view.support_type
        combobox_type.grid(row=x+1, column=0)
        print('a',self.view.supporter)
        combobox_type.set(self.view.supporter['type'])
        combobox_type.bind("<<ComboboxSelected>>", type_func)

        combobox_character = ttk.Combobox(self.root, state='readonly')
        combobox_character.grid(row=x+1, column=1)
        combobox_character['values'] = self.view.support_character[combobox_type.get()]
        combobox_character.set(self.view.supporter['character'])
        combobox_character.bind("<<ComboboxSelected>>", supporter_func)


    def _battle_area(self, battle, x):
        p0 = 'player0' # clothes
        p1 = 'player1'
        p2 = 'player2'
        p3 = 'player3'
        to_who = ['None', p1, p2, p3]
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
        def combobox_func(event):
            title = combobox.get()

            self.view.battleSkill = self.view.statusController.battle(title, battle, player, skill)
            self.view.now_status_skill.set(self.view.battleSkill)

        combobox = ttk.Combobox(self.root, state='readonly')
        combobox['values'] = [None, 'player1', 'player2', 'player3']
        combobox.grid(row=x, column=y)
        k = battle[0] + battle[-1] + player[0] + player[-1] + skill[0] + skill[-1]
        current = self.view.battleSkill[k]
        if current == 'player1':
            combobox.current(1)
        elif current == 'player2':
            combobox.current(2)
        elif current == 'player3':
            combobox.current(3)
        else:
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
        self.view.ReadHistoryViewOpen = False
        self.view.get_history_title()
        self.view.history_title_combobox['value'] = self.view.history_title
        self.root.destroy()

    
    def _make_Noble_Phantasm_combobox(self, battle, player, x, y):
        def Noble_Phantasm_func(event):
            title = combobox.get()
            self.view.battleSkill = self.view.statusController.Noble_Phantasm(title, battle, player)
            self.view.now_status_skill.set(self.view.battleSkill)


        combobox = ttk.Combobox(self.root, state='readonly')
        combobox['values'] = ['OFF', 'ON']
        combobox.grid(row=x, column=y)
        k = battle[0] + battle[-1] + player[0] + player[-1] + 'NP'
        current = self.view.battleSkill[k]

        if current == 'OFF':
            combobox.current(0)
        else:
            combobox.current(1)

        combobox.bind("<<ComboboxSelected>>", Noble_Phantasm_func)