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
        button_Cadastro.config(command = self.cadastrar_funcionarios)
        button_Cadastro.pack()
        

        button_Listar = Button(window, text="Listar Funcionarios")
        button_Listar.config(command = sistema.Listar_Funcionarios)
        button_Listar.pack()

        button_atualizar = Button(window, text="Atualizar/Corrigir Cadastro do funcionario")
        button_atualizar.config(command = self.Atualizar_Funcionario)
        button_atualizar.pack()

        button_deletar = Button(window, text="Deletar Funcionario")
        button_deletar.config(command = self.Deletar_Funcionario)
        button_deletar.pack()

        button_sair = Button(window, text="Sair")
        button_sair.config(command = self.sair)
        button_sair.pack()

        window.mainloop()

    def sair(self):
        print("Até Mais :) ")
        exit()

    def cadastrar_funcionarios(self):
        Cadastro_page()
    
    def Atualizar_Funcionario(self):
        Atualizar_page()
    
    def Deletar_Funcionario(self):
        Deletar_page()



class Cadastro_page():
    servidor = cadastro.Server()
    sistema = cadastro.Funcionario(servidor)

    def __init__(self):
        window = Toplevel()
        window.geometry("600x600")
        window.title("Pagina de controle de informação dos funcionarios ")
        window.config(background="#2545d3")

        label = Label(window, text='Vamos Cadastrar o funcionario')
        label.pack()

        label_name = Label(window, text="Nome")
        label_name.pack()
        self.entry_Name = Entry(window)
        self.entry_Name.pack()

        label_cpf = Label(window, text="CPF")
        label_cpf.pack()
        self.entry_cpf = Entry(window)
        self.entry_cpf.pack()

        labelnasc = Label(window, text="Data de Nascimento")
        labelnasc.pack()
        self.entry_DataNascimento = Entry(window)
        self.entry_DataNascimento.pack()

        label_rua = Label(window, text="RUA")
        label_rua.pack()
        self.entry_Rua = Entry(window)
        self.entry_Rua.pack()

        label_Cidade = Label(window, text="Cidade")
        label_Cidade.pack()
        self.entry_Cidade = Entry(window)
        self.entry_Cidade.pack()

        label_Estado = Label(window, text="Estado")
        label_Estado.pack()
        self.entry_Estado = Entry(window)
        self.entry_Estado.pack()

        label_cep = Label(window, text="Cep")
        label_cep.pack()
        self.entry_Cep = Entry(window)
        self.entry_Cep.pack()
        
        label_ini = Label(window, text="Data do Inicio do Contrato")
        label_ini.pack()
        self.entry_InicioContrato = Entry(window)
        self.entry_InicioContrato.pack()

        label_fim = Label(window, text="Data do Fim do Contrato")
        label_fim.pack()
        self.entry_FimContrato = Entry(window)
        self.entry_FimContrato.pack()

        label_salario = Label(window, text="Salario")
        label_salario.pack()
        self.entry_Salario = Entry(window)
        self.entry_Salario.pack()

        label_cargo = Label(window, text="Cargo")
        label_cargo.pack()
        self.entry_Cargo = Entry(window)
        self.entry_Cargo.pack()
        
        botao_obter = Button(window, text="Enviar as Informações", command=self.Cadastrar)
        botao_obter.pack()
        
        
        
        window.mainloop()

    def Cadastrar(self):
        name = self.entry_Name.get()
        cpf = self.entry_cpf.get()
        data_nascimento = self.entry_DataNascimento.get()
        Rua = self.entry_Rua.get()
        Cidade = self.entry_Cidade.get()
        Estado = self.entry_Estado.get()
        Cep = self.entry_Cep.get()
        inicio_contrato = self.entry_InicioContrato.get()
        fim_contrato = self.entry_FimContrato.get()
        salario = self.entry_Salario.get()
        cargo = self.entry_Cargo.get()

    
        endereço = (f"{Rua} {Cidade} {Estado} {Cep}")
        self.sistema.cadastrar_funcionarios(name, cpf, data_nascimento, endereço, inicio_contrato, fim_contrato, salario, cargo)
    


class Atualizar_page():
    servidor = cadastro.Server()
    sistema = cadastro.Funcionario(servidor)


    def __init__(self):
        window = Toplevel()
        window.geometry("600x600")
        window.title("Pagina de controle de informação dos funcionarios ")
        window.config(background="#2545d3")

        label = Label(window, text='Vamos Atualizar o funcionario')
        label.pack()
        
        label_ID = Label(window, text="Qual o ID do funcionario")
        label_ID.pack()
        self.entry_ID = Entry(window)
        self.entry_ID.pack

        label_name = Label(window, text="Nome")
        label_name.pack()
        self.entry_Name = Entry(window)
        self.entry_Name.pack()

        label_cpf = Label(window, text="CPF")
        label_cpf.pack()
        self.entry_cpf = Entry(window)
        self.entry_cpf.pack()

        labelnasc = Label(window, text="Data de Nascimento")
        labelnasc.pack()
        self.entry_DataNascimento = Entry(window)
        self.entry_DataNascimento.pack()

        label_rua = Label(window, text="RUA")
        label_rua.pack()
        self.entry_Rua = Entry(window)
        self.entry_Rua.pack()

        label_Cidade = Label(window, text="Cidade")
        label_Cidade.pack()
        self.entry_Cidade = Entry(window)
        self.entry_Cidade.pack()

        label_Estado = Label(window, text="Estado")
        label_Estado.pack()
        self.entry_Estado = Entry(window)
        self.entry_Estado.pack()

        label_cep = Label(window, text="Cep")
        label_cep.pack()
        self.entry_Cep = Entry(window)
        self.entry_Cep.pack()
        
        label_ini = Label(window, text="Data do Inicio do Contrato")
        label_ini.pack()
        self.entry_InicioContrato = Entry(window)
        self.entry_InicioContrato.pack()

        label_fim = Label(window, text="Data do Fim do Contrato")
        label_fim.pack()
        self.entry_FimContrato = Entry(window)
        self.entry_FimContrato.pack()

        label_salario = Label(window, text="Salario")
        label_salario.pack()
        self.entry_Salario = Entry(window)
        self.entry_Salario.pack()

        label_cargo = Label(window, text="Cargo")
        label_cargo.pack()
        self.entry_Cargo = Entry(window)
        self.entry_Cargo.pack()
        
        botao_obter = Button(window, text="Enviar as Informações", command=self.Atualizar)
        botao_obter.pack()
        
        
        
        window.mainloop()

    def Atualizar(self):
        ID = self.entry_ID.get()
        name = self.entry_Name.get()
        cpf = self.entry_cpf.get()
        Data_nascimento = self.entry_DataNascimento.get()
        Rua = self.entry_Rua.get()
        Cidade = self.entry_Cidade.get()
        Estado = self.entry_Estado.get()
        Cep = self.entry_Cep.get()
        Inicio_contrato = self.entry_InicioContrato.get()
        Fim_contrato = self.entry_FimContrato.get()
        Salario = self.entry_Salario.get()
        Cargo = self.entry_Cargo.get()
        
        endereço = (f"{Rua}, {Cidade}, {Estado}, {Cep}")
        self.sistema.cadastrar_funcionarios(ID, name, cpf, Data_nascimento, endereço, Inicio_contrato, Fim_contrato, Salario, Cargo)





class Deletar_page():
    servidor = cadastro.Server()
    sistema = cadastro.Funcionario(servidor)

    def __init__(self):
        window = Toplevel()
        window.geometry("600x600")
        window.title("Pagina de controle de informação dos funcionarios ")
        window.config(background="#2545d3")

        label = Label(window, text='Vamos Deletar o funcionario')
        label.pack()

        label_ID = Label(window, text="Qual o ID do funcionario")
        label_ID.pack()
        self.entry_ID = Entry(window)
        self.entry_ID.pack

        label_name = Label(window, text="Nome")
        label_name.pack()
        self.entry_Name = Entry(window)
        self.entry_Name.pack()

        window.mainloop()
    
    
    def Deletar(self):
        ID = self.entry_ID.get()
        name = self.entry_Name.get()

        self.sistema.cadastrar_funcionarios(ID, name)




if __name__ == "__main__":
    Janela = Ponto_Server()