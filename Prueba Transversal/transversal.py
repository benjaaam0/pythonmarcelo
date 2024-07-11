import random 
import statistics

# Lista de trabajadores
lista_empleados = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez",
                   "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]

# Función para generar sueldos aleatorios entre $300,000 y $2,500,000
def generar_sueldos_aleatorios():
    return [random.randint(300000, 2500000) for _ in range(10)]

# Función para clasificar y mostrar los sueldos de los trabajadores
def mostrar_lista_empleados(sueldos):
    empleados = [{"nombre": lista_empleados[i], "sueldo": sueldos[i]} for i in range(len(lista_empleados))]
    
    # Clasificar empleados por sueldo
    sueldos_bajos = []
    sueldos_medios = []
    sueldos_altos = []
    
    for empleado in empleados:
        if empleado["sueldo"] < 800000:
            sueldos_bajos.append(empleado)
        elif empleado["sueldo"] >= 800000 and empleado["sueldo"] <= 2000000:
            sueldos_medios.append(empleado)
        else:
            sueldos_altos.append(empleado)
    
    # Mostrar la lista clasificada
    print("Sueldos menores a $800.000")
    print(f"TOTAL: {len(sueldos_bajos)}")
    print("Nombre empleado Sueldo")
    for empleado in sueldos_bajos:
        print(f"{empleado['nombre']}: ${empleado['sueldo']}")
    
    print("\nSueldos entre $800.000 y $2.000.000")
    print(f"TOTAL: {len(sueldos_medios)}")
    print("Nombre empleado Sueldo")
    for empleado in sueldos_medios:
        print(f"{empleado['nombre']}: ${empleado['sueldo']}")
    
    print("\nSueldos superiores a $2.000.000")
    print(f"TOTAL: {len(sueldos_altos)}")
    print("Nombre empleado Sueldo")
    for empleado in sueldos_altos:
        print(f"{empleado['nombre']}: ${empleado['sueldo']}")
    
    # Calcular el total de sueldos
    total_sueldos = sum(empleado["sueldo"] for empleado in empleados)
    print(f"\nTOTAL SUELDOS: ${total_sueldos}")

# Función para calcular y mostrar estadísticas de sueldos
def ver_estadisticas(sueldos):
    sueldo_mas_alto = max(sueldos)
    sueldo_mas_chico = min(sueldos)
    promedio_sueldos = statistics.mean(sueldos)
    media_geometrica = statistics.geometric_mean(sueldos)

    print("------ Estadísticas de sueldos ------")
    print(f" - Sueldo más alto: ${sueldo_mas_alto}")
    print(f" - Sueldo más bajo: ${sueldo_mas_chico}")
    print(f" - Promedio de sueldos: ${promedio_sueldos:.2f}")
    print(f" - Media geométrica de sueldos: ${media_geometrica:.2f}")

# Función para generar reporte detallado de sueldos con descuentos
def generar_reporte_sueldos(sueldos):
    print("Reporte detallado de sueldos:")

    for i, trabajador in enumerate(lista_empleados):
        sueldo_base = sueldos[i]
        descuento_salud = sueldo_base * 0.07
        descuento_afp = sueldo_base * 0.12
        sueldo_liquido = sueldo_base - descuento_salud - descuento_afp

        print(f"{trabajador}:")
        print(f" - Sueldo base: ${sueldo_base}")
        print(f" - Descuento salud (7%): ${descuento_salud:.2f}")
        print(f" - Descuento AFP (12%): ${descuento_afp:.2f}")
        print(f" - Sueldo líquido: ${sueldo_liquido:.2f}")

# Función principal que maneja el menú y las opciones del programa
def main():
    sueldos = []  # Lista vacía para almacenar los sueldos
    
    while True:
        print("\n--- Menú de la aplicación ---")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            sueldos = generar_sueldos_aleatorios()
            print("Sueldos aleatorios generados.")
        
        elif opcion == '2':
            if not sueldos:
                print("Debe generar los sueldos primero (opción 1).")
            else:
                mostrar_lista_empleados(sueldos)
        
        elif opcion == '3':
            if not sueldos:
                print("Debe generar los sueldos primero (opción 1).")
            else:
                ver_estadisticas(sueldos)
        
        elif opcion == '4':
            if not sueldos:
                print("Debe generar los sueldos primero (opción 1).")
            else:
                generar_reporte_sueldos(sueldos)
        
        elif opcion == '5':
            print("Finalizando programa...\n Desarrollado por Benjamin Martinez \n RUT: 22.106.039-3")
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")

# Iniciar la ejecución del programa
if __name__ == "__main__":
    main()