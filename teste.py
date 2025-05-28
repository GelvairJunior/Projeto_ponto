import sqlite3
from datetime import datetime
from email_validator import validate_email, EmailNotValidError
import phonenumbers
from phonenumbers.phonenumberutil import NumberParseException
import geocoder

class Server():
    def __init__(self, db_path='ponto.db'):
        self.db_path = db_path


class Ponto_register():

    def __init__(self, ID_funcionario):
        self.ID_funcionario = ID_funcionario
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


    def locali(self):
        g = geocoder.ip('me')
        if g.ok:
            latitude = g.latlng[0] or None,
            longitude = g.latlng[1] or None,
            rua = g.street or "Desconhecido",
            cidade = g.city or "Desconhecido",
            estado = g.state or "Desconhecido",
            cep = g.postal or "00000-000"
            return latitude, longitude, rua, cidade, estado, cep
        else:
            return None, None, "Desconhecido", "Desconhecido", "Desconhecido", "00000-000"


    def register(self):
        data_registro = datetime.now().strftime('%Y-%m-%d')
        tipo_ponto = "Tempo Real"
        status = "Registrado"
        
        with sqlite3.connect(self.server.db_path) as conn:
            cursor = conn.cursor()

            insert_ponto = '''
            INSERT INTO REGISTRO_PONTO (ID_FUNCIONARIO, DATA_REGISTRO, TYPE_PONTO, STATUS)
            VALUES (?, ?, ?, ?)
            '''
            cursor.execute(insert_ponto, (self.ID_funcionario, data_registro, tipo_ponto, status))
            id_ponto = cursor.lastrowid
            
            conn.commit()
            
        self.id_ponto = id_ponto
        return (id_ponto)

    def entrada(self, id_ponto):
        hora_entrada = datetime.now().strftime('%H:%M:%S')
        
        latitude, longitude, rua, cidade, estado, cep = self.locali()
        
        with sqlite3.connect(self.server.db_path) as conn:
            cursor = conn.cursor()

            update_query = '''
            UPDATE REGISTRO_PONTO
            SET HORA_ENTRADA = ?
            WHERE ID_PONTO = ?
            '''
            cursor.execute(update_query, (hora_entrada, id_ponto))

            insert_local = '''
            INSERT INTO LOCALIZACAO (ID_PONTO, LONGITUDE, LATITUDE, RUA, CIDADE, ESTADO, CEP, TIPO)
            VALUES (?, ?, ?, ?, ?, ?, ?, 'Entrada')
            '''
            cursor.execute(insert_local, (id_ponto, longitude, latitude, rua, cidade, estado, cep))

            conn.commit()        
        
    def almoco(self, id_ponto):
        hora_almoço = datetime.now().strftime('%H:%M:%S')
        
        latitude, longitude, rua, cidade, estado, cep = self.locali()
        
        with sqlite3.connect(self.server.db_path) as conn:
            cursor = conn.cursor()

            update_query = '''
            UPDATE REGISTRO_PONTO
            SET TIME_ALMOÇO = ?
            WHERE ID_PONTO = ?
            '''
            cursor.execute(update_query, (hora_almoço, id_ponto))

            insert_local = '''
            INSERT INTO LOCALIZACAO (ID_PONTO, LONGITUDE, LATITUDE, RUA, CIDADE, ESTADO, CEP, TIPO)
            VALUES (?, ?, ?, ?, ?, ?, ?, 'Almoço')
            '''
            cursor.execute(insert_local, (id_ponto, longitude, latitude, rua, cidade, estado, cep))

            conn.commit()        
    
    
    def saida(self, id_ponto):
        hora_saida = datetime.now().strftime('%H:%M:%S')
        
        latitude, longitude, rua, cidade, estado, cep = self.locali()

        with sqlite3.connect(self.server.db_path) as conn:
            cursor = conn.cursor()

            update_query = '''
            UPDATE REGISTRO_PONTO
            SET HORA_SAIDA = ?
            WHERE ID_PONTO = ?
            '''
            cursor.execute(update_query, (hora_saida, id_ponto))

            insert_local = '''
            INSERT INTO LOCALIZACAO (ID_PONTO, LONGITUDE, LATITUDE, RUA, CIDADE, ESTADO, CEP, TIPO)
            VALUES (?, ?, ?, ?, ?, ?, ?, 'Saída')
            '''
            cursor.execute(insert_local, (id_ponto, longitude, latitude, rua, cidade, estado, cep))

            conn.commit()
    


if __name__ == '__main__':
    ID_funcionario = 2

    # Cria uma instância da classe
    ponto = Ponto_register(ID_funcionario)

    # Chama os métodos da instância
    id_ponto = ponto.register()
    print(f'Ponto registrado com ID: {id_ponto}')

    # Depois (em horários diferentes):
    ponto.entrada(id_ponto)
    print('Entrada registrada.')

    ponto.almoco(id_ponto)
    print('Almoço registrado.')

    ponto.saida(id_ponto)
    print('Saída registrada.')