import sqlite3
import Funcionario
from datetime import datetime

class cadastro():
    def __init__(self):
        self.server = Funcionario.Server()

    def cadastrar_funcionarios(self, name, cpf, data_nascimento, endereço: Funcionario.Endereço,  inicio_contrato, fim_contrato, salario, cargo):

        with sqlite3.connect(self.server.db_path) as connection:
            cursor = connection.cursor()


            insert_funcionario = '''
                INSERT INTO FUNCIONARIO (NAME, CPF, DATA_NASCIMENTO, ENDEREÇO, INICIO_DO_CONTRATO, FIM_DO_CONTRATO, SALARIO, CARGO)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            '''

            funcionario_inf = (name, cpf, data_nascimento, endereço, inicio_contrato, fim_contrato, salario, cargo)

            cursor.execute(insert_funcionario, funcionario_inf)
            connection.commit()

            print('funcionario cadastrado agora o login e senha dele')
            login = input('Login: ')
            senha = input('Senha: ')
            autoridade = input('Qual é o nivel de autorização do funcionario: ')

            id_funcionario = cursor.lastrowid

            insert_query = '''
                INSERT INTO LOGIN (ID_FUNCIONARIO, LOGIN, SENHA, AUTORIDADE)
                VALUES (?, ?, ?, ?)
            '''

            funcionario_cadas = (id_funcionario, login, senha, autoridade)

            cursor.execute(insert_query, funcionario_cadas)
            connection.commit()

            print('Login criado')

if __name__ == '__main__':
    name = input('Digite seu nome: ')
    cpf = input('Digite seu CPF: ')
    data_nascimento = input('Digite sua data de nascimento: ')
    endereço = input('Digite seu endereço:')
    inicio_contrato = input('Digite a data do inicio do contrato: ')
    fim_contrato = input('Digite a data do fim do contrato: ')
    salario = input('Digite o salario: ')
    cargo = input('Digite cargo: ')


    cadastro_obj = cadastro()
    cadastro_obj.cadastrar_funcionarios(name, cpf, data_nascimento, endereço, inicio_contrato, fim_contrato, salario, cargo)
