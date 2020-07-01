from datetime import datetime, timedelta

from Controllers.CasosBairroController import CasosBairroController
from Controllers.CasosBairrosController import CasosBairrosController
from Controllers.CasosLocaisController import CasosLocaisController
from Controllers.CasosLocalController import CasosLocalController
from Controllers.CasosPorDataController import CasosPorDataController
from Services.BairroServices import BairroServices
from Services.CasoServices import CasoServices
from Services.LocalServices import LocalServices
from Services.SintomaServices import SintomaServices
from View.CasosGeralView import CasosGeralView


class CasosGeralController:
    def __init__(self):
        self.casoServices = CasoServices()
        self.casos = self.casoServices.listar()
        infoCasos = self.getInfoCasos()
        bairros = BairroServices().listar()
        locais = LocalServices().listar()

        view = CasosGeralView(infoCasos, bairros, locais)
        while True:
            event, values = view.read()
            view.esconderErros()
            if event == 'verTodosBairros':
                view.hide()
                CasosBairrosController(bairros)

            elif event == 'verTodosLocais':
                view.hide()
                CasosLocaisController(locais)

            elif event == 'pesquisaPorData':
                view.hide()
                data = values['data']
                if data == "":
                    view.nenhumaData()
                    continue

                infoCasosData = self.getInfoDia(data)
                CasosPorDataController(data, infoCasosData)

            elif event == 'verBairro':
                if values['bairro'] == '':
                    view.nenhumBairro()
                    continue
                view.hide()
                CasosBairroController(values['bairro'])

            elif event == 'verLocal':
                print(values)
                if values['local'] == '':
                    view.nenhumLocal()
                    continue
                view.hide()
                CasosLocalController(values['local'])







    def getInfoCasos(self):
        ontem = datetime.now() - timedelta(days=1)
        ontemStr = ontem.strftime('%Y-%m-%d')

        totalCasos = len(self.casos)

        novosCasos = len([caso for caso in self.casos if caso.dataRelato.strftime('%Y-%m-%d') == ontemStr])

        sintomasFrequencia = {}
        for sintoma in SintomaServices().listar():
            sintomaPerc = len([caso for caso in self.casos if sintoma in caso.sintomas]) / len(self.casos)
            sintomasFrequencia[sintoma.descricao] = sintomaPerc
        sintomasFrequencia = {k:v for k,v in sorted(sintomasFrequencia.items(), key=lambda x:x[1], reverse=True)} #ordenando os casos



        return{
            "totalCasos":totalCasos,
            "novosCasos":novosCasos,
            "sintomasFrequencia": sintomasFrequencia
        }

    def getInfoDia(self, data):
        data = datetime.strptime(data, '%d/%m/%Y').date()

        casosAcumulados = 0
        casosAtivos = 0
        recuperadosDia = 0
        recuperadosTotal = 0
        casosRegistrados = 0
        casosInicioSintomas = 0

        for caso in self.casos:
            if caso.dataRelato.date() == data:
                casosRegistrados +=1
            if caso.dataInicioSintomas.date() == data:
                casosInicioSintomas += 1

            if caso.dataFimSintomas == None:
                casosAtivos += 1
            else:
                recuperadosTotal +=1
                if caso.dataFimSintomas.date() == data:
                    recuperadosDia +=1
                elif caso.dataFimSintomas > data:
                    casosAtivos +=1

            if caso.dataRelato.date() <= data:
                casosAcumulados +=1

        return{
            "casosAtivos":casosAtivos,
            "recuperadosDia":recuperadosDia,
            "recuperadosTotal":recuperadosTotal,
            "casosRegistrados":casosRegistrados,
            "casosInicioSintomas":casosInicioSintomas,
            "casosAcumulados": casosAcumulados
        }
