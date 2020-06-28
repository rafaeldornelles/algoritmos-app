from Model.Paciente import Paciente
from Parser.BairroParser import BairroParser
from Parser.LocalParser import LocalParser


class PacienteParser:
    @staticmethod
    def dictToPaciente(dict):
        id = dict['id']
        nome = dict['nome']
        bairro = BairroParser.dictToBairro(dict['bairro'])
        locaisVisitados = [LocalParser.dictToLocal(local) for local in dict['locaisVisitados']]

        return Paciente(id, nome, bairro, locaisVisitados)

    @staticmethod
    def pacienteToDict(paciente:Paciente):
        dict = {
            "id": paciente.id,
            "nome": paciente.nome,
            "bairro": BairroParser.bairroToDict(paciente.bairro),
            "locaisVisitados": [LocalParser.localToDict(local) for local in paciente.locaisVisitados]
        }

        return dict