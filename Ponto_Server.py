from tkinter import *
import cadastro


class Ponto_Server():

    def __init__(self):
        servidor = cadastro.Server()
        sistema = cadastro.Funcionario(servidor)

        window = Tk()
        window.geometry("600x600")
        window.title("Pagina de controle de informação dos funcionarios ")
        window.config(background="#2545d3")

        label = Label(window, text='Escolha uma opção: ')
        label.pack()

        button_Cadastro = Button(window, text="Cadastrar Funcionario")
        button_Cadastro.pack()
        

        button_Listar = Button(window, text="Listar Funcionarios")
        button_Listar.pack()

        button_atualizar = Button(window, text="Atualizar/Corrigir Cadastro do funcionario")
        button_atualizar.pack()

        button_deletar = Button(window, text="Deletar Funcionario")
        button_deletar.pack()

        button_sair = Button(window, text="Sair")
        button_sair.pack()


        button_Cadastro.config(command = sistema.cadastrar_funcionarios)
        button_Listar.config(command = sistema.Listar_Funcionarios)
        button_atualizar.config(command = sistema.Atualizar_Funcionario)
        button_deletar.config(command = sistema.Deletar_Funcionario)
        button_sair.config(command = self.sair)

        window.mainloop()  



    def sair(self):
        print("Até Mais :) ")
        exit()






if __name__ == "__main__":
    Janela = Ponto_Server()