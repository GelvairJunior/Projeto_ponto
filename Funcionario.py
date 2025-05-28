import sqlite3 
from tkinter import *
from email_validator import validate_email, EmailNotValidError
from phonenumbers.phonenumberutil import NumberParseException
import phonenumbers
from datetime import datetime
import geocoder

import Ponto

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
        return (self.rua, self.cidade, self.estado, self.cep)    
        
class Contatos():
    def __init__(self, celular, email):
        self.celular = celular
        self.email = email
    
    def email_validaçao(self):
        try: 
            validate_email(self.email, check_deliverability=True)
            return (True)
        except EmailNotValidError:
            return False 
    
    def celular_validaçao(self):
        try:
            numero = phonenumbers.parse(self.celular, "BR")
            phonenumbers.is_valid_number(numero)
            return True
        except NumberParseException:
            return False
    
    def validar_contatos(self):
        return self.email_validaçao() and self.celular_validaçao()

class Contrato():
    def __init__(self, inicio_contrato, fim_contrato, salario, cargo):
        self.inicio_contrato = inicio_contrato
        self.fim_contrato = fim_contrato
        self.salario = salario
        self.cargo = cargo
    
    def __str__(self):
        return (self.inicio_contrato, self.fim_contrato, self.salario, self.cargo)

class Cadastro():
    
    def __init__(self, name, cpf, data_nascimento, contatos: Contatos, endereço: Endereço, contrato: Contrato ):
        self.name = name
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereço = endereço
        self.contrato = contrato
        self.contatos = contatos
        self.server = Server()

    def cadastrar_funcionarios(self, login, senha, autoridade):

        with sqlite3.connect(self.server.db_path) as connection:
            cursor = connection.cursor()


            insert_funcionario = '''
                INSERT INTO FUNCIONARIO (NAME, CPF, DATA_NASCIMENTO, CELULAR, EMAIL, RUA, CIDADE, ESTADO, CEP, INICIO_DO_CONTRATO, FIM_DO_CONTRATO, SALARIO, CARGO)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            '''

            funcionario_inf = (self.name, self.cpf, self.data_nascimento, self.contatos.celular, self.contatos.email, self.endereço.rua, self.endereço.cidade, self.endereço.estado, self.endereço.cep, self.contrato.inicio_contrato, self.contrato.fim_contrato, self.contrato.salario, self.contrato.cargo)

            cursor.execute(insert_funcionario, funcionario_inf)
            connection.commit()

            id_funcionario = cursor.lastrowid

            insert_query = '''
                INSERT INTO LOGIN (IDLOGIN, SENHA, AUTORIDADE)
                VALUES (?, ?, ?)
            '''

            funcionario_cadas = (id_funcionario, login, senha, autoridade)

            cursor.execute(insert_query, funcionario_cadas)
            connection.commit()


class Funcionario():
    def __init__(self, ID_funcionario, login, senha):
        self.ID_funcionario = ID_funcionario
        self.login = login
        self.senha = senha
        self.server = Server()

    def alterar(self, new_senha):
        with sqlite3.connect(self.server.db_path) as connection:
            cursor = connection.cursor()

            update_query = '''
            UPDATE LOGIN
            SET SENHA = ?
            WHERE LOGIN = ?;
            '''

            cursor.execute(update_query, (new_senha, self.login))

            connection.commit()

    def ponto(self):
        bater_ponto = Ponto.Ponto_register(self.ID_funcionario)
        return bater_ponto()
    
    def ponto_aplicado(self):
        bater_aplicado = Ponto.Ponto_register_aplicado(self.ID_funcionario)
        return bater_aplicado()


class Analista(Funcionario):
    def __init__(self, login, senha):
        super().__init__(login, senha)

    def Listar_Funcionarios(self):
        
        with sqlite3.connect(self.server.db_path) as connection:

            cursor = connection.cursor()

            select_query = "SELECT * FROM FUNCIONARIO;"

            cursor.execute(select_query)

            funcionarios = cursor.fetchall()

            print("Aqui todos os Funcionarios cadastrados e seus cargos: ")
            for funcionario in funcionarios:
                print(funcionario)


class RH(Analista):
    def __init__(self, ID, name, cpf, data_nascimento, endereço: Endereço, contatos: Contatos, contrato: Contrato, login, senha):
        super().__init__(login, senha)
        self.ID = ID
        self.name = name
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.contatos = contatos
        self.endereço = endereço
        self.contrato = contrato
        self.server = Server()
    
    def Atualizar_Funcionario(self):

        with sqlite3.connect(self.server.db_path) as connection:
            cursor = connection.cursor()

            update_query = '''
            UPDATE FUNCIONARIO
            SET NAME = ?, CPF, DATA_NASCIMENTO = ?, CELULAR = ?, EMAIL = ?, RUA, CIDADE, ESTADO, CEP, INICIO_DO_CONTRATO, FIM_DO_CONTRATO = ?, SALARIO CARGO = ?
            WHERE ID_FUNCIONARIO = ?;
            '''

            cursor.execute(update_query, (self.name, self.cpf, self.data_nascimento,  self.contatos.celular, self.contatos.email, self.endereço.rua, self.endereço.cidade, self.endereço.estado, self.endereço.cep, self.contrato.inicio_contrato, self.contrato.fim_contrato, self.contrato.salario, self.contrato.cargo, self.ID))

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
            (ID_FUNCIONARIO_SAIDA, NAME, CPF, DATA_NASCIMENTO, CELULAR, EMAIL, RUA, CIDADE, ESTADO, CEP, INICIO_DO_CONTRATO, FIM_DO_CONTRATO, SALARIO, CARGO)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
            '''

            funcionario_com_motivo = funcionario + (motivo, ID)
            cursor.execute(insert_saidas, funcionario_com_motivo)

            delete_funcionario = '''
            DELETE FROM FUNCIONARIO
            WHERE ID_FUNCIONARIO = ?;
            '''
            
            delete_login = '''
            DELETE FROM LOGIN
            WHERE ID_FUNCIONARIO = ?;
            '''
            
            cursor.execute(delete_funcionario, delete_login, (ID,))

            connection.commit()

            print(f"Funcionário {name} deletado e movido para pelo motivo: {motivo}")
            
    def alterar_ponto(self):
        alterar_ponto = Ponto.Ponto_register_modificado(self.ID_funcionario)
        return alterar_ponto()
