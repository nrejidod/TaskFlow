import json
from models.tarea import Tarea
def cargar_datos():
    lista_tareas = []
    try:
        with open("datos.json","r") as archivo:
            datos = json.load(archivo)
            for dato in datos:
                nueva_tarea = Tarea.desde_diccionario(dato)
                lista_tareas.append(nueva_tarea)
            return lista_tareas
    except FileNotFoundError:
        return lista_tareas
        

def guardar_datos(lista_tareas):
    datos = []
    for tarea in lista_tareas:
        nuevo_diccionario = tarea.a_diccionario()
        datos.append(nuevo_diccionario)
    with open("datos.json","w") as archivo:
        json.dump(datos,archivo, indent=4)

