from Controllers.CadastrarLocaisVisitadosController import CadastrarLocaisVisitadosController
from Model.Caso import Caso
from Services.BairroServices import BairroServices
from Services.FormaContagioService import FormaContagioService
from Services.SintomaServices import SintomaServices
from View.CadastrarCasoView import CadastrarCasoView
from datetime import datetime

class CadastrarCasoController:
    def __init__(self, paciente):
        formasContagio = FormaContagioService().listar()
        sintomas = SintomaServices().listar()
        view = CadastrarCasoView(formasContagio, sintomas)
        while True:
            event, values = view.read()
            if event == 'next':
                print(values)
                if values['fcontagio'] == "" or values['datasintomas'] == '':
                    view.mostrarErro()
                else:
                    #verificar se a pessoa marcou ao menos um sintoma
                    sintomasMarcados = [sintoma for sintoma in sintomas if values[sintoma.descricao] == True]
                    if len(sintomasMarcados) == 0:
                        view.nenhumSintoma()

                    else:
                        caso = Caso(0, paciente, values['fcontagio'], datetime.strptime(values['datasintomas'], '%d/%m/%Y'), datetime.now(), None, sintomasMarcados)
                        if values['datafimsintomas'] != '':
                            caso.dataFimSintomas = datetime.strptime(values['datafimsintomas'], '%d/%m/%Y')
                        CadastrarLocaisVisitadosController(caso)
