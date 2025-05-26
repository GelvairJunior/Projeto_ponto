import sqlite3
import Funcionario
from datetime import datetime
import geocoder
import folium

class Ponto_register():
    def __init__(self, login, senha, Server):
        self.login = login
        self.senha = senha
        self.server = Server()


    def register(self):
        data_registro = datetime.now().strftime('%Y-%m-%d')
        status = ''
        return (data_registro)

    def entrada():
        hora_entrada = datetime.now().strftime('%H:%M:%S')
        tipo_ponto = "Tempo Real"
        return (hora_entrada, tipo_ponto)

    def almoco():
        hora_almoço = datetime.now().strftime('%H:%M:%S')
        return (hora_almoço)
    
    def saida():
        hora_saida = datetime.now().strftime('%H:%M:%S')
        return (hora_saida)


    def localização():
        localização = localização



class completar():
    def justificativa(self, id_funcionario, motivo_atraso, motivo_ausencia, atestado, solicitaçao):
        self.id_funcionario = id_funcionario
        self.motivo_atraso = motivo_atraso
        self.motivo_ausencia = motivo_ausencia
        self.atestado = atestado
        self.solicitaçao = solicitaçao

    def banco_de_horas(self, id_funcionario, horas, horas_previstas, horas_extras, folgas, folha):
        self.id_funcionario = id_funcionario
        self.horas = horas
        self.horas_previstas = horas_previstas
        self.horas_extras = horas_extras
        self.folgas = folgas
        self.folha = folha