from PySimpleGUI import PySimpleGUI as sg

from Services.LocalServices import LocalServices


class CasosGeralView:
    def __init__(self, info):
        self.novosCasos = info['novosCasos']
        self.sintomasComuns = info['sintomasComuns']
        self.totalCasos = info['totalCasos']

    def render(self, window):
        layout = [
            [sg.Text('Resumo dos casos:')],
            [sg.Text(f'{self.totalCasos} casos suspeitos cadastrados')],
            [sg.Text(f'{self.novosCasos} novos casos suspeitos')],
            [sg.Text(f'Sintomas mais comuns:')],
            [sg.Text(self.sintomasComuns)],
            [sg.Text(f'Pesquisar por Bairro:')],
            [sg.InputText(), sg.Button('Pesquisar'), sg.Button('Ver Todos')],
            [sg.Text(f'Pesquisar por Data:')],
            [sg.InputText(disabled=True),sg.CalendarButton('Selecionar Data'), sg.Button('Pesquisar')],
            [sg.Text(f'Pesquisar por Local:')],
            [sg.InputCombo(LocalServices().listar()), sg.Button('Pesquisar'), sg.Button('Ver todos')],
        ]
        window.layout(layout)
        return window.read()

