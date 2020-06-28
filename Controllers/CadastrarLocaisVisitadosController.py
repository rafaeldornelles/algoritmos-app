from Controllers.CadastrarCasoConfirmarController import CadastrarCasoConfirmarController
from Model.Locais import Locais
from Services.LocalServices import LocalServices
from View.CadastrarLocaisVisitadosView import CadastrarLocaisVisitadosView
from View.LocalCadastroView import LocalCadastroView


class CadastrarLocaisVisitadosController:
    def __init__(self, caso):
        service = LocalServices()
        locais = service.listar()

        view = CadastrarLocaisVisitadosView(locais)
        while True:
            event, values = view.read()
            if event == 'cadlocal': #evento de cadastrar local
                cadastroView = LocalCadastroView()
                e,v = cadastroView.read()
                if e == 'cadastrar':
                    local = Locais(0, v['nome'], v['endereco'])
                    local.id = service.cadastrar(local)
                    locais.append(local)
                    view.atualizarLocais()
                    cadastroView.close()


            elif event == 'cadfinal':
                caso.paciente.locaisVisitados = values['locais']
                view.close()
                CadastrarCasoConfirmarController(caso)
                break