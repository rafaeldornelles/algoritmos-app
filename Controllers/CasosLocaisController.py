from View.CasosLocaisView import CasosLocaisView


class CasosLocaisController:
    def __init__(self, locais):
        view = CasosLocaisView(locais)

        while True:
            event, values = view.read()
            if event == 'Voltar':
                break

        view.close()