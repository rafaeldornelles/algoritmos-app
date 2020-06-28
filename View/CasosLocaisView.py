from PySimpleGUI import PySimpleGUI as sg

from Model.Locais import Locais
from Services.LocalServices import LocalServices


class CasosLocaisView:
    def __init__(self, window:sg.Window, locais:[Locais]):
        self.window = window
        self.locais = locais

    def render(self):
        layout = [
            [sg.Table([[local.nome, local.casos] for local in self.locais], headings=('Local', 'Casos'))]
        ]
        self.window.layout(layout)
        return self.window.read()

print(CasosLocaisView(sg.Window(''), locais=LocalServices().listar()).render())