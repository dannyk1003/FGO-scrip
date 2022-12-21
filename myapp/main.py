from Controllers.statusController import statusController
from Controllers.clickController import clickController
from Controllers.hwndController import hwndController
from Views.view import View
from Logs.log import getLog
import os

print(os.path.dirname(os.path.realpath(__file__)))

if __name__ == '__main__':
    path = os.path.dirname(os.path.realpath(__file__))
    # FGO = Controller()
    # FGO.main()
    # QApplication(sys.argv)
    logger = getLog(path)
    logger.returnLog().info('test')

    
    FGO_view = View(statusController(path), clickController(path), hwndController(path), path)
    FGO_view.main()