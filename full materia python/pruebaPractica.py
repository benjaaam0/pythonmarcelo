import json

def agregar_libro(libros, titulo, autor):
    """Agrega un nuevo libro a la lista de libros."""
    libro = {
        "titulo": titulo,
        "autor": autor,
        "estado": "disponible"
    }
    libros.append(libro)
    print(f"Libro '{titulo}' de {autor} agregado exitosamente.")

def marcar_prestado(libros, titulo):
    """Marca un libro como prestado por su título."""
    for libro in libros:
        if libro["titulo"] == titulo:
            if libro["estado"] == "disponible":
                libro["estado"] = "prestado"
                print(f"Libro '{titulo}' ha sido marcado como prestado.")
                return
            else:
                print(f"El libro '{titulo}' ya está prestado.")
                return
    print(f"Libro '{titulo}' no encontrado en la colección.")

def listar_libros(libros):
    """Imprime todos los libros con su estado."""
    if not libros:
        print("No hay libros en la colección.")
    for libro in libros:
        print(f"Título: {libro['titulo']}, Autor: {libro['autor']}, Estado: {libro['estado']}")

def guardar_libros(libros, nombre_archivo):
    """Guarda la lista de libros en un archivo JSON."""
    with open(nombre_archivo, 'w') as archivo:
        json.dump(libros, archivo, indent=4)
    print(f"Libros guardados en el archivo '{nombre_archivo}'.")

def cargar_libros(nombre_archivo):
    """Carga los libros desde un archivo JSON y devuelve la lista de libros."""
    try:
        with open(nombre_archivo, 'r') as archivo:
            libros = json.load(archivo)
        print(f"Libros cargados desde el archivo '{nombre_archivo}'.")
        return libros
    except FileNotFoundError:
        print(f"Archivo '{nombre_archivo}' no encontrado.")
        return []

# Ejemplo de uso
if __name__ == "__main__":
    # Inicializamos la lista de libros
    coleccion_libros = []
    
    # Agregamos algunos libros
    agregar_libro(coleccion_libros, "Cien Años de Soledad", "Gabriel García Márquez")
    agregar_libro(coleccion_libros, "Don Quijote de la Mancha", "Miguel de Cervantes")
    
    # Listamos todos los libros
    listar_libros(coleccion_libros)
    
    # Marcamos un libro como prestado
    marcar_prestado(coleccion_libros, "Cien Años de Soledad")
    
    # Listamos todos los libros para verificar el cambio de estado
    listar_libros(coleccion_libros)
    
    # Guardamos los libros en un archivo JSON
    guardar_libros(coleccion_libros, "libros.json")
    
    # Cargamos los libros desde un archivo JSON
    nueva_coleccion_libros = cargar_libros("libros.json")
    
    # Listamos la nueva colección para verificar la carga
    listar_libros(nueva_coleccion_libros)
