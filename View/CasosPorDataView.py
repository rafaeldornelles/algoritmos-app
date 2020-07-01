from PySimpleGUI import PySimpleGUI as sg

class CasosPorDataView:
    def __init__(self, data, info):
        self.window = sg.Window('Covidometro Poa')
        layout = [
            [sg.Text(f'Informações sobre o dia {data}')],
            [sg.Text(f'Casos acumulados no dia:'), sg.Text(info['casosAcumulados'])],
            [sg.Text(f'Casos ativos no dia:'), sg.Text(info['casosAtivos'])],
            [sg.Text(f'Casos registrados no dia:'), sg.Text(info['casosRegistrados'])],
            [sg.Text(f'Pessoas cujos sintomas iniciaram no dia:'), sg.Text(info['casosInicioSintomas'])],
            [sg.Text(f'Pessoas recuperadas no dia:'), sg.Text(info['recuperadosDia'])],
            [sg.Button('Voltar', key='voltar')]
        ]

        self.window.layout(layout)

    def read(self):
        self.window.un_hide()
        return self.window.read()

    def hide(self):
        self.window.hide()

    def close(self):
        self.window.close()