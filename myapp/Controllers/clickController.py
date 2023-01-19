# 點擊流程
# import tkinter.messagebox
import threading
import inspect
import ctypes


from Models.clickModel import clickModel

class clickController:
    def __init__(self, path, app):
        self.path = path
        self.model = clickModel(path, app)
        self.thread_start = 'No'

    
    def _async_raise(self, tid, exctype):
        tid = ctypes.c_long(tid)
        if not inspect.isclass(exctype):
            exctype = type(exctype)

        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
        if res == 0:
            raise ValueError('invalid thread id')
        elif res != 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
            raise SystemError('PyThreadState_SetAsync failed')

    def stop_thread(self, thread):
        self._async_raise(thread.ident, SystemExit)

    
    def start(self, now_status_support, now_status_skill, apple, time, hwnd, innerHwnd):
        # result = self.model.get_window()

        if self.thread_start == 'No':
            self.thread_start = threading.Thread(target=self.runScrip, args = (now_status_support, now_status_skill, apple, time, hwnd, innerHwnd))
            self.thread_start.start()


    def end(self):
        if self.thread_start == 'No':
            print('No Thread')
        else:
            self.stop_thread(self.thread_start)
            print(self.thread_start)
            self.thread_start = 'No'

    
    def runScrip(self, now_status_support, now_status_skill, apple, time, hwnd, innerHwnd):
        print('abc')
        self.model.status_init(now_status_support, now_status_skill, apple, hwnd, innerHwnd)
        self.model.now_step()
        print('def')

        for i in range(time):
            print('now is times:', i)
            self.model.runScrip()
        self.thread_start = 'No'
        print('success')
        # tkinter.messagebox.showinfo("Info", "Scrip End")
    
    def control(self, innerHwnd):
        print(innerHwnd)
        self.control_set = True
        if self.control_set == True:
            self.model.no_control(innerHwnd)
            self.control_set = False
        else:
            self.model.control(innerHwnd)
            self.control_set = True

        
    

    # def on_button_click(self, text, func, now_status_support=None, now_status_skill=None, time = None):
    #     result = None
    #     if func == 'start':
    #         result = self.model.get_window()
    #         print('clickController', now_status_support, now_status_skill)
    #         # self.model.runScrip()
    #         # thread_start = threading.Thread(target=self.model.runScrip, )
    #         # thread_start.start()
    #         if self.thread_start == 'No':
    #             self.thread_start = threading.Thread(target=self.runScrip, args = (now_status_support, now_status_skill, time))
    #             self.thread_start.start()
    #     elif func == 'end':
    #         if self.thread_start == 'No':
    #             print('No Thread')
    #         else:
    #             self.stop_thread(self.thread_start)
    #             print(self.thread_start)
    #             self.thread_start = 'No'

    #     print(result)
    #     # return result
