from Services.CasoServices import CasoServices
from Services.PacienteServices import PacienteServices
from View.CadastrarCasoConfirmarView import CadastrarCasoConfirmarView


class CadastrarCasoConfirmarController():
    def __init__(self, caso):
        view = CadastrarCasoConfirmarView(caso)
        while True:
            event, values = view.read()

            if event == 'ok':
                caso.paciente.id = PacienteServices().cadastrar(caso.paciente).id
                caso.id = CasoServices().cadastrar(caso).id

                view.sucessoPopup()
                view.close()
                break