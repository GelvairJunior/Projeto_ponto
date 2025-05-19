from tkinter import *
import cadastro


class Ponto_Server():
    
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


    def Atualizar():
        ID = entry_ID.get()
        Name = entry_Name.get()
        CPF = entry_CPF.get()
        Data_nascimento = entry_Data_nascimento.get()
        Rua = entry_Rua.get()
        Cidade = entry_Cidade.get()
        Estado = entry_Estado.get()
        Cep = entry_Cep.get()
        Inicio_contrato = entry_InicioContrato.get()
        Fim_contrato = entry_FimContrato.get()
        Salario = entry_Salario.get()
        Cargo = entry_Cargo.get()

    def Deletar():
        ID = entry_ID.get()
        Name = entry_Name.get()

    def sair(self):
        print("Até Mais :) ")
        exit()



class Cadastro_page():
    servidor = cadastro.Server()
    sistema = cadastro.Funcionario(servidor)

    window = Tk()
    window.geometry("600x600")
    window.title("Pagina de controle de informação dos funcionarios ")
    window.config(background="#2545d3")

    label = Label(window, text='Vamos Cadastraro o funcionario')
    label.pack()

    Label(window, text="Nome").grid(row=0, column=0)
    entry_Name = Entry(window)
    entry_Name.grid(row=0, column=1)

    Label(window, text="CPF").grid(row=1, column=0)
    entry_cpf = Entry(window)
    entry_cpf.grid(row=1, column=1)

    Label(window, text="Data de Nascimento").grid(row=2, column=0)
    entry_DataNascimento = Entry(window)
    entry_DataNascimento.grid(row=2, column=1)

    Label(window, text="RUA").grid(row=3, column=1)
    entry_Rua = Entry(window)
    entry_Rua.grid(row=3, column=1)

    Label(window, text="Cidade").grid(row=4, column=0)
    entry_Cidade = Entry(window)
    entry_Cidade.grid(row=4, column=1)

    Label(window, text="Estado").grid(row=5, column=0)
    entry_Estado = Entry(window)
    entry_Estado.grid(row=5, column=1)

    Label(window, text="Cep").grid(row=6, column=0)
    entry_Cep = Entry(window)
    entry_Cep.grid(row=6, column=1)

    Label(window, text="Data do Inicio do Contrato").grid(row=7, column=0)
    entry_InicioContrato = Label(window)
    entry_InicioContrato.grid(row=7, column=1)

    Label(window, text="Data do Fim do Contrato").grid(row=8, column=0)
    entry_FimContrato = Label(window)
    entry_FimContrato.grid(row=8, column=1)

    Label(window, text="Salario").grid(row=9, column=0)
    entry_Salario = Entry(window)
    entry_Salario.grid(row=9, column=1)

    Label(window, text="Cargo").grid(row=10, column=0)
    entry_Cargo = Entry(window)
    entry_Cargo.grid(row=10, column=1)

    def Cadastrar(self):
        Name = self.entry_Name.get()
        CPF = self.entry_CPF.get()
        Data_nascimento = self.entry_DataNascimento.get()
        Rua = self.entry_Rua.get()
        Cidade = self.entry_Cidade.get()
        Estado = self.entry_Estado.get()
        Cep = self.entry_Cep.get()
        Inicio_contrato = self.entry_InicioContrato.get()
        Fim_contrato = self.entry_FimContrato.get()
        Salario = self.entry_Salario.get()
        Cargo = self.entry_Cargo.get()

        self.sistema(Name, CPF, Data_nascimento, Rua, Cidade, Estado, Cep, Inicio_contrato, Fim_contrato, Salario, Cargo)
    
    window.mainloop()


class Atualizar_page():
    servidor = cadastro.Server()
    sistema = cadastro.Funcionario(servidor)

    window = Tk()
    window.geometry("600x600")
    window.title("Pagina de controle de informação dos funcionarios ")
    window.config(background="#2545d3")

    label = Label(window, text='Escolha uma opção: ')
    label.pack()



    window.mainloop()


class Deletar_page():
    servidor = cadastro.Server()
    sistema = cadastro.Funcionario(servidor)

    window = Tk()
    window.geometry("600x600")
    window.title("Pagina de controle de informação dos funcionarios ")
    window.config(background="#2545d3")

    label = Label(window, text='Escolha uma opção: ')
    label.pack()


    window.mainloop()


if __name__ == "__main__":
    Janela = Ponto_Server()