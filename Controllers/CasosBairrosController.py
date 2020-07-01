from View.CasosBairrosView import CasosBairrosView


class CasosBairrosController:
    def __init__(self, bairros):
        view = CasosBairrosView(bairros)
        while True:
            event, values = view.read()
            if event == 'Voltar':
                view.close()
                break