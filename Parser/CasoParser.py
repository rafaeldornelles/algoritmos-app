from datetime import datetime

from Model.Caso import Caso
from Parser.FormaContagioParser import FormaContagioParser
from Parser.PacienteParser import PacienteParser
from Parser.SintomaParser import SintomaParser


class CasoParser:
    @staticmethod
    def dictToCaso(dict):
        id = dict['id']
        paciente = PacienteParser.dictToPaciente(dict['paciente'])
        formaContagio = FormaContagioParser.dictToFormaContagio(dict['formaContagio'])
        dataInicioSintomas = datetime.strptime(dict['dataInicioSintomas'], '%Y-%m-%d')
        dataRelato = datetime.strptime(dict['dataRelato'], '%Y-%m-%d')
        dataFimSintomas = datetime.strptime(dict['dataFimSintomas'], '%Y-%m-%d') if dict['dataFimSintomas'] != None else None
        sintomas = [SintomaParser.dictToSintoma(sintoma) for sintoma in dict['sintomas']]

        return Caso(id, paciente, formaContagio, dataInicioSintomas, dataRelato, dataFimSintomas, sintomas)

    @staticmethod
    def casoToDict(caso:Caso):
        dict = {
            "id": caso.id,
            "paciente": PacienteParser.pacienteToDict(caso.paciente),
            "formaContagio": FormaContagioParser.formaContagioToDict(caso.formaContagio),
            "dataInicioSintomas": caso.dataInicioSintomas.strftime('%Y-%m-%d'),
            "dataRelato": caso.dataRelato.strftime('%Y-%m-%d'),
            "dataFimSintomas": caso.dataFimSintomas.strftime('%Y-%m-%d') if caso.dataFimSintomas != None else None,
            "sintomas": [SintomaParser.sintomaToDict(sintoma) for sintoma in caso.sintomas]
        }

        return dict
