class Bairro:
    def __init__(self, id, descricao, casos = None):
        self.id = id
        self.descricao = descricao
        if casos != None:
            self.casos = casos

    def __str__(self):
        return f'{self.id} - {self.descricao}'