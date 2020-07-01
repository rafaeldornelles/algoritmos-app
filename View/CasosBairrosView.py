from PySimpleGUI import PySimpleGUI as sg

from Services.BairroServices import BairroServices
from Services.CasoServices import CasoServices


class CasosBairrosView:
    def __init__(self, bairros):
        print('a')
        self.window = sg.Window('Covidometro Poa')

        layout = [
            [sg.Table([[bairro.descricao, bairro.casos] for bairro in bairros], headings=["Bairro", "Casos"], select_mode=sg.TABLE_SELECT_MODE_NONE)],
            [sg.Button('Voltar')]
        ]
        self.window.layout(layout)

    def read(self):
        return self.window.read()

    def close(self):
        self.window.close()


