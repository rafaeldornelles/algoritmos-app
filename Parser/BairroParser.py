from Model.Bairro import Bairro


class BairroParser:
    @staticmethod
    def dictToBairro(dict):
        id = dict['id']
        descricao = dict['descricao']
        casos = None
        if 'casos' in dict.keys():
            casos = dict['casos']

        return Bairro(id, descricao, casos)

    @staticmethod
    def bairroToDict(bairro:Bairro):
        dict = {
            "id": bairro.id,
            "descricao": bairro.descricao,
            "casos":bairro.casos
        }

        return dict