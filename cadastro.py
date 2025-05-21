import sqlite3 
from tkinter import *


class Server():
    def __init__(self, db_path='ponto.db'):
        self.db_path = db_path

class Endereço():
    def __init__(self, rua, cidade, estado, cep):
        self.rua = rua
        self.cidade = cidade
        self.estado = estado
        self.cep = cep
    
    def __str__(self):
        return f"{self.rua}, {self.cidade} - {self.estado}, {self.cep}"


class Funcionario():
    servidor = Server()
    
    def __init__(self, server):
        self.server = server

    def cadastrar_funcionarios(self, name, cpf, data_nascimento, endereço, inicio_contrato, fim_contrato, salario, cargo):

        with sqlite3.connect(self.server.db_path) as connection:
            cursor = connection.cursor()


            insert_query = '''
                INSERT INTO FUNCIONARIO (NAME, CPF, DATA_NASCIMENTO, ENDEREÇO, INICIO_DO_CONTRATO, FIM_DO_CONTRATO, SALARIO, CARGO)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            '''

            funcionario_inf = (name, cpf, data_nascimento, endereço, inicio_contrato, fim_contrato, salario, cargo)

            cursor.execute(insert_query, funcionario_inf)
            connection.commit()

            print('Funcionário Cadastrado com Sucesso')

    def Listar_Funcionarios(self):
        
        with sqlite3.connect(self.server.db_path) as connection:

            cursor = connection.cursor()

            select_query = "SELECT * FROM FUNCIONARIO;"

            cursor.execute(select_query)

            funcionarios = cursor.fetchall()

            print("Aqui todos os Funcionarios cadastrados e seus cargos: ")
            for funcionario in funcionarios:
                print(funcionario)
    
    def Atualizar_Funcionario(self, ID, name, cpf, data_nascimento, endereço, inicio_contrato, fim_contrato, salario, cargo):

        with sqlite3.connect(self.server.db_path) as connection:
            cursor = connection.cursor()

            update_query = '''
            UPDATE FUNCIONARIO
            SET NAME = ?, CPF, DATA_NASCIMENTO = ?, ENDEREÇO, INICIO_DO_CONTRATO, FIM_DO_CONTRATO, SALARIO CARGO = ?
            WHERE ID_FUNCIONARIO = ?;
            '''

            cursor.execute(update_query, (name, cpf, data_nascimento, endereço, inicio_contrato, fim_contrato, salario, cargo, ID))

            connection.commit()

            print(f"Funcionario {self.name} foi atualizado/corrigido")

    def Deletar_Funcionario(self, ID, name):

        with sqlite3.connect(self.server.db_path) as connection:
            cursor = connection.cursor()

            delete_query = '''
            DELETE FROM FUNCIONARIO
            WHERE ID_FUNCIONARIO = ?;
            '''

            cursor.execute(delete_query, (ID,))

            connection.commit()

            print(f"Funcionario {name} Deletado")