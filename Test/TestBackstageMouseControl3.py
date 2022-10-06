import win32gui, win32ui, win32con, win32api
from time import sleep

VK_KEY_A = 0x41
VK_KEY_B = 0x42
VK_KEY_P = 0x50
VK_KEY_L = 0x4C
VK_KEY_E = 0x45
VK_KEY_7 = 0x37

def main():
    window_name = '未命名 - 小畫家'
    hwnd = win32gui.FindWindow(None, window_name)
    print(get_inner_windows(hwnd))
    hwnd = get_inner_windows(hwnd)['Afx:00007FF6B63C0000:8']
    sleep(1)
    positionInWindow(hwnd)
    win32gui.SetForegroundWindow(hwnd)
    # press_key(hwnd, VK_KEY_7)
    doClick(hwnd, 500, 100)
    doClick(hwnd, 50, 300)
    doClick(hwnd, 500, 500)
    drag(hwnd, 500, 100, 50, 300)
    drag(hwnd, 50, 300, 500, 500)
    drag(hwnd, 500, 500, 500, 100)

    # win.SendMessage(win32con.WM_KEYDOWN, 0x32, 0)
    # sleep(0.01)
    # win.SendMessage(win32con.WM_KEYUP, 0x32, 0)
    # get_inner_windows(hwnd)

def list_window_names():
    '列舉視窗名稱'
    def winEnumHandler(hwnd, ctx):
        print(hex(hwnd), '"' + win32gui.GetWindowText(hwnd) + '"')
    win32gui.EnumWindows(winEnumHandler, None)


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
    sleep(0.5)
    # win32gui.PostMessage(hwnd, win32con.WM_KEYUP, key, 0)


def doClick(hwnd, x, y):
    long_position = win32api.MAKELONG(x, y)
    win32gui.PostMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, long_position)
    sleep(2)
    win32gui.PostMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, long_position)


def drag(hwnd, x1, y1, x2, y2):
    long_position1 = win32api.MAKELONG(x1, y1)
    long_position2 = win32api.MAKELONG(x2, y2)
    win32gui.PostMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, long_position1)
    sleep(1)
    win32gui.PostMessage(hwnd, win32con.WM_MOUSEMOVE, 0, long_position2)
    sleep(1)
    win32gui.PostMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, long_position2)


def positionInWindow(hwnd):
    tempt = win32api.GetCursorPos()
    print('tempt',tempt)

    windowRec = win32gui.GetWindowRect(hwnd)
    print('windowRec', windowRec)

    x = tempt[0] - windowRec[0]
    y = tempt[1] - windowRec[1]
    print('position', x, y)



main()