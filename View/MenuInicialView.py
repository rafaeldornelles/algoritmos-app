from PySimpleGUI import PySimpleGUI as sg

class MenuInicialView:
    def __init__(self):
        layout = [
            [sg.Text('Covidômetro Poa')],
            [sg.Text('Selecione a opção desejada:')],
            [sg.Button('Ver casos', key='ver')],
            [sg.Button('Cadastrar caso suspeito', key='cadastrar')]
        ]
        self.window = sg.Window('Covidometro Poa')
        self.window.layout(layout)

    def read(self):
        return self.window.read()

    def close(self):
        self.window.close()