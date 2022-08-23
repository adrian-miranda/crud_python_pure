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

def id_actualizado(usuarios):
    listar_usuarios(usuarios)
    codigo = False
    usuario_actualizado = int(input('ingrese el codigo de usuario a actualizar: '))
    for usuario in usuarios:
        if usuario[0] == usuario_actualizado:
            codigo = True
            break
    if (codigo):
        nombre_editado = input('Ingrese nombre a modificar: ')
        apellido_editado = input('Ingrese apellido a modificar: ')
        email_editado = input('Ingrese email a modificar: ')
        anio_editado = input('Ingrese año a modificar: ')
        mes_editado = input('Ingrese mes a modificar: ')
        dia_editado = input('Ingrese dia a modificar: ')
        edad_editado = (f'{anio_editado}-{mes_editado}-{dia_editado}')
        usuario_editado = (nombre_editado , apellido_editado ,email_editado,  edad_editado)
    else:
        usuario_editado = None
    return usuario_editado

def id_borrado(usuarios):
    listar_usuarios(usuarios)
    codigo = False
    usuario_eliminar = int(input('ingrese el codigo de usuario a eliminar: '))
    for usuario in usuarios:
        if usuario[0] == usuario_eliminar:
            codigo = True
            break
    if not codigo:
        usuario_eliminar = ''
    return usuario_eliminar


