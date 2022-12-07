from Controllers.statusController import statusController
from Controllers.clickController import clickController
from Controllers.hwndController import hwndController
from Views.view import View
from PyQt6.QtWidgets import QApplication
import sys

if __name__ == '__main__':
    # FGO = Controller()
    # FGO.main()
    # QApplication(sys.argv)
    FGO_view = View(statusController(), clickController(), hwndController())
    FGO_view.main()