def listar_usuarios(cursos):
    print('Crusos: ')
    contador = 1
    for curso in cursos:
        datos = "\ncontador {0}\nid: {1}\nNombre: {2}\nApellido: {3}\nEmail: {4}\nEdad: {5}\n"
        print(datos.format(contador , curso[0], curso[1],curso[2],curso[3],curso[4]))
        contador = contador + 1