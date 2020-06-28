import requests

from Parser.SintomaParser import SintomaParser


class SintomaServices:
    def listar(self):
        r = requests.get('http://localhost:8000/api/sintomas')
        sintomas = [SintomaParser.dictToSintoma(sintoma) for sintoma in r.json()]
        return sintomas