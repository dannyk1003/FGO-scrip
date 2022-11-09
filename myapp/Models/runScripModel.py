import threading
import time
from clickModel import Model

class Scrip(Model):
    def __init__(self):
        self.model = Model()

    def main():
        pass

    def runScrip(self):

        if self.connect == 'Success': # 連線成功

            self.window_to_front()
            # win32gui.MoveWindow(self.hwnd, True, True, 934, 540, True)
            # time.sleep(0.5)

            self.doClick(self.mission)
            time.sleep(1)
            for times in range(self.times): # 次數大於一次時
                print('剩餘次數', self.times)
                print('第', times, '次')

                self.AP_recovery()

                self.select_support()

                # mission_start_location = self.locateOnImage('mission_start', 'ScreenShot')
                # if mission_start_location != None:
                #     self.doClick(mission_start_location)


                for i in range(1, 4):
                    self.startBattle(i)
                    
                print('battle end')
                
                self.go_again()
                self.times -= 1

                

            print('success')

