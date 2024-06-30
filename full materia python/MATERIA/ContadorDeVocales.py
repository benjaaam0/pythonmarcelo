def contar_vocales(cadena):
    """
    Cuenta la cantidad de vocales (mayúsculas y minúsculas) en una cadena.
    """
    vocales = "aeiouAEIOU"
    contador = 0
    for caracter in cadena:
        if caracter in vocales:
            contador += 1
    return contador

# Solicitar al usuario una cadena de texto
cadena = input("Ingrese una cadena de texto: ")

# Contar las vocales en la cadena ingresada
cantidad_vocales = contar_vocales(cadena)

# Mostrar el resultado
print(f"La cantidad de vocales en la cadena es: {cantidad_vocales}")

