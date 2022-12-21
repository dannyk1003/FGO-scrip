from Controllers.statusController import statusController
from Controllers.clickController import clickController
from Controllers.hwndController import hwndController
from Views.view import View
from PyQt6.QtWidgets import QApplication
import os

print(os.path.dirname(os.path.realpath(__file__)))

if __name__ == '__main__':
    # FGO = Controller()
    # FGO.main()
    # QApplication(sys.argv)
    path = os.path.dirname(os.path.realpath(__file__))
    FGO_view = View(statusController(path), clickController(path), hwndController(path), path)
    FGO_view.main()