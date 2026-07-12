import persistencia
from gestor.gestortareas import GestorTareas


def menu(Gestor):
    gestor = Gestor

def main():
    lista_tareas = persistencia.cargar_datos()
    gestor = GestorTareas(lista_tareas) 
    menu(gestor)
    
if __name__ == "__main__":
    main()
