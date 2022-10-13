import tkinter as tk
import tkinter.messagebox as msg # messagebox要另行匯入，否則會出錯。
from tkinter import ttk
import win32api, win32gui
import numpy as np


def hwnd_list():   
    title = dict()
    windows = []
    def get_all_title(hwnd, mouse):
        if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
            title.update({hwnd:win32gui.GetWindowText(hwnd)})
    mouse = 0
    win32gui.EnumWindows(get_all_title,mouse)

    for hwnd, title in title.items():
        if title != "":
            windows.append([hwnd, title])

    return windows


def get_inner_windows(whnd1):
    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            hwnds[win32gui.GetClassName(hwnd)] = hwnd
        return True
    hwnds = {}
    win32gui.EnumChildWindows(whnd1, callback, hwnds)
    return hwnds


def get_hwnd(window_name):
    hwnd = win32gui.FindWindow(None, window_name)
    # print(get_inner_windows(hwnd))
    # hwnd = get_inner_windows(hwnd)['Afx:00007FF6B63C0000:8']
    return hwnd

     
root = tk.Tk()
root.title('my window')
root.geometry('200x150')


def combobox_selected(event):
     print(mycombobox.current(), comboboxText.get())
     labelText.set('the window name is ' + comboboxText.get())
     return comboboxText.get()


comboboxText = tk.StringVar()
mycombobox = ttk.Combobox(root, textvariable=comboboxText, state='readonly')
mycombobox['values'] = list(np.array(hwnd_list())[:,1])
mycombobox.current(3)
mycombobox.bind('<<ComboboxSelected>>', combobox_selected)
mycombobox.grid(row=1, column=1)


labelText = tk.StringVar()
mylabel = tk.Label(root, textvariable=labelText, height=5, font=('Arial', 12))
mylabel.grid(row=2, column=1)


comboboxText1 = tk.StringVar()
mycombobox1 = ttk.Combobox(root, textvariable=comboboxText1, state='readonly')
mycombobox1['values'] = list(get_inner_windows(get_hwnd(combobox_selected(5))))
mycombobox1.grid(row=3, column=1)

root.mainloop()