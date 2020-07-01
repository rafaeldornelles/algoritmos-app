from PySimpleGUI import  PySimpleGUI as sg

class CasosBairroView:
    def __init__(self, bairro):
        self.window = sg.Window('Covidometo Poa')

        layout = [
            [sg.Text(f'Casos no bairro {bairro.descricao}')],
            [sg.Text(f'Total de casos: {bairro.casos}')],
            [sg.Button("Voltar", key='voltar')]
        ]
        self.window.layout(layout)

    def read(self):
        return self.window.read()

    def close(self):
        self.window.close()