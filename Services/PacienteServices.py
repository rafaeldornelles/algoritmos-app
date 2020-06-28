import requests

from Model.Paciente import Paciente
from Parser.PacienteParser import PacienteParser
import json


class PacienteServices:
    def listar(self): #get post put e delete
        r = requests.get('http://localhost:8000/api/pacientes')
        pacientes = [PacienteParser.dictToPaciente(paciente) for paciente in r.json()]
        return pacientes

    def buscarPorId(self, id):
        r = requests.get(f'http://localhost:8000/api/pacientes/{id}')
        paciente = PacienteParser.dictToPaciente(r.json())
        return paciente

    def cadastrar(self, paciente:Paciente):
        dict = PacienteParser.pacienteToDict(paciente)
        r = requests.post('http://localhost:8000/api/pacientes', json.dumps(dict))
        print(r.text)
        paciente = PacienteParser.dictToPaciente(r.json())
        return paciente

    def atualizar(self, paciente):
        dict = PacienteParser.pacienteToDict(paciente)
        r = requests.put('http://localhost:8000/api/pacientes', json.dumps(dict))
        paciente = PacienteParser.dictToPaciente(r.json())
        return paciente

    def deletar(self, paciente):
        r = requests.delete(f'http://localhost:8000/api/pacientes/{paciente.id}')
        paciente = PacienteParser.dictToPaciente(r.json())
        return paciente