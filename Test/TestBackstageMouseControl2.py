import win32gui, win32ui, win32con, win32api
from time import sleep

VK_KEY_A = 0x41
VK_KEY_B = 0x42
VK_KEY_P = 0x50
VK_KEY_L = 0x4C
VK_KEY_E = 0x45


def main():
    window_name = 'TestBackstageMouseControl2.txt - 記事本'
    hwnd = win32gui.FindWindow(None, window_name)
    print(get_inner_windows(hwnd))
    hwnd = get_inner_windows(hwnd)['RichEditD2DPT']
    # {'RichEditD2DPT': 198836, 'Windows.UI.Composition.DesktopWindowContentBridge': 133290, 'Windows.UI.Input.InputSite.WindowClass': 133314}
    # win = win32ui.CreateWindowFromHandle(hwnd)
    # win.SendMessage(win32con.WM_CHAR, ord('A'), 0)
    # win.SendMessage(win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    # win.SendMessage(win32con.WM_KEYUP, win32con.VK_RETURN, 0)
    # win.SendMessage(win32con.WM_CHAR, ord('B'), 0)

    # win32gui.SetForegroundWindow(hwnd)
    sleep(1)
    press_key(hwnd, VK_KEY_A, 0.5)
    press_key(hwnd, VK_KEY_P, 0.5)
    press_key(hwnd, VK_KEY_P, 0.5)
    press_key(hwnd, VK_KEY_L, 0.5)
    press_key(hwnd, VK_KEY_E, 0.5)
    doClick(hwnd, 50, 200)


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


def press_key(hwnd, key, sec):
    win32gui.PostMessage(hwnd, win32con.WM_KEYDOWN, key, 0)
    sleep(sec)
    win32gui.SendMessage(hwnd, win32con.WM_KEYUP, key, 0)


def doClick(hwnd, cx, cy):
    long_position = win32api.MAKELONG(cx, cy)
    win32gui.PostMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.VK_LBUTTON, long_position)



main()