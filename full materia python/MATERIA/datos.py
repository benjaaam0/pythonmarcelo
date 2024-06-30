# Pedir entrada del usuario
nombre = input("Ingrese nombre y apellido: ")
rut = input("Ingrese su rut: ")  # Mantener como cadena para incluir posibles guiones o puntos
correo = input("Ingrese su correo: ")
telef = input("Ingrese su teléfono: ")  # Mantener como cadena para evitar pérdida de formato

# Convertir a mayúsculas solo el nombre y el correo (si es necesario)
nombre_upper = nombre.upper()
correo_upper = correo.upper()

# Mostrar la información formateada
print(f"NOMBRE:\t\t{nombre_upper}")
print(f"RUT:\t\t{rut}")
print(f"CORREO:\t\t{correo_upper}")
print(f"TELÉFONO:\t{telef}")
