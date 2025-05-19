import sqlite3 
from tkinter import *


class Server():
    def __init__(self, db_path='ponto.db'):
        self.db_path = db_path

class Endereço():
    def __init__(self, rua, cidade, estado, cep):
        self.Rua = rua
        self.Cidade = cidade
        self.Estado = estado
        self.Cep = cep
    
    def __str__(self):
        return f"{self.Rua}, {self.Cidade} - {self.Estado}, {self.Cep}"


class Funcionario():
    def __init__(self, server):
        self.server = server

    def cadastrar_funcionarios(self, name, cpf, data_nascimento, endereço, inicio_contrato, fim_contrato, salario, cargo):
    
        self.Name = name
        self.CPF = cpf
        self.Data_nascimento = data_nascimento
        self.Endereço = endereço
        self.Inicio_contrato = inicio_contrato
        self.Fim_contrato = fim_contrato
        self.Salario = salario
        self.Cargo = cargo

        with sqlite3.connect(self.server.db_path) as connection:
            cursor = connection.cursor()


            insert_query = '''
                INSERT INTO FUNCIONARIO (NAME, CPF, DATA_NASCIMENTO, ENDEREÇO, INICIO_DO_CONTRATO, FIM_DO_CONTRATO, SALARIO, CARGO)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            '''

            funcionario_inf = (name, cpf, data_nascimento, str(endereço), inicio_contrato, fim_contrato, salario, cargo)

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
        
        self.ID = ID
        self.Name = name
        self.CPF = cpf
        self.Data_nascimento = data_nascimento
        self.Endereço = endereço
        self.Inicio_contrato = inicio_contrato
        self.Fim_contrato = fim_contrato
        self.Salario = salario
        self.Cargo = cargo

        with sqlite3.connect(self.server.db_path) as connection:
            cursor = connection.cursor()

            update_query = '''
            UPDATE FUNCIONARIO
            SET NAME = ?, CPF, DATA_NASCIMENTO = ?, ENDEREÇO, INICIO_DO_CONTRATO, FIM_DO_CONTRATO, SALARIO CARGO = ?
            WHERE ID_FUNCIONARIO = ?;
            '''

            print(f"Qual o ID {ID}")

            cursor.execute(update_query, (name, cpf, data_nascimento, str(endereço), inicio_contrato, fim_contrato, salario, cargo, ID))

            connection.commit()

            print(f"Funcionario {name} foi atualizado/corrigido")

    def Deletar_Funcionario(self, ID, name):
        
        self.ID = ID
        self.Name = name

        with sqlite3.connect(self.server.db_path) as connection:
            cursor = connection.cursor()

            delete_query = '''
            DELETE FROM FUNCIONARIO
            WHERE ID_FUNCIONARIO = ?;
            '''

            ID = int(input("Qual é o ID do funcionario que quer remover? "))
            name = str(input("Qual o nome do funcionario? "))

            cursor.execute(delete_query, (ID,))

            connection.commit()

            print(f"Funcionario {name} Deletado")
            res = str(input("Quer Deletar algum mais funcionario:(sim/nao) "))