from Model import Locais
from Model.Bairro import Bairro


class Paciente:
    def __init__(self, id, nome, bairro:Bairro, locaisVisitados:[Locais]):
        self.id = id
        self.nome = nome
        self.bairro = bairro
        self.locaisVisitados = locaisVisitados

    def __str__(self):
        return self.nome