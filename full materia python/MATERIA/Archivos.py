#Importar las librerias para trabajar con archivos.

import csv #Excel
import json #Json

#Funcion para crear archivos 
def crear_archivo_txt(nombre_archivo,contenido):

  """Crea un archivo de texto y escribe contenido en el."""

  with open(nombre_archivo, 'w') as archivo:

    archivo.write(contenido)

  print(f"archivo: {nombre_archivo} creado exitosamente")

#Funcion para crear archivos JSON

def crear_archivo_json(nombre_archivo,datos):

  """Crea un archivo de texto y escribe contenido en el."""

  with open(nombre_archivo, 'w') as archivo:

    #Conversion de diccionario en json y lo escribe en el archivo.

    json.dump(datos,archivo,indent=4)
  print(f"Archivo: {nombre_archivo} creado exitosamente.")

#Funcion para crear un archivo CSV

def crear_archivo_csv (nombre_archivo,datos):

  with open(nombre_archivo,'w',newline='') as archivo:

    escritor_csv = csv.writer(archivo)

    #Creando un objeto que escribe 

    escritor_csv.writerows(datos)
  print(f"Archivo: {nombre_archivo} creado exitosamente")

#Funcion leer el archivo txt

def leer_archivo_txt(nombre_archivo):

  with open(nombre_archivo,'r') as archivo:
    return archivo.read()
  
#Funcion leer el archivo CSV
def leer_archivo_csv(nombre_archivo):

  with open(nombre_archivo,'r') as archivo:

    #Lee el contenido del csv y lo transforma en una lista de listas o matriz bidimensional 
    return list(csv.reader(archivo))
  
#Funcion leer el archivo JSON
def leer_archivo_json(nombre_archivo):

  with open(nombre_archivo,'r') as archivo:

    #Lee el contenido del archivo JSON y lo convierte a un diccionario 
    return json.load(archivo)

#Funcion para agregar contenido a un archivo de texto existente
def agregar_contenido_txt(nombre_archivo,contenido):

  with open(nombre_archivo, 'a') as archivo:

    archivo.write(contenido)
  print(f"Contenido agregado al archivo: {nombre_archivo} exitosamente.")
  contenido_txt = "wenisimaaaa es un ejemplo"
  crear_archivo_txt('ejemplo_crear_archivo.txt', contenido_txt)

  #Datos para el archivo CSV
datos_csv = [

  ['Nombre','Edad','Ciudad'],
  ['Benja',18,'Calbuco'],
   ['Demente',23,'Puerto Montt']

  ]

crear_archivo_csv('Ejemplo.csv',datos_csv)



  #Datos para el JSON
datos_json = {

    'Nombre':'Rata',
    'Edad': 16,
    'Ciudad': 'Calbuco',
    'habilidades' : ['Python', 'Java', 'SQL']

  }
crear_archivo_json('ejemplo.json', datos_json)

#Leer el contenido 

print("Contenido del archivo de texto")
print(leer_archivo_txt('ejemplo_crear_archivo.txt'))

#Leer el contenido

print("Contenido del archivo de CSV")
for fila in leer_archivo_csv('Ejemplo.csv'):

  print(fila)

#leer y mostrar el contenido JSON

print("contenido del archivo JSON")
print(json.dumps(leer_archivo_json("ejemplo.json"),indent=4))

#txt adicioanal

contenido_adicional_txt = "\nEste es un contenido adicional"
agregar_contenido_txt("ejemplo_crear_archivo.txt",contenido_adicional_txt)
print("\n Contenido actualizado del txt")
print(leer_archivo_txt("ejemplo_crear_archivo.txt"))