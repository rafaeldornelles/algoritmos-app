from datetime import datetime

from Model.FormaContagio import FormaContagio
from Model.Paciente import Paciente
from Model.Sintoma import Sintoma


class Caso:
    def __init__(self, id, paciente:Paciente, formaContagio:FormaContagio, dataInicioSintomas:datetime, dataRelato:datetime, dataFimSintomas:datetime, sintomas:[Sintoma]):
        self.id = id
        self.paciente = paciente
        self.formaContagio = formaContagio
        self.dataInicioSintomas = dataInicioSintomas
        self.dataRelato = dataRelato
        self.dataFimSintomas = dataFimSintomas
        self.sintomas = sintomas

    def __str__(self):
        return f'{self.dataInicioSintomas} - {self.paciente}'