from Controllers.CadastrarCasoController import CadastrarCasoController
from Model.Paciente import Paciente
from Services.BairroServices import BairroServices
from View.CadastrarCasoView import CadastrarCasoView
from View.CadastrarUsuarioView import CadastrarUsuarioView


class CadastrarUsuarioController:
    def __init__(self):
        bairros = BairroServices().listar()
        view = CadastrarUsuarioView(bairros)
        while True:
            event, values = view.read()
            if event == 'next':
                if values['nome'] == '' or values['bairro'] == '':
                    view.mostrarMensagemErro()
                else:
                    paciente = Paciente(0, values['nome'], values['bairro'], [])
                    CadastrarCasoController(paciente)
                    break
            elif event == None:
                break
