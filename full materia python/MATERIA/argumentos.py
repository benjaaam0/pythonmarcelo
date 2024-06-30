#funcion Recibe una cantidad variable de argumentos 
#*args
def suma_multiple(*args):
  """
  Recibe una cantidad x de argumentos *args y devuelve una suma total
  """
  suma_total = 0

  for numero in args:

    suma_total += numero

  return suma_total
#llamar a la funcion
resultado_multiple = suma_multiple(1,2,3,4,5,6,7,8,9,10)
print(f"La suma total de: 1,2,3,4,5,6,7,8,9,10 es {resultado_multiple}")
 #2- recibir una cantidad variable de argumentos (nombres) **kwargs Diccionarios.
def saludo_completo(**kwargs):
  """
  Recibe un diccionario e imprime una cadena completa con cada valor.
  """
  saludo = "hola"
  #declaro un for
  for clave,valor in kwargs.items():#desempaqueta el diccionario en clave:VAlor
    saludo+= f" {valor}"
  saludo += "\nBienvenido a las clas de funciones "

  print(saludo)
#LLamamos a la F 
saludo_completo(Nombre="Benja",apellido="Martinez")
#funcion combinada que usa *args y *kwargs
def informacion_completa(*args, **kwargs):
  """
  Recibe argumentos desde listas y diccionario y los imprime 
  """
  print("informacion recibida")

  for argumentos in args:

    print(f"Argumento: {argumentos}")

  for clave, valor in kwargs.items():

    print(f"{clave} : {valor}")

  print(type(kwargs))
#llamar a la funcion
informacion_completa(1,2,3,4,5, Nombre="Benja", Comuna="Calbuco")
#funcion compleja que devuelve varios valores
def estadisticas(*args):
  """
  Recibe varios argumentos y devuelve varios varios estadisticas:
  Suma,promedio,minimo y un maximo
  """
  suma_total = sum(args)
  promedio = suma_total / len(args)
  maximo = max(args)
  minimo = min(args)
  return suma_total,promedio,maximo,minimo

suma_total,promedio,maximo,minimo = estadisticas(10,20,30,40,50)
print(f"Suma: {suma_total}\n Promedio: {promedio}\n Maximo: {maximo}\n Minimo: {minimo}")
#Funcion lista y diccionario 
def procesar_datos(lista,diccionario):

  """
  Recibe lista y diccionario y los procesa de distinta manera
  """
  print("Procesando una lista")

  for elemento in lista :

    print(f"elemento: {elemento}")

  print("Procesando un diccionario")

  for clave,valor in diccionario.items():

    print(f"{clave}: {valor}")
#crear lista y diccionario e invocar a mi funcion
lista_ejemplo = [1,2,3,4,5]
diccionario_ejemplo = {
  
  "saludo": "hola",
  "despedida": "Adios",
  "numero": 777
}
#funcion recursiva
def factorial(numero):
  
  """
  Calcula el factorial de un numero de manera recursiva
  """
  if numero == 0:

    return 1
  else:
    return numero * factorial(numero-1) #invocamos de manera recursiva a la misma funcion

#llamar a la funcion factorial con el argumento 5
resultado_factorial = factorial(5)
print(f"El factorial de 5 es {resultado_factorial}")

#Funcion anidad: Una funcion dentro de otra.
#Organizar el codigo 
def operacion_anidada(a,b):

  def suma(numero1,numero2):

    return numero1 + numero2

  def multiplicacion(numero1,numero2):

    return numero1*numero2
  resultado_suma = suma(a,b)
  resultado_multiplicacion=multiplicacion(a,b)
  return resultado_suma, resultado_multiplicacion

#LLamar a mi funcion:
resultado_suma, resultado_multiplicacion = operacion_anidada(4,5)
print(f"la suma de 4 y 5 es {resultado_suma}\n la multiplicacion de 4 y 5 es {resultado_multiplicacion}")

#Funcion de tipo lambda - Eleva numeros al cuadrado 
elevar_cuadrado = lambda x: x**2

#Lista de numeros
numeros = [1,2,3,4,5]

#USar la funcion map() va a aplicar mi funcion lambda a cada numero de mi lista 
#list() convierte cada numero o resultado a una lista
numeros_cuadrados = list(map(elevar_cuadrado,numeros))
print(f"Los numeros: {numeros} : elevados al cuadrado son: {numeros_cuadrados}")