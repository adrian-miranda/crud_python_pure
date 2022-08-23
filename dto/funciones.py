def listar_usuarios(usuarios):
    print('Crusos: ')
    contador = 1
    for usuario in usuarios:
        datos = "\ncontador {0}\nid: {1}\nNombre: {2}\nApellido: {3}\nEmail: {4}\nEdad: {5}\n"
        print(datos.format(contador , usuario[0], usuario[1],usuario[2],usuario[3],usuario[4]))
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

def id_borrado(usuarios):
    listar_usuarios(usuarios)
    codigo = False
    usuario_eliminar = int(input('ingrese el codigo de usuario a eliminar: '))
    for usuario in usuarios:
        print(f'estos son : {usuario}')
        if usuario[0] == usuario_eliminar:
            codigo = True
            break
    if not codigo:
        usuario_eliminar = ''
    return usuario_eliminar