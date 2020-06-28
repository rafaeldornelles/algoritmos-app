class Locais:
    def __init__(self, id, nome, endereco, casos = None):
        self.id = id
        self.nome = nome
        self.endereco = endereco
        if casos != None:
            self.casos = casos

    def __str__(self):
        return self.nome
