class Sintoma:
    def __init__(self, id, descricao):
        self.id = id
        self.descricao = descricao

    def __str__(self):
        return self.descricao