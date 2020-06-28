from PySimpleGUI import PySimpleGUI as sg

from Services.BairroServices import BairroServices
from Services.CasoServices import CasoServices


class CasosBairrosView:
    def __init__(self, window, bairros=None):
        print('a')
        self.window = window
        self.bairros = bairros
        print(self.bairros)

    def render(self):
        layout = [
            [sg.Table([[bairro.descricao, bairro.casos] for bairro in self.bairros], headings=["Bairro", "Casos"], select_mode=sg.TABLE_SELECT_MODE_NONE)],
            [sg.Button('Voltar')]
        ]
        self.window.layout(layout)
        self.window.read()


CasosBairrosView(sg.Window(''), BairroServices().listar()).render()
