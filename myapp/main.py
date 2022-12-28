from Logs.log import getLog
import os, sys
from PyQt6.QtWidgets import QApplication
app = QApplication(sys.argv)

print(os.path.dirname(os.path.realpath(__file__)))

try:

    if __name__ == '__main__':
        path = os.path.dirname(os.path.realpath(__file__))
        # FGO = Controller()
        # FGO.main()
        # QApplication(sys.argv)
        logger = getLog(path)
        

        from Controllers.statusController import statusController
        from Controllers.clickController import clickController
        from Controllers.hwndController import hwndController
        from Views.view import View

        logger.returnLog().info('main start')
        FGO_view = View(statusController(path), clickController(path, app), hwndController(path), path, logger)
        FGO_view.main()
        logger.returnLog().info('main end')

except Exception as e:
    logger.returnLog().error(e)