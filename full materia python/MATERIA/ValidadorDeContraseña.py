def validar_contraseña(contraseña):
    """
    Valida si la contraseña cumple con los requisitos:
    - Al menos 8 caracteres
    - Al menos una letra mayúscula
    - Al menos una letra minúscula
    - Al menos un número
    """
    if len(contraseña) < 8:
        return False
    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False
    for caracter in contraseña:
        if caracter.isupper():
            tiene_mayuscula = True
        elif caracter.islower():
            tiene_minuscula = True
        elif caracter.isdigit():
            tiene_numero = True
    return tiene_mayuscula and tiene_minuscula and tiene_numero

# Solicitar al usuario una contraseña
contraseña = input("Ingrese una contraseña: ")

# Validar la contraseña
if validar_contraseña(contraseña):
    print("La contraseña cumple con los requisitos.")
else:
    print("La contraseña no cumple con los requisitos.")
