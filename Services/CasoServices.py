import json

import requests

from Model.Caso import Caso
from Parser.CasoParser import CasoParser

class CasoServices:
    def listar(self):
        r = requests.get('http://localhost:8000/api/casos')
        casos = [CasoParser.dictToCaso(caso) for caso in r.json()]
        return casos

    def buscarPorId(self, id):
        r = requests.get(f'http://localhost:8000/api/casos/{id}')
        caso = CasoParser.dictToCaso(r.json())
        return caso

    def cadastrar(self, caso:Caso):
        dict = CasoParser.casoToDict(caso)
        r = requests.post('http://localhost:8000/api/casos', json.dumps(dict))
        print(r.text)
        caso = CasoParser.dictToCaso(r.json())
        return caso

    def atualizar(self, caso):
        dict = CasoParser.casoToDict(caso)
        r = requests.put('http://localhost:8000/api/casos', json.dumps(dict))
        caso = CasoParser.dictToCaso(r.json())
        return caso

    def deletar(self, caso):
        r = requests.delete(f'http://localhost:8000/api/casos/{caso.id}')
        caso = CasoParser.dictToCaso(r.json())
        return caso

    def listarPorBairro(self, idBairro):
        r = requests.get(f'http://localhost:8000/api/casos/bairro/{idBairro}')
        casos = [CasoParser.dictToCaso(caso) for caso in r.json()]
        return casos

    def listarPorLocal(self, idLocal):
        r = requests.get(f'http://localhost:8000/api/casos/local/{idLocal}')
        casos = [CasoParser.dictToCaso(caso) for caso in r.json()]
        return casos