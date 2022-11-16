from Controllers.statusController import statusController
from Controllers.clickController import clickController
from Views.view import View

if __name__ == '__main__':
    # FGO = Controller()
    # FGO.main()
    FGO_view = View(statusController(), clickController())
    FGO_view.main()