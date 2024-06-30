def calcular_imc(peso, altura):
    """
    Calcula el índice de masa corporal (IMC) dado el peso en kg y la altura en metros.
    """
    imc = peso / (altura ** 2)
    return imc

# Solicitar al usuario el peso y la altura
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

# Calcular el IMC
imc = calcular_imc(peso, altura)

# Mostrar el resultado del IMC con dos decimales
print(f"Su índice de masa corporal (IMC) es: {imc:.2f}")
