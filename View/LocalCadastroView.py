from PySimpleGUI import PySimpleGUI as sg
class LocalCadastroView:
    def __init__(self):
        self.window = sg.Window('Covidometro Poa')
        layout = [
            [sg.Text('Nome:'), sg.InputText(key='nome')],
            [sg.Text('Endereço:'), sg.InputText(key='endereco')],
            [sg.Button('Cadastrar', key='cadastrar')]
        ]
        self.window.layout(layout)

    def read(self):
        return self.window.read()

    def close(self):
        self.window.close()