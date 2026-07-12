class GestorTareas:
    
    def __init__(self,lista_tareas = None):
        if lista_tareas is None:
            self.lista_tareas = []
        else:
            self.lista_tareas = lista_tareas
    
    def agregar_tarea(self,nueva_tarea):
        self.lista_tareas.append(nueva_tarea)

    def buscar_por_id(self,id_buscado):
        for tarea in self.lista_tareas:
            if id_buscado == tarea.id:
                return tarea
        return None

    def eliminar_tarea(self,id_tarea):
        tarea_a_eliminar = self.buscar_por_id(id_tarea)
        if tarea_a_eliminar is None:
            return False
        self.lista_tareas.remove(tarea_a_eliminar)
        return True
    
    def obtener_siguiente_id(self):
        if not self.lista_tareas:
            return 1
        else:
            id_maximo = max(tarea.id for tarea in self.lista_tareas)
            return id_maximo + 1
