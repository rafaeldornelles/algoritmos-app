from PySimpleGUI import PySimpleGUI as sg

from Services.BairroServices import BairroServices
from Services.FormaContagioService import FormaContagioService
from Services.SintomaServices import SintomaServices


class CadastrarCasoView:
    def __init__(self, formasContagio, sintomas):
        self.window = sg.Window('Covidometro Poa')
        layout = [
            [sg.Text('Cadastrar Caso')],
            [sg.Text('Passo 2 de 3: Informações de caso')],
            [sg.Text('Preencha todos os campos obrigatórios', text_color='red', visible=False, key='error')],
            [sg.Text('Preencha pelo menos um sintoma', text_color='red', visible=False, key='sintomaerror')],
            [sg.Text('Forma de Infecção Provável(caso conhecida)'), sg.InputCombo(formasContagio, key='fcontagio')],
            [sg.Text('Data de Início de Sintomas:'),sg.InputText(disabled=True, tooltip='Pressione o botão selecionar', key='datasintomas'), sg.CalendarButton("Selecionar", format='%d/%m/%Y')],
            [sg.Text('(opcional) Data de Fim de Sintomas:)'), sg.InputText(disabled=True, tooltip='Pressione o botão selecionar', key='datafimsintomas'), sg.CalendarButton("Selecionar", format='%d/%m/%Y')],
            [sg.Text('Sintomas')],
            [sg.Checkbox(sintoma, key=sintoma.descricao) for sintoma in sintomas],
            [sg.Button('Próximo', key='next')]
        ]

        self.window.layout(layout)

    def read(self):
        return self.window.read()

    def mostrarErro(self):
        self.window.find_element('error').update(visible=True)

    def nenhumSintoma(self):
        self.window.find_element('sintomaerror').update(visible=True)
