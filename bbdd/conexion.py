#Encargado de conectar a la bbdd
import mysql.connector
from mysql.connector import Error

class DAO():
    def __init__(self):
        try:
            self.la_conexion = mysql.connector.connect(
                host = 'localhost',
                port = 3306,
                user = 'root',
                password = 'root',
                db = 'ensayo_rubrica'
            )
            if (self.la_conexion.is_connected()):
                # print('conexion existosa')
                info_server = self.la_conexion.get_server_info()
                # print(info_server)
                cursor = self.la_conexion.cursor()
                cursor.execute('SELECT DATABASE()')
                row = cursor.fetchone()
                # print(row)
        except Error as ex:
            print('Error al intentar la conexion {0}'.format(ex))
    
    def listar_usuarios(self):
        if(self.la_conexion.is_connected()):
            try:
                cursor = self.la_conexion.cursor()
                cursor.execute("SELECT * FROM login_usuario ORDER BY id ASC")
                resultado_listado = cursor.fetchall()
                return resultado_listado
            except Error as ex:
                print('Error al intentar la conexion {0}'.format(ex))
            finally:
                if self.la_conexion.is_connected():
                    self.la_conexion.close()
                    print('conexion finalizada')


