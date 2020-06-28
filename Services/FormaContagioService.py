import requests

from Parser.FormaContagioParser import FormaContagioParser


class FormaContagioService:
    def listar(self):
        r = requests.get("http://localhost:8000/api/formascontagio")
        formasContagio = [FormaContagioParser.dictToFormaContagio(formaContagio) for formaContagio in r.json()]
        return formasContagio