import sqlite3
from datetime import datetime
import geocoder


class Server():
    def __init__(self, db_path='ponto.db'):
        self.db_path = db_path

class Ponto_register():
    def __init__(self, ID_funcionario):
        self.ID_funcionario = ID_funcionario
        self.server = Server()


    def locali(self):
        g = geocoder.ip('me')
        if g.ok:
            latitude = g.latlng[0] if g.latlng else None
            longitude = g.latlng[1] if g.latlng else None
            rua = g.street or "Desconhecido"
            cidade = g.city or "Desconhecido"
            estado = g.state or "Desconhecido"
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

class Ponto_register_aplicado():
    def __init__(self, ID_funcionario):
        self.ID_funcionario = ID_funcionario
        self.server = Server()
    
class Ponto_register_modificado():
    def __init__(self, ID_funcionario):
        self.ID_funcionario = ID_funcionario
        self.server = Server()