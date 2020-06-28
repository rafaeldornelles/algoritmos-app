from Controllers.CadastrarUsuarioController import CadastrarUsuarioController
from Controllers.CasosGeralController import CasosGeralController
from View.MenuInicialView import MenuInicialView


class MenuInicialController:
    def __init__(self):
        event, _ = MenuInicialView().read()
        print(event)
        if event == 1:
            CasosGeralController()
        elif event == 2:
            CadastrarUsuarioController()