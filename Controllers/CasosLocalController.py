from View.CasosLocalView import CasosLocalView


class CasosLocalController:
    def __init__(self, local):
        view = CasosLocalView(local)

        while True:
            event, values = view.read()
            if event == 'voltar':
                break

        view.close()