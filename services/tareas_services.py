from models.tarea import Tarea

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

def obtener_titulo():
    pass
def obtener_descripcion():
    pass

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

