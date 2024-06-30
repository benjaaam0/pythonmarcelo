print("Bienvenidos al mundo de la programacion")
print("ingresa tu nombre: ")
Nom = input()
print("Bienvenido" , Nom)

print("Ingrese el numero equivalente a x en la siguiente ecuacion : x2 + 3x + 1 / 4")
num = input(int())
resultadoeq = ((num**2) + 3 * num + 1 ) / 4
print("El resultado de la ecuacion es" , resultadoeq)

nombre = input("Ingrese nombre y apellido")
rut = int(input("Ingrese su rut: "))
correo = input("Ingrese su correo: ")
telef = int(input("Ingrese su telefono: "))

nombre_upper = nombre.upper()
correo_upper = correo.upper()
print("NOMBRE\t\t", nombre_upper)
print("RUT:\t\t")