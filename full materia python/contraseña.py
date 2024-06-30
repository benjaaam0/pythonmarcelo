#contraseña

# Función para validar entradas
def validar_entrada(entrada, tipo, longitud):
    if tipo == "letras" and not entrada.isalpha():
        print(f"Error: {entrada} debe contener solo letras.")
        return False
    if tipo == "numeros" and not entrada.isdigit():
        print(f"Error: {entrada} debe contener solo números.")
        return False
    if len(entrada) != longitud:
        print(f"Error: {entrada} debe tener {longitud} caracteres.")
        return False
    return True

# Solicitar la entrada del usuario
nombre = input("Las 3 primeras letras de su primer nombre: ")
apellido = input("Las 2 primeras letras de su segundo apellido: ")
rut = input("Los 2 primeros números de su RUT: ")
mes = input("Las 3 letras iniciales del mes de su nacimiento: ")
ciudad = input("Las 2 últimas letras de la ciudad donde vive: ")

# Validar las entradas
validacion_nombre = validar_entrada(nombre, "letras", 3)
validacion_apellido = validar_entrada(apellido, "letras", 2)
validacion_rut = validar_entrada(rut, "numeros", 2)
validacion_mes = validar_entrada(mes, "letras", 3)
validacion_ciudad = validar_entrada(ciudad, "letras", 2)

# Solo proceder si todas las entradas son válidas
if validacion_nombre and validacion_apellido and validacion_rut and validacion_mes and validacion_ciudad:
    # Generar opciones de contraseña combinando las entradas de distintas maneras
    opcion1 = nombre + apellido + rut + mes + ciudad
    opcion2 = nombre + rut + apellido + mes + ciudad + mes
    opcion3 = rut + nombre + mes + ciudad + apellido
    opcion4 = apellido + rut + nombre + mes + ciudad + rut
    opcion5 = ciudad + apellido + nombre + rut + mes + ciudad

    # Imprimir las opciones de contraseña
    print("")
    print(f"La opción 1 de contraseña es: {opcion1}")
    print(f"La opción 2 de contraseña es: {opcion2}")
    print(f"La opción 3 de contraseña es: {opcion3}")
    print(f"La opción 4 de contraseña es: {opcion4}")
    print(f"La opción 5 de contraseña es: {opcion5}")
else:
    print("\nPor favor, corrige las entradas incorrectas e intenta de nuevo.")
