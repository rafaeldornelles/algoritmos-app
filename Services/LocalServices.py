import json

import requests

from Parser.LocalParser import LocalParser


class LocalServices:
    def listar(self):
        r = requests.get('http://localhost:8000/api/locais')
        locais = [LocalParser.dictToLocal(local) for local in r.json()]
        return locais

    def cadastrar(self, local):
        dict = LocalParser.localToDict(local)
        print(json.dumps(dict))
        r = requests.post('http://localhost:8000/api/locais', json.dumps(dict))
        print(r.text)
        local = LocalParser.dictToLocal(r.json())
        return local