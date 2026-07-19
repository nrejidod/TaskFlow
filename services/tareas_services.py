from models.tarea import Tarea
from persistencia import guardar_datos
PRIORIDADES = {
    1:"Baja importancia",
    2:"Media importancia",
    3:"Alta importancia"
}
MENSAJE_PRIORIDADES = {
    "print":"Ingrese prioridad de la tarea.\n1) Baja importancia\n2) Media importancia\n3) Alta importancia ",
    "input":"Ingrese prioridad de la tarea(1,2,3): "
}
ESTADOS = {
    1:"Pendiente",
    2:"En progreso",
    3:"Realizada",
}
MENSAJE_ESTADOS = {
    "print":"Ingrese estado de la tarea.\n1) Pendiente.\n2) En progreso.\n3) Realizada.",
    "input":"Ingrese estado de la tarea(1,2,3): "
}
ERRORES = "Error! Ingrese un valor entre 1,2,3."

def crear_tarea(gestor):

    titulo = obtener_titulo()
    descripcion = obtener_descripcion()
    prioridad = obtener_prioridad_o_estado(PRIORIDADES,MENSAJE_PRIORIDADES,ERRORES)
    estado = obtener_prioridad_o_estado(ESTADOS,MENSAJE_ESTADOS,ERRORES)
    id_tarea = gestor.obtener_siguiente_id()

    tarea = Tarea(id_tarea,titulo,descripcion,prioridad,estado)
    gestor.agregar_tarea(tarea)
    try:
        guardar_datos(gestor.lista_tareas)
    except OSError:
        eliminado = gestor.eliminar_tarea(id_tarea)
        if not eliminado:
            raise RuntimeError(
                f"No se pudo deshacer la creacion de la tarea {id_tarea}"
            )
        return None
    return tarea


def obtener_titulo():
    while True:
        titulo = input("Ingrese el titulo de la tarea: ")
        titulo = titulo.strip()
        if titulo == "":
            print("Error! No has escrito el titulo de la tarea.")
        else:    
            return titulo

def obtener_descripcion():
    descripcion = input("Ingrese descripción de la tarea: ")
    descripcion = descripcion.strip()
    return descripcion

def obtener_prioridad_o_estado(diccionario,mensaje,error):
    while True:
        print(mensaje["print"])
        try:
            prioridad_o_estado = int(input(mensaje["input"]))
            if prioridad_o_estado in diccionario:
                return diccionario[prioridad_o_estado]
            else:
                print(error)
        except ValueError:
            print(error)

