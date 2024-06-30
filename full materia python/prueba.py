# Definición de funciones
def cargar_tareas(archivo):
    """
    Función para cargar las tareas desde un archivo.
    """
    try:
        with open(archivo, 'r') as file:
            tareas = [line.strip() for line in file.readlines()]
        return tareas
    except FileNotFoundError:
        return []

def guardar_tareas(archivo, tareas):
    """
    Función para guardar las tareas en un archivo.
    """
    with open(archivo, 'w') as file:
        for tarea in tareas:
            file.write(f"{tarea}\n")

def mostrar_tareas(tareas):
    """
    Función para mostrar todas las tareas.
    """
    if not tareas:
        print("No hay artículos en la lista de compras.")
    else:
        print("\nLista de Compras:")
        for i, tarea in enumerate(tareas, start=1):
            print(f"{i}. {tarea}")

def añadir_tarea(tareas):
    """
    Función para añadir un nuevo artículo a la lista de compras.
    """
    tarea = input("Ingrese el nuevo artículo: ")
    tareas.append(tarea)
    print(f"Artículo '{tarea}' añadido a la lista.")

def marcar_tarea_completada(tareas):
    """
    Función para marcar un artículo como comprado.
    """
    mostrar_tareas(tareas)
    try:
        indice = int(input("Ingrese el número del artículo comprado: ")) - 1
        if 0 <= indice < len(tareas):
            tarea_completada = tareas.pop(indice)
            print(f"Artículo '{tarea_completada}' marcado como comprado.")
        else:
            print("Número de artículo inválido.")
    except ValueError:
        print("Por favor, ingrese un número válido.")

# Estructura principal del programa
def main():
    archivo_tareas = "compras.txt"
    tareas = cargar_tareas(archivo_tareas)
    
    while True:
        print("\nMenú de Opciones:")
        print("1. Mostrar lista de compras")
        print("2. Añadir nuevo artículo")
        print("3. Marcar artículo como comprado")
        print("4. Guardar y salir")
        
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                mostrar_tareas(tareas)
            elif opcion == 2:
                añadir_tarea(tareas)
            elif opcion == 3:
                marcar_tarea_completada(tareas)
            elif opcion == 4:
                guardar_tareas(archivo_tareas, tareas)
                print("Lista de compras guardada. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()
