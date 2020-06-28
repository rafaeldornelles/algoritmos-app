from PySimpleGUI import PySimpleGUI as sg

class CadastrarCasoSucessoView:
    def __init__(self, window):
        self.window = window

    def render(self):
        layout = [
            [sg.Text('Usuário Cadastrado com sucesso')],
            [sg.Button('Voltar')]
        ]
        self.window.layout(layout)
        self.window.read()

CadastrarCasoSucessoView(sg.Window('')).render()