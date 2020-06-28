from Model.Locais import Locais


class LocalParser:
    @staticmethod
    def dictToLocal(dict):
        id = dict['id']
        nome = dict['nome']
        endereco = dict['endereco']
        casos = None
        if 'casos' in dict.keys():
            casos = dict['casos']

        return Locais(id, nome, endereco, casos)

    @staticmethod
    def localToDict(local: Locais):
        dict = {
            "id": local.id,
            "nome": local.nome,
            "endereco": local.endereco,
        }
        try:
            dict['casos'] = local.casos
        except:
            pass

        return dict
