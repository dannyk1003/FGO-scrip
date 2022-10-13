# 顯示畫面

from re import S
import tkinter as tk
from tkinter import ttk


class View:
    def __init__(self, controller):
        self.controller = controller
        self.root = tk.Tk()

        self.times = tk.StringVar()
        self.get_hwnd = tk.StringVar()
        self.to_who = ['None', 'P1', 'P2', 'P3']

        self.root.title('FGO Scrip')
        self.root.geometry('1000x800')
        


    def main(self):
        
        self._make_label('Start&End', 0, 0)
        self._make_button('get hwnd', 'get_hwnd', 1, 0)
        self._make_button('Start', 'Start&End', 1, 1)
        self._make_button('End', 'Start&End', 1, 2)
        self._make_get_hwnd_label(1, 3)
        self._make_label('Times', 2, 0)
        self._make_times_label(3, 0)
        self._make_button('-5', 'Times', 3, 1)
        self._make_button('-1', 'Times', 3, 2)
        self._make_button('+1', 'Times', 3, 3)
        self._make_button('+5', 'Times', 3, 4)
        self._make_button('unlimited', 'Times', 3, 5)

        self._battle_area('Battle1', 4)
        self._battle_area('Battle2', 11)
        self._battle_area('Battle3', 18)

        
        self.root.mainloop()


    def _make_main_frame(self):
        self.main_frm = ttk.Frame(self.root)
        self.main_frm.pack()

    
    def _make_area_frame(self):
        frm = ttk.Frame(self.main_frm)
        frm.pack()


    def _make_button(self, text, func, x, y):

        def button_event():
            print(func)
            self.controller.on_button_click(text, func)

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
        get_hwnd = ttk.Entry(self.root, textvariable=self.get_hwnd, state='disabled')
        get_hwnd.grid(row=x, column=y)

    
    def _make_checkbutton(self, text, func, x, y):
        def checkbutton_event():
            self.controller.on_checkbutton_click(text, func, var.get())
            print(text, var.get())

        checkbutton_Text = tk.StringVar()
        var = tk.IntVar()
        checkbutton = tk.Checkbutton(self.root, text = checkbutton_Text, variable=var, command=checkbutton_event)
        checkbutton['text'] = text
        checkbutton.grid(row=x, column=y)


    def _make_combobox(self, text, x, y):
        def combobox_func(event):
            title = combobox.get()
            self.controller.on_

        combobox_Text = tk.StringVar()
        combobox = ttk.Combobox(self.root, textvariable=combobox_Text, state='readonly')
        combobox['values'] = text
        combobox.grid(row=x, column=y)
        combobox.current(0)

        combobox.bind("<<ComboboxSelected>>", combobox_func)


    def _battle_area(self, text, x):
        self._make_label(text, x, 0)
        self._make_label('clothesS1', x+1, 0)
        self._make_combobox(self.to_who, x+2, 0)
        self._make_label('P1S1', x+1, 1)
        self._make_combobox(self.to_who, x+2, 1)
        self._make_label('P2S1', x+1, 2)
        self._make_combobox(self.to_who, x+2, 2)
        self._make_label('P3S1', x+1, 3)
        self._make_combobox(self.to_who, x+2, 3)
        self._make_label('clothesS2', x+3, 0)
        self._make_combobox(self.to_who, x+4, 0)
        self._make_label('P1S2', x+3, 1)
        self._make_combobox(self.to_who, x+4, 1)
        self._make_label('P2S2', x+3, 2)
        self._make_combobox(self.to_who, x+4, 2)
        self._make_label('P3S2', x+3, 3)
        self._make_combobox(self.to_who, x+4, 3)
        self._make_label('clothesS3', x+5, 0)
        self._make_combobox(self.to_who, x+6, 0)
        self._make_label('P1S3', x+5, 1)
        self._make_combobox(self.to_who, x+6, 1)
        self._make_label('P2S3', x+5, 2)
        self._make_combobox(self.to_who, x+6, 2)
        self._make_label('P3S3', x+5, 3)
        self._make_combobox(self.to_who, x+6, 3)        
