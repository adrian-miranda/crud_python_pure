def listar_usuarios(cursos):
    print('Crusos: ')
    contador = 1
    for curso in cursos:
        datos = "\ncontador {0}\nid: {1}\nNombre: {2}\nApellido: {3}\nEmail: {4}\nEdad: {5}\n"
        print(datos.format(contador , curso[0], curso[1],curso[2],curso[3],curso[4]))
        contador = contador + 1

def registro_usuario():
    nombre = input('Ingrese nombre: ')
    apellido = input('Ingrese apellido: ')
    email = input('Ingrese email: ')
    anio = input('Ingrese año: ')
    mes = input('Ingrese mes: ')
    dia = input('Ingrese dia: ')
    edad = (f'{anio}-{mes}-{dia}')

    usuario = (nombre , apellido ,email,  edad)
    return usuario