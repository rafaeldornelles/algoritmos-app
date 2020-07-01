from PySimpleGUI import PySimpleGUI as sg


class CasosLocalView:
    def __init__(self, local):
        self.window = sg.Window('Covidometro Poa')

        layout = [
            [sg.Text(f'Casos no local {local.nome}')],
            [sg.Text(f'Total de casos: {local.casos}')],
            [sg.Button('voltar', key='voltar')]
        ]

        self.window.layout(layout)

    def read(self):
        return  self.window.read()

    def close(self):
        self.window.close()