from PySimpleGUI import PySimpleGUI as sg

from Model.Locais import Locais
from Services.LocalServices import LocalServices


class CasosLocaisView:
    def __init__(self, locais:[Locais]):
        self.window = sg.Window('Covidometro Poa')
        layout = [
            [sg.Table([[local.nome, local.casos] for local in locais], headings=['Local', 'Casos'])],
            [sg.Button('Voltar', key='Voltar')]
        ]
        self.window.layout(layout)

    def read(self):
        return self.window.read()

    def close(self):
        self.window.close()

