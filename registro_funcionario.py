import sqlite3

class register():
    int.id_do_funcionario
    str.data_do_registro
    str.hora_de_entrada
    str.hora_de_saída
    locals.localização
    str.tipo_ponto
    str.status

class justificativa(register):
    str.motivo_de_atraso
    str.motivo_de_ausencia
    str.atestado
    str.solicitação

class banco_de_horas(register):
    int.horas
    int.horas_previstas
    int.horas_extras
    str.folgas
    str.folha

class correcao(banco_de_horas):
    str.modificar_horas
