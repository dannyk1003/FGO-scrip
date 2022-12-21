import tkinter as tk
from tkinter import ttk


class GetHwndView:
    def __init__(self, view):
        self.view = view
        self.root = tk.Tk()
        self.root.title('get hwnd')
        self.root.protocol('WM_DELETE_WINDOW', self.exit)
        self.GetHwndViewOpen = True
        self.window_list = self.view.hwndController.get_window_list()
        self._make_combobox_and_innerWindows(self.window_list)
        self._make_button('Done')

        
        
    def main(self):
        self.root.mainloop()
        print('view 3 end')


    def _make_combobox_and_innerWindows(self, content):
        
        def combobox_func(event):
            print(combobox.current(), combobox.get())
            label_Text.set(f'the window is : \n {combobox_Text.get()}' )
            self.view.window = combobox.get()
            self.view.hwnd = self.view.hwndController.get_hwnd(self.view.window)
            self.inner_window_list = self.view.hwndController.get_inner_window_list(self.view.hwnd)

            inner_combobox['values'] = self.inner_window_list


        def inner_combobox_func(event):
            print(123)
            print(inner_combobox.current(), inner_combobox.get())
            inner_label_Text.set(f'the inner window is : \n {inner_combobox_Text.get()}')
            self.view.innerWindow = inner_combobox.get()
            self.view.innerHwnd = self.view.hwndController.get_inner_hwnd(self.view.window, self.view.innerWindow)



        combobox_Text = tk.StringVar()
        combobox = ttk.Combobox(self.root, textvariable=combobox_Text, state='readonly')
        combobox['values'] = content
        combobox.pack()

        label_Text = tk.StringVar()
        label = tk.Label(self.root, textvariable=label_Text, font=('Arial', 12), wraplength=400)

        label.pack()

        combobox.bind("<<ComboboxSelected>>", combobox_func)

        
        inner_combobox_Text = tk.StringVar()
        inner_combobox = ttk.Combobox(self.root, textvariable=inner_combobox_Text, state='readonly')
        inner_combobox.pack()

        inner_label_Text = tk.StringVar()
        inner_label = tk.Label(self.root, textvariable=inner_label_Text, font=('Arial', 12), wraplength=400)

        inner_combobox.bind("<<ComboboxSelected>>", inner_combobox_func)

        inner_label.pack()


    def _make_button(self, text):

        def button_event():
            self.exit()
            

        button_Text = tk.StringVar()
        button = ttk.Button(self.root, text=button_Text, command=button_event)
        button['text'] = text
        button.pack()


    
    def exit(self):
        # sys.exit(0)
        self.view.GetHwndViewOpen = False
        self.root.destroy()