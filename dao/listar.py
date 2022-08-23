from mysql.connector import Error
def listar_usuarios(self):
        if(self.la_conexion.is_connected()):
            try:
                cursor = self.la_conexion.cursor()
                cursor.execute("SELECT * FROM login_usuario ORDER BY id ASC")
                resultado_listado = cursor.fetchall()
                return resultado_listado
            except Error as ex:
                print('Error al intentar la conexion {0}'.format(ex))