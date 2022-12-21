# 找尋hwnd
import win32gui
import sys
import numpy as np

class hwndModel:
    def __init__(self, path):
        self.path = path

        self.window = ''
        self.innerWindow = ''
        self.hwnd = ''
        self.innerHwnd = ''
        self.connect = ''


    def connection(self, window, innerWindow):
        self.window = window
        self.innerWindow = innerWindow

        self.hwnd = win32gui.FindWindow(None, self.window)

        if self.hwnd == 0:
            self.connect = 'Fail'

        else:

            def get_inner_windows(hwnd):
                def callback(hwnd, hwnds):
                    if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
                        hwnds[win32gui.GetClassName(hwnd)] = hwnd
                    return True
                hwnds_dict = dict()
                win32gui.EnumChildWindows(hwnd, callback, hwnds_dict)

                return hwnds_dict
            if get_inner_windows(self.hwnd) == {}:
                self.connect = 'Fail'
            else:
                self.innerHwnd = get_inner_windows(self.hwnd)[self.innerWindow]
                print(self.hwnd, self.innerHwnd)
                self.connect = 'Success'
        
        return self.connect


    def get_all_windows(self):
        '''
        Return all hwnds
        '''
        all_hwnds_dict = dict()
        hwnds_dict = dict()
        hwnds_list = list()
        def get_all_title(hwnd, mouse):
            if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
                all_hwnds_dict.update({hwnd:win32gui.GetWindowText(hwnd)})
        mouse = 0
        win32gui.EnumWindows(get_all_title,mouse)

        for hwnd, title in all_hwnds_dict.items():
            if title != "":
                hwnds_list.append([hwnd, title])
                hwnds_dict.update({hwnd: title})

        self.hwnds_list = hwnds_list
        self.hwnds_dict = hwnds_dict

    
    def get_window_list(self):
        self.get_all_windows()

        return list(np.array(self.hwnds_list)[:,1])



    def get_inner_windows(self, hwnd):
        '''
        Return all inner hwnds
        '''
        def callback(hwnd, hwnds):
            if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
                hwnds[win32gui.GetClassName(hwnd)] = hwnd
            return True
        hwnds_dict = dict()
        hwnds_list = list()
        win32gui.EnumChildWindows(hwnd, callback, hwnds_dict)

        for title, hwnd in hwnds_dict.items():
            hwnds_list.append([hwnd, title])
        
        if hwnds_list == []:
            self.inner_hwnds_list = [[self.hwnd, self.window]]
        else:
            self.inner_hwnds_list = hwnds_list
            self.inner_hwnds_dict = hwnds_dict


    def get_inner_window_list(self, hwnd):
        self.get_inner_windows(hwnd)
        
        return list(np.array(self.inner_hwnds_list)[:,1])


    def get_hwnd(self, window_name):
        self.hwnd = win32gui.FindWindow(None, window_name)


    def get_inner_hwnd_list(self, hwnd):
        self.get_inner_windows(hwnd)

        return list(np.array(self.inner_hwnds_list)[:,0])
        

    def get_inner_hwnd(self, window, innerWindow):
        self.get_hwnd(window)
        self.get_inner_windows(self.hwnd)
        print(innerWindow)
        print(self.inner_hwnds_dict)
        self.innerHwnd = self.inner_hwnds_dict[innerWindow]

        return self.innerHwnd
