# Hwnd
import sys

# sys.path.append('..')

from Models.hwndModel import hwndModel

class hwndController:
    def __init__(self, path):
        self.model = hwndModel(path)
        self.path = path


    def connection(self, window, innerWindow):
        result = self.model.connection(window, innerWindow)
        return result

    
    def get_window_list(self):
        result = self.model.get_window_list()
        print(result)
        return result


    def get_hwnd_list(self):
        self.model.get_all_windows()
        result = self.model.hwnds_list
        return result

    
    def get_inner_hwnds_list(self, hwnd):
        self.model.get_inner_windows(hwnd)
        result = self.model.inner_hwnds_list
        return result


    def get_inner_window_list(self, hwnd):
        result = self.model.get_inner_window_list(hwnd)
        return result

    
    def get_hwnd(self, window_name):
        self.model.get_hwnd(window_name)
        result = self.model.hwnd
        return result


    def get_inner_hwnd(self, window, innerWindow):
        result = self.model.get_inner_hwnd(window, innerWindow)
        return result