
from peliculas import listar_peliculas, agregar_pelicula, eliminar_pelicula, buscar_pelicula
import os


while True:
    print("\n--------------------------------\nLista de Peliculas")
    print("\n1. Listar todas las peliculas")
    print("\n2. Agregar una Pelicula")
    print("\n3. Eliminar Pelicula")
    print("\n4. Buscar por ID")
    print("\n5. Salir\n")



    opcion = input("seleccione una opcion:")


    if opcion == '1':
        listar_peliculas()

    if opcion == '2':
        agregar_pelicula()

    if opcion == '3':
        eliminar_pelicula()

    if opcion == '4':
        buscar_pelicula()
        
    elif opcion == '5':    
        print("Fin")
        break

    os.system('clear')

