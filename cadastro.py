import sqlite3 
import tkinter as tk

class Server():
    def __init__(self, db_path='ponto.db'):
        self.db_path = db_path

class Funcionario():
    def __init__(self, server):
        self.server = server

    def cadastrar_funcionarios(self):
        with sqlite3.connect(self.server.db_path) as connection:
            cursor = connection.cursor()

            res = 'sim'
    
            while res.lower() == 'sim':
                Name = input('Escreva seu nome: ')
                data_nascimento = input('Digite sua data de nascimento: ')
                cargo = input('Qual é o seu Cargo: ')

                insert_query = '''
                    INSERT INTO FUNCIONARIO (NAME, DATA_NASCIMENTO, CARGO)
                    VALUES (?, ?, ?)
                '''

                funcionario_inf = (Name, data_nascimento, cargo)

                cursor.execute(insert_query, funcionario_inf)
                connection.commit()

                print('Funcionário Cadastrado com Sucesso')

                res = input('Ainda tem mais funcionarios para cadastrar? (sim/nao): ')

    def Listar_Funcionarios(self):
        with sqlite3.connect(self.server.db_path) as connection:

            cursor = connection.cursor()

            select_query = "SELECT * FROM FUNCIONARIO;"

            cursor.execute(select_query)

            funcionarios = cursor.fetchall()

            print("Aqui todos os Funcionarios cadastrados e seus cargos: ")
            for funcionario in funcionarios:
                print(funcionario)
    
    def Atualizar_Funcionario(self):
        res = 'sim'
    
        while res.lower() == 'sim':
            with sqlite3.connect(self.server.db_path) as connection:
                cursor = connection.cursor()

                update_query = '''
                UPDATE FUNCIONARIO
                SET NAME = ?, DATA_NASCIMENTO = ?, CARGO = ?
                WHERE ID_FUNCIONARIO = ?;
                '''

                id = int(input("Qual é o ID do funcionario que quer modificar? "))
                nome = input("Corrigir o nome: ")
                nascimento = input("Corrigir Data de nascimento: ")
                cargo = input("Qual é o Cargo atualizado: ")

                cursor.execute(update_query, (nome, nascimento, cargo, id))

                connection.commit()

                print(f"Funcionario {nome} foi atualizado/corrigido")

                res = str(input("Tem mais alguem para atualizar?(sim/nao) "))

    def Deletar_Funcionario(self):
        res = "sim"

        while res.lower() == "sim":
            with sqlite3.connect(self.server.db_path) as connection:
                cursor = connection.cursor()

                delete_query = '''
                DELETE FROM FUNCIONARIO
                WHERE ID_FUNCIONARIO = ?;
                '''

                id = int(input("Qual é o ID do funcionario que quer remover? "))
                nome = str(input("Qual o nome do funcionario? "))

                cursor.execute(delete_query, (id,))

                connection.commit()

                print(f"Funcionario {nome} Deletado")
                res = str(input("Quer Deletar algum mais funcionario:(sim/nao) "))


if __name__ == "__main__":
    servidor = Server()
    sistema = Funcionario(servidor)

    escolha = 0
    while escolha < 5:
    
        escolha = int(input('O que deseja fazer? \n [1] Cadastrar Funcionario \n [2] Listar Funcionarios \n [3] Atualizar/corrigir Funcionario \n [4] Deletar Funcionario \n [5] Sair \n : '))

        if escolha == 1:
            sistema.cadastrar_funcionarios()

        if escolha == 2:
            sistema.Listar_Funcionarios()

        if escolha == 3:
            sistema.Atualizar_Funcionario()

        if escolha == 4:
            sistema.Deletar_Funcionario()
    print("Até mais :) ")