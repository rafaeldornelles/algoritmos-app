from PySimpleGUI import PySimpleGUI as sg

from Services.BairroServices import BairroServices


class CadastrarUsuarioView:
    def __init__(self, bairros):
        self.layout = [
            [sg.Text('Cadastrar Caso')],
            [sg.Text('Passo 1 de 3: Cadastrar Usuário')],
            [sg.Text('Preencha todos os campos', text_color='red', visible=False, key='erro')],
            [sg.Text('Insira seus dados')],
            [sg.Text('Nome:'), sg.InputText(key='nome')],
            [sg.Text('Bairro:'), sg.InputCombo(bairros, key='bairro')],
            [sg.Button('Próximo', key='next')]
        ]
        self.window = sg.Window('Covidometro Poa')
        self.window.layout(self.layout)

    def read(self):
        return self.window.read()

    def mostrarMensagemErro(self):
        self.window.find_element('erro').Update(visible=True)

    def close(self):
        self.window.close()