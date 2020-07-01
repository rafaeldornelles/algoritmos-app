from View.CasosPorDataView import CasosPorDataView


class CasosPorDataController:
    def __init__(self, data, infoCasos):
        view = CasosPorDataView(data, infoCasos)
        while True:
            event, values = view.read()
            if event == 'voltar':
                break

        view.close()