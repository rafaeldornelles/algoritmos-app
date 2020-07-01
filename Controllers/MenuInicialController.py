from Controllers.CadastrarUsuarioController import CadastrarUsuarioController
from Controllers.CasosGeralController import CasosGeralController
from View.MenuInicialView import MenuInicialView


class MenuInicialController:
    def __init__(self):
        view = MenuInicialView()
        while True:
            event, _ = view.read()
            print(event)
            if event == 'ver':
                view.hide()
                CasosGeralController()
            elif event == 'cadastrar':
                view.hide()
                CadastrarUsuarioController()
            elif event == None:
                break