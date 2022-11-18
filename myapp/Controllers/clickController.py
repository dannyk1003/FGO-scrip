# 點擊流程
import sys
import threading
import inspect
import ctypes

sys.path.append('..')

from Models.clickModel import clickModel

class clickController:
    def __init__(self):
        self.model = clickModel()
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

    
    def start(self, now_status_support, now_status_skill, time):
        result = self.model.get_window()

        if self.thread_start == 'No':
            self.thread_start = threading.Thread(target=self.runScrip, args = (now_status_support, now_status_skill, time))
            self.thread_start.start()


    def end(self):
            if self.thread_start == 'No':
                print('No Thread')
            else:
                self.stop_thread(self.thread_start)
                print(self.thread_start)
                self.thread_start = 'No'

    
    def runScrip(self, now_status_support, now_status_skill, time):
        for i in range(time):
            print('now is times:', i)
            self.model.runScrip(now_status_support, now_status_skill)
        
    

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
