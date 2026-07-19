import persistencia
from gestor.gestortareas import GestorTareas
from ui.menu import iniciar_menu


def main():
    lista_tareas = persistencia.cargar_datos()
    gestor = GestorTareas(lista_tareas) 
    iniciar_menu(gestor)
    
if __name__ == "__main__":
    main()
