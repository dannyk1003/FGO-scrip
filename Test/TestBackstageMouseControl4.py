import win32gui, win32ui, win32con, win32api
from time import sleep


VK_KEY_7 = 0x37
VK_KEY_E = 0x45
VK_KEY_A = 0x41



def main():
    window_name = 'BlueStacks App Player'
    hwnd = get_hwnd(window_name)
    win32gui.SetForegroundWindow(hwnd)
    doClick(hwnd, 0, 0)
    doClick(hwnd, 688, 422)
    doClick(hwnd, 861, 425)
    doClick(hwnd, 1025, 418)
    doClick(hwnd, 1189, 654)
    doClick(hwnd, 865, 645)
    doClick(hwnd, 1006, 535)
    doClick(hwnd, 1345, 756)





def get_hwnd(window_name):
    hwnd = win32gui.FindWindow(None, window_name)
    print(get_inner_windows(hwnd))
    hwnd = get_inner_windows(hwnd)['Qt5154QWindowIcon']
    return hwnd


def get_inner_windows(whnd1):
    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            hwnds[win32gui.GetClassName(hwnd)] = hwnd
        return True
    hwnds = {}
    win32gui.EnumChildWindows(whnd1, callback, hwnds)
    return hwnds


def press_key(hwnd, key):
    win32gui.PostMessage(hwnd, win32con.WM_KEYDOWN, key, 0)
    sleep(2)


def doClick(hwnd, x, y):
    long_position = win32api.MAKELONG(x, y)
    win32gui.PostMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, long_position)
    sleep(2)
    win32gui.PostMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, long_position)


main()