import requests
import os
URL = "http://127.0.0.1:8000/peliculas/"




##declaracion de funciones##
##LISTAR TODAS##
def listar_peliculas():
    respuesta = requests.get(URL)
    if respuesta.status_code == 200:
        peliculas = respuesta.json()
        os.system('clear')
        print("\t\t---LISTA DE PELICULAS---")
        for pelicula in peliculas:
            print(f"\n{pelicula['titulo']}:\n  {pelicula['estado']}")

        input("\nPresione enter para continuar")
            
    else:
        print("Error al obtener peliculas")

##BUSCAR POR ID
def buscar_pelicula():
    os.system('clear')
    id_peli = input("Ingrese el id a buscar: ")
    respuesta = requests.get(f"{URL}{id_peli}")
    if respuesta.status_code == 200:
        pelicula = respuesta.json()
        print(f"Titulo: {pelicula['titulo']}\n  Estado: {pelicula['estado']}")
        input("\nPresione enter para continuar")

    else: 
        print("No existe esa pelicula!")


##AGREGAR PELICULA#
def agregar_pelicula():
    os.system('clear')
    titulo = input("\nIngrese el nombre de la pelicula: ")
    estado = input("ingrese el estado actual: ")

    data = {
        "titulo": titulo,
        "estado": estado
    }

    respuesta = requests.post(URL, json=data)
    if respuesta.status_code == 200:
        print("Pelicula creada con éxito!")
        input("\nPresione enter para continuar")
    else:
        print("Hubo un error...")


##ELIMINAR

def eliminar_pelicula():
    os.system('clear')
    try:
        id_peli = input("\nIngrese el ID de la pelicula que desea eliminar: ")

        respuesta = requests.delete(f"{URL}{id_peli}")

        if respuesta.status_code == 200:
            print(f"La pelicula se eliminó con éxito...")
            input("\nPresione enter para continuar")

        elif respuesta.status_code == 404:
            print(f"La pelicula no se encontró!")

        else:
            print ("Hubo un error!")

    except ValueError:
        print("Ingrese un ID valido!")


    

    
