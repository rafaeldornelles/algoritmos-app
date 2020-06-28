from Model.FormaContagio import FormaContagio


class FormaContagioParser:
    @staticmethod
    def dictToFormaContagio(dict):
        id = dict['id']
        descricao = dict['descricao']

        return FormaContagio(id, descricao)

    @staticmethod
    def formaContagioToDict(bairro:FormaContagio):
        dict = {
            "id": bairro.id,
            "descricao": bairro.descricao
        }

        return dict