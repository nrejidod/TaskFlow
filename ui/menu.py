from services import tareas_services 
from ui.mostrar import mostrar_tarea,mostrar_tareas
def obtener_opcion_menu():
    while True:
        try:
            opcion = int(input(
                """
Menú de TaskFlow
1. Crear tarea
2. Mostrar tareas
3. Salir
Seleccione una opción: """
            ))   
            if 1<= opcion <=3:
                return opcion
            
            print("Ingrese una opción válida.")   

        except ValueError:
            print("Debe ingresar un número.")

def iniciar_menu(gestor):
    while True:
        opcion = obtener_opcion_menu()

        if opcion == 1:
            tarea = tareas_services.crear_tarea(gestor)

            if tarea is not None:
                mostrar_tarea(tarea)
                print("Tarea creada. ¿Desea editarla?")
            else:
                print("Error al crear la Tarea, intente nuevamente.")
        elif opcion == 2:
            mostrar_tareas(gestor.lista_tareas)
        elif opcion == 3:
            print("Cerrando programa")
            return 
        
        