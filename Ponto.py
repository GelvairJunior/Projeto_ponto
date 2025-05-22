import sqlite3


class Ponto_register():
    def register(self, id_funcionario, data_registro, hora_entrada, hora_saida, hora_almoço, localização, tipo_ponto, status):
        self.id_funcionario = id_funcionario
        self.data_registro = data_registro
        self.hora_entrada = hora_entrada
        self.hora_saida = hora_saida
        self.hora_almoço = hora_almoço
        self.localização = localização
        self.tipo_ponto = tipo_ponto
        self.status = status

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
