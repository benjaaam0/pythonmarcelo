#Se leen dos numeros
num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))

#Elige el numero mas grande
if num1 > num2:
    larger_num = num1
else:
    larger_num = num2

#Imprime el resultado 
print("El numero mas grande es: ",larger_num)
