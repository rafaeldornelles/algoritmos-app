from Model.Sintoma import Sintoma


class SintomaParser:
    @staticmethod
    def dictToSintoma(dict:{}):
        id = dict["id"]
        descricao = dict["descricao"]

        return Sintoma(id, descricao)

    @staticmethod
    def sintomaToDict(sintoma:Sintoma):
        dict = {
            "id": sintoma.id,
            "descricao": sintoma.descricao
        }

        return dict