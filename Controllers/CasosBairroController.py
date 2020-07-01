from View.CasosBairroView import CasosBairroView


class CasosBairroController:
    def __init__(self, bairro):
        view = CasosBairroView(bairro)

        while True:
            event, value = view.read()
            if event == 'voltar':
                break

        view.close()
