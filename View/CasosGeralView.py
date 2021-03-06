from PySimpleGUI import PySimpleGUI as sg

class CasosGeralView:
    def __init__(self, infoCasos, bairros, locais):
        self.novosCasos = infoCasos['novosCasos']
        self.sintomasComuns = infoCasos['sintomasFrequencia']
        self.totalCasos = infoCasos['totalCasos']

        self.bairros = bairros
        self.locais = locais

        self.window = sg.Window('Covidometro Poa')

        layout = [
                     [sg.Text('Resumo dos casos:')],
                     [sg.Text(f'{self.totalCasos} casos suspeitos cadastrados')],
                     [sg.Text(f'{self.novosCasos} novos casos suspeitos')],
                     [sg.Text(f'Sintomas mais comuns:')]
                 ] \
                 + \
                 [[sg.Text(f"{sintoma} - {round(frequencia * 100, 2)}% dos casos")] for sintoma, frequencia in self.sintomasComuns.items()] \
                 + \
                 [
                     [sg.Text(f'Pesquisar por Bairro:')],
                     [sg.Text('selecione um bairro', visible=False, key='erroBairro', text_color='red')],
                     [sg.InputCombo(self.bairros, key='bairro'), sg.Button('Pesquisar', key='verBairro'), sg.Button('Ver Todos', key='verTodosBairros')],
                     [sg.Text(f'Pesquisar por Data:')],
                     [sg.Text('Selecione uma data', visible=False, key='erroData', text_color='red')],
                     [sg.InputText(disabled=True, key='data'),sg.CalendarButton('Selecionar Data', format='%d/%m/%Y'), sg.Button('Pesquisar', key='pesquisaPorData')],
                     [sg.Text(f'Pesquisar por Local:')],
                     [sg.Text('selecione um local', visible=False, key='erroLocal', text_color='red')],
                     [sg.InputCombo(self.locais, key='local'), sg.Button('Pesquisar', key='verLocal'), sg.Button('Ver todos', key='verTodosLocais')],
                 ]

        print(layout)
        self.window.layout(layout)

    def read(self):
        self.window.un_hide()
        return self.window.read()

    def close(self):
        self.window.close()

    def hide(self):
        self.window.hide()

    def nenhumaData(self):
        self.window.find_element('erroData').update(visible=True)

    def nenhumBairro(self):
        self.window.find_element('erroBairro').update(visible=True)

    def esconderErros(self):
        self.window.find_element('erroData').update(visible=False)
        self.window.find_element('erroBairro').update(visible=False)
        self.window.find_element('erroLocal').update(visible=False)

    def nenhumLocal(self):
        self.window.find_element('erroLocal').update(visible=True)
