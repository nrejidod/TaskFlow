def mostrar_tarea(tarea):
    print(f"""
Tarea ID: {tarea.id}
Nombre: {tarea.titulo}
Descripción: {tarea.descripcion}
Prioridad: {tarea.prioridad}
Estado: {tarea.estado}
""")
    
def mostrar_tareas(lista_tareas):
    if not lista_tareas:
        print("No hay tareas.")
        return
    for tarea in lista_tareas:
        mostrar_tarea(tarea)
