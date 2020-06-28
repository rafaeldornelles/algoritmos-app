import requests

from Parser.BairroParser import BairroParser


class BairroServices:
    def listar(self):
        r = requests.get('http://localhost:8000/api/bairros')
        bairros = [BairroParser.dictToBairro(bairro) for bairro in r.json()]
        return bairros
