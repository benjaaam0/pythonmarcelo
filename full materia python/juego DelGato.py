#juego del gato

# Definir el tablero como una lista de 9 elementos
tablero = [' ' for _ in range(9)]

# Función para imprimir el tablero
def imprimir_tablero(tablero):
    print("\t" + tablero[0] + "\t|\t" + tablero[1] + "\t|\t" + tablero[2])
    print("\t" + '-' * 7 + '|' + '-' * 7 + '|' + '-' * 7)
    print("\t" + tablero[3] + "\t|\t" + tablero[4] + "\t|\t" + tablero[5])
    print("\t" + '-' * 7 + '|' + '-' * 7 + '|' + '-' * 7)
    print("\t" + tablero[6] + "\t|\t" + tablero[7] + "\t|\t" + tablero[8])

# Función para verificar si hay un ganador
def verificar_ganador(tablero, jugador):
    # Definir todas las posibles combinaciones ganadoras
    combinaciones_ganadoras = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), # Filas
        (0, 3, 6), (1, 4, 7), (2, 5, 8), # Columnas
        (0, 4, 8), (2, 4, 6)              # Diagonales
    ]
    # Comprobar si alguna combinación ganadora está llena por el mismo jugador
    for combinacion in combinaciones_ganadoras:
        if tablero[combinacion[0]] == tablero[combinacion[1]] == tablero[combinacion[2]] == jugador:
            return True
    return False

# Función para verificar si el tablero está lleno
def tablero_lleno(tablero):
    return ' ' not in tablero

# Función para jugar el juego del gato
def jugar():
    turno = 'X'
    while True:
        imprimir_tablero(tablero)
        print(f"Turno del jugador {turno}. Elige una posición (1-9): ")
        
        try:
            # Convertir la entrada del jugador a índice de la lista
            posicion = int(input()) - 1
            if tablero[posicion] != ' ':
                print("Esta posición ya está ocupada. Elige otra.")
                continue
            tablero[posicion] = turno
        except (ValueError, IndexError):
            print("Entrada inválida. Elige un número del 1 al 9 que corresponda a una posición vacía.")
            continue

        # Verificar si hay un ganador
        if verificar_ganador(tablero, turno):
            imprimir_tablero(tablero)
            print(f"¡El jugador {turno} ha ganado!")
            break
        
        # Verificar si el tablero está lleno (empate)
        if tablero_lleno(tablero):
            imprimir_tablero(tablero)
            print("¡Empate! El tablero está lleno.")
            break

        # Cambiar el turno al otro jugador
        turno = 'O' if turno == 'X' else 'X'

# Ejecutar el juego
jugar()
