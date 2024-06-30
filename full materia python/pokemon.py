import tkinter as tk
import requests
import random
from io import BytesIO
from PIL import Image, ImageTk


def obtener_descripcion_pokemon(numero_especie):

  url = f"https://pokeapi.co/api/v2/pokemon-species/{numero_especie}"

  response = requests.get(url)

  if response.status_code == 200:

    data = response.json()

    descriptions = [desc['flavor_text'] for desc in data['flavor_text_entries'] if desc['language']['name'] == 'es']

    if descriptions:

      descripcion = descriptions[0].replace('\n', ' ')

      return descripcion

    else:

      return "No se encontró una descripción en español para este Pokémon."

  else:

    return "No se pudo obtener la descripción del Pokémon."

def buscar_pokemon(nombre_pokemon):

  url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon}"

  response = requests.get(url)

  if response.status_code == 200:

    data = response.json()
    nombre = data["name"]
    numero = data["id"]
    tipos = [tipo["type"]["name"] for tipo in data["types"]]
    stats = {stat['stat']['name']: stat['base_stat'] for stat in data['stats']}
    descripcion = obtener_descripcion_pokemon(numero)
    imagen_url = data["sprites"]["front_default"]
    response_imagen = requests.get(imagen_url)
    image = Image.open(BytesIO(response_imagen.content))
    imagen = image.resize((300,300), Image.Resampling.LANCZOS)
    foto = ImageTk.PhotoImage(imagen)

    label_imagen.config(image=foto)
    label_imagen.image = foto
    resultado = f"Nombre: {nombre}\nNúmero: {numero}\nTipo(s): {', '.join(tipos)}\nEstadísticas:\n{stats}\nDescripción: {descripcion}"

  else:

    resultado = "No se encontró el Pokémon."

    label_imagen.config(image=None)

  label_resultado.config(text=resultado)

def buscar_pokemon_aleatorio():

  pokemon_id = random.randint(1, 1025)

  buscar_pokemon(str(pokemon_id))

def limpiar_pokemon():

  entry_pokemon.delete(0, tk.END) # Borra el contenido del Entry
  label_resultado.config(text="") # Borra el texto del resultado
  label_imagen.config(image='') # Borra la imagen asignando una cadena vacía al atributo image

window = tk.Tk()
window.title("Encuentra tu Pokémon")

entry_pokemon = tk.Entry(window)
entry_pokemon.pack()

button_buscar = tk.Button(window, text="Buscar", command=lambda: buscar_pokemon(entry_pokemon.get().lower()))
button_buscar.pack()

button_pokemon_aleatorio = tk.Button(window, text="Mostrar Pokémon Aleatorio", command=buscar_pokemon_aleatorio)
button_pokemon_aleatorio.pack()

button_limpiar = tk.Button(window, text="Limpiar", command=limpiar_pokemon)
button_limpiar.pack()

label_resultado = tk.Label(window, text="")
label_resultado.pack()

label_imagen = tk.Label(window)
label_imagen.pack()

window.mainloop()