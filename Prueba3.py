import os

# Función para limpiar la consola según el sistema operativo
def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

# Clase para manejar las reservas
class Reserva:
    def __init__(self, nombre, apellido, ciudad_origen, tour, cantidad_personas):
        self.nombre = nombre
        self.apellido = apellido
        self.ciudad_origen = ciudad_origen
        self.tour = tour
        self.cantidad_personas = cantidad_personas

# Variable global para almacenar las reservas
reservas = []

# Función para registrar una reserva
def registrar_reserva():
    limpiar_consola()
    print("------REGISTRO DE RESERVA------\n")
    nombre = input("Ingrese nombre del cliente: ")
    apellido = input("Ingrese apellido del cliente: ")
    ciudad_origen = input("Ingrese ciudad de origen del cliente: ")

    while True:
        print("\n------TOURS DISPONIBLES------")
        print("1. Isla de Pascua")
        print("2. Carretera Austral")
        print("3. Calbuco")
        print("4. Desierto de Atacama")
        print("5. No está el destino que desea")

        tour_opcion = input("\nSeleccione el número del tour: ")

        if tour_opcion == '1':
            tour = "Isla de Pascua"
            break
        elif tour_opcion == '2':
            tour = "Carretera Austral"
            break
        elif tour_opcion == '3':
            tour = "Calbuco"
            break
        elif tour_opcion == '4':
            tour = "Desierto de Atacama"
            break
        elif tour_opcion == '5':
            print("No está el destino que desea")
            print("¡Hasta luego!")
            return  # Salir de la función sin añadir reserva
        else:
            print("Opción inválida. Seleccione el número del tour.")

    cantidad_personas = input("Ingrese cantidad de personas para el tour: ")
    while not cantidad_personas.isdigit():
        cantidad_personas = input("Ingrese un valor numérico para la cantidad de personas: ")

    reserva = Reserva(nombre, apellido, ciudad_origen, tour, int(cantidad_personas))
    reservas.append(reserva)
    print("\nReserva registrada correctamente.\n")

# Función para listar todas las reservas
def listar_reservas():
    limpiar_consola()
    print("Listado de Reservas\n")
    if reservas:
        for i, reserva in enumerate(reservas, 1):
            print(f"{i}. Cliente: {reserva.nombre} {reserva.apellido}, Origen: {reserva.ciudad_origen}, Tour: {reserva.tour}, Cantidad: {reserva.cantidad_personas}")
    else:
        print("No hay reservas registradas.")

# Función para imprimir detalle de reservas por destino en un archivo de texto
def imprimir_detalle_por_destino():
    limpiar_consola()
    print("Imprimir Detalle de Reservas por Destino\n")
    if reservas:
        # Mostramos los destinos disponibles
        destinos = ["Isla de Pascua", "Carretera Austral", "Calbuco", "Desierto de Atacama", "No está el destino que desea"]
        print("Destinos disponibles:")
        for i, destino in enumerate(destinos, 1):
            print(f"{i}. {destino}")

        destino_opcion = input("\nSeleccione el número del destino para imprimir el detalle de reservas: ")
        while destino_opcion not in ['1', '2', '3', '4', '5']:
            destino_opcion = input("Opción inválida. Seleccione el número del destino: ")

        destino_seleccionado = destinos[int(destino_opcion) - 1]

        # Generamos el archivo de texto con el detalle de reservas para el destino seleccionado
        nombre_archivo = f"detalle_reservas_{destino_seleccionado.replace(' ', '_').lower()}.txt"
        with open(nombre_archivo, 'w') as archivo:
            archivo.write(f"Detalle de Reservas para {destino_seleccionado}\n\n")
            for reserva in reservas:
                if reserva.tour == destino_seleccionado:
                    archivo.write(f"Cliente: {reserva.nombre} {reserva.apellido}, Origen: {reserva.ciudad_origen}, Cantidad: {reserva.cantidad_personas}\n")
        print(f"\nSe ha generado el archivo '{nombre_archivo}' con el detalle de las reservas para {destino_seleccionado}.\n")
    else:
        print("No hay reservas registradas.")

# Función principal para ejecutar el programa
def main():
    while True:
        print("Bienvenido a SurExplora - Sistema de Reservas\n")
        print("1. Registrar Reserva")
        print("2. Listar Todas las Reservas")
        print("3. Imprimir Detalle de Reservas por Destino")
        print("4. Salir del Programa")

        opcion = input("\nSeleccione una opción: ")
        limpiar_consola()

        if opcion == '1':
            registrar_reserva()
        elif opcion == '2':
            listar_reservas()
        elif opcion == '3':
            imprimir_detalle_por_destino()
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor seleccione una opción válida.\n")

if __name__ == "__main__":
    main()