from PySimpleGUI import PySimpleGUI as sg

class CadastrarCasoConfirmarView:
    def __init__(self, caso):
        self.nomeLabel = sg.Text(caso.paciente.nome)
        self.bairroLabel = sg.Text(caso.paciente.bairro)
        self.locaisVisitadosLabel = sg.Text(', '.join([local.nome for local in caso.paciente.locaisVisitados]))
        self.dataInicioSintomasLabel = sg.Text(caso.dataInicioSintomas.strftime('%d/%m/%Y'))
        self.formaContagioLabel = sg.Text(caso.formaContagio)
        self.sintomasLabel = sg.Text(', '.join([sintoma.descricao for sintoma in caso.sintomas]))
        self.dataFimSintomas = sg.Text(caso.dataFimSintomas.strftime('%d/%m/%Y')) if caso.dataFimSintomas != None else sg.Text('-')

        self.window = sg.Window('Covidometro Poa')

        layout = [
            [sg.Text('Cadastrar Caso')],
            [sg.Text('Confirme os dados:')],
            [sg.Text('Dados do Paciente', font=('helvetica', 12, 'bold'))],
            [sg.Text('Nome:'), self.nomeLabel],
            [sg.Text('Bairro:'), self.bairroLabel],
            [sg.Text('Locais Visitados:'), self.locaisVisitadosLabel],
            [sg.Text('Dados dos Sintomas:', font=('helvetica', 12, 'bold'))],
            [sg.Text('Data de Inicio dos Sintomas: '), self.dataInicioSintomasLabel],
            [sg.Text('Forma de Contágio:'), self.formaContagioLabel],
            [sg.Text('Sintomas:'), self.sintomasLabel],
            [sg.Text('Data de fim dos sintomas:'), self.dataFimSintomas],
            [sg.Button('Cadastrar', key='ok')]
        ]
        self.window.layout(layout)

    def read(self):
        return self.window.read()


    def sucessoPopup(self):
        sg.popup('Caso cadastrado com sucesso')

    def close(self):
        self.window.close()