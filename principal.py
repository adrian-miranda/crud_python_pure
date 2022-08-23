from mysql.connector import Error
from bbdd.conexion import DAO
import dto.funciones

#este es el archivo encargado de lanzar la aplicacion por consola
def menu_principal():
    continuar = True
    #Esta variable hace que el menu se repita mietras el usuario no la pase a false
    while(continuar):
        opcion_correcta = False
        #Al inicio del ciclo no hay una opcion correcta, porque no se ha seleccionado ninguna
        while not(opcion_correcta):
            opcion = int(input('\nQue le gustaria hacer:\n\n1._Buscar: \n2._Agregar: \n3._Modificar: \n4._Borrar: \n5._Salir: '))
            if (opcion < 1 or opcion > 5):
                print('Opcion Icorrecta')
            elif (opcion == 5):
                continuar = False 
                #de esta manera cortamos el ciclo
                print('Hasta pronto')
                break
                #de esta manera salimos del ciclo
            else:
                opcion_correcta = True
                # de esta manera lo que se hace es que se sale del segundo while, de lo contrari seguiria mostrando el menu y pasa al siguiente paso que es ejecutar_opcion(opcion)
                ejecutar_opcion(opcion)

def ejecutar_opcion(opcion):
    dao = DAO()

    if opcion == 1:
        try:
            listar_usuarios = dao.listar_usuarios()
            if len(listar_usuarios) > 0:
                dto.funciones.listar_usuarios(listar_usuarios)
            else:
                print('no se han encontrado cursos')
        except Error as ex:
            print('Error  {0}'.format(ex))

    elif opcion == 2:
        usuario = dto.funciones.registro_usuario()
        try:
            dao.agregar_usuario(usuario)
        except Error as ex:
            print('Error  {0}'.format(ex))
    elif opcion == 3:
        try:
            listar_usuarios = dao.listar_usuarios()
            if (len(listar_usuarios) > 0):
                usuario = dto.funciones.id_actualizado(listar_usuarios)
                if usuario:
                    dao.actualizar_usuario(usuario)
                else:
                    print('Id usuario no encontrado')
            else:
                print('Usuario no encontrado')
        except Error as ex:
            print('Error  {0}'.format(ex))
    elif opcion == 4:
        try:
            listar_usuarios = dao.listar_usuarios()
            if(len(listar_usuarios) > 0):
                codigo_eliminar = dto.funciones.id_borrado(listar_usuarios)
                if not(codigo_eliminar == ''):
                    dao.borrar_usuario(codigo_eliminar)
                else:
                    print('Usuario no encontrado')
        except Error as ex:
            print('Error  {0}'.format(ex))
    else:
        print('opcion no valida')
    # return print(opcion)

menu_principal()