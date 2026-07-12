class Tarea:
    def __init__(self,id_tarea, titulo, descripcion, prioridad, estado):
        self.id = id_tarea
        self.titulo = titulo
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.estado = estado

    def marcar_completada(self):
        self.estado = "Realizada"
    def cambiar_prioridad(self, nueva_prioridad):
        self.prioridad = nueva_prioridad
    def cambiar_descripcion(self, nueva_descripcion):
        self.descripcion = nueva_descripcion

    def __str__(self):
        return f"----------------------\nID: {self.id}\nTitulo de la tarea: {self.titulo}\nDescripción: {self.descripcion}\nPrioridad: {self.prioridad}\nEstado: {self.estado}\n----------------------"


    def a_diccionario(self):
        return {
            "id":self.id,
            "titulo":self.titulo,
            "descripcion":self.descripcion,
            "prioridad":self.prioridad,
            "estado":self.estado
        }
    
    @classmethod
    def desde_diccionario(cls,datos):
        return cls(
            datos["id"],
            datos["titulo"],
            datos["descripcion"],
            datos["prioridad"],
            datos["estado"]
        )