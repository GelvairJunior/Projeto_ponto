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

class Contrato():
    def __init__(self, inicio_contrato, fim_contrato, salario, cargo):
        self.inicio_contrato = inicio_contrato
        self.fim_contrato = fim_contrato
        self.salario = salario
        self.cargo = cargo
    

class Funcionario():
    def __init__(self, name, cpf, data_nascimento, endereço: Endereço, contrato: Contrato):
        self.name = name
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereço = endereço
        self.contrato = contrato
    
    def bater_ponto(self,):
        self.null
        
    def justificativa(self,):
        self.null
        
    def banco_horas(self,):
        self.null    
        
        
    def cadastrar_funcionarios(self, name, cpf, data_nascimento, endereço: Endereço, contrato: Contrato):

        with sqlite3.connect(self.server.db_path) as connection:
            cursor = connection.cursor()


            insert_query = '''
                INSERT INTO FUNCIONARIO (NAME, CPF, DATA_NASCIMENTO, ENDEREÇO, INICIO_DO_CONTRATO, FIM_DO_CONTRATO, SALARIO, CARGO)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            '''

            funcionario_inf = (name, cpf, data_nascimento, endereço, contrato.inicio_contrato, contrato.fim_contrato, contrato.salario, contrato.cargo)

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
    
    def Atualizar_Funcionario(self, ID, name, cpf, data_nascimento, endereço: Endereço, contrato: Contrato):

        with sqlite3.connect(self.server.db_path) as connection:
            cursor = connection.cursor()

            update_query = '''
            UPDATE FUNCIONARIO
            SET NAME = ?, CPF, DATA_NASCIMENTO = ?, ENDEREÇO, INICIO_DO_CONTRATO, FIM_DO_CONTRATO, SALARIO CARGO = ?
            WHERE ID_FUNCIONARIO = ?;
            '''

            cursor.execute(update_query, (name, cpf, data_nascimento, endereço, contrato.inicio_contrato, contrato.fim_contrato, contrato.salario, contrato.cargo, ID))

            connection.commit()

            print(f"Funcionario {self.name} foi atualizado/corrigido")

    def Deletar_Funcionario(self, ID, name, motivo):

        with sqlite3.connect(self.server.db_path) as connection:
            cursor = connection.cursor()
            
            select_query = '''
            SELECT * FROM FUNCIONARIO
            WHERE ID_FUNCIONARIO = ?;
            '''
            
            cursor.execute(select_query, (ID,))
            funcionario = cursor.fetchone()

            if not funcionario:
                print(f"Nenhum funcionário encontrado com ID {ID}.")

            insert_saidas = '''
            INSERT INTO SAIDAS
            (ID_FUNCIONARIO_SAIDA, NAME, CPF, DATA_NASCIMENTO, ENDEREÇO, INICIO_DO_CONTRATO, FIM_DO_CONTRATO, SALARIO, CARGO, MOTIVO)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
            '''

            funcionario_com_motivo = funcionario + (motivo,)
            cursor.execute(insert_saidas, funcionario_com_motivo)

            delete_query = '''
            DELETE FROM FUNCIONARIO
            WHERE ID_FUNCIONARIO = ?;
            '''
            cursor.execute(delete_query, (ID,))

            connection.commit()

            print(f"Funcionário {name} deletado e movido para pelo motivo: {motivo}")
