from PySimpleGUI import PySimpleGUI as sg

from Services.LocalServices import LocalServices


class CadastrarLocaisVisitadosView:
    def __init__(self, locais):
        self.window = sg.Window('Covidometro Poa')
        self.locais = locais

        layout = [
            [sg.Text('Cadastrar Caso')],
            [sg.Text('Passo 3 de 3: (opcional) Informe os locais os quais visitou até dois dias antes do início dos sintomas')],
            [sg.Listbox(self.locais, select_mode=sg.SELECT_MODE_MULTIPLE, size=(100,10), key='locais')],
            [sg.Button('Adicionar Novo Local', key='cadlocal')],
            [sg.Button('Cadastrar', key='cadfinal')]

        ]
        self.window.layout(layout)

    def read(self):
        return self.window.read()

    def atualizarLocais(self):
        self.window.find_element('locais').update(values=self.locais)

    def close(self):
        self.window.close()

