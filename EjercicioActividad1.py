from datetime import date

# Clase Museo
class Museo:
    def __init__(self, nombre, año_fundacion):
        self.nombre = nombre
        self.año_fundacion = año_fundacion

    def __str__(self):
        return f"Museo: {self.nombre}, Fundado en: {self.año_fundacion}"

# Clase Artista
class Artista:
    def __init__(self, id_artista, nombre, nacionalidad, obra_famosa):
        self.id = id_artista
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.obra_famosa = obra_famosa

    def __str__(self):
        return f"Artista: {self.nombre} ({self.nacionalidad}), Obra Famosa: {self.obra_famosa}"

# Clase Coleccion
class Coleccion:
    def __init__(self, nombre_coleccion):
        self.nombre_coleccion = nombre_coleccion

    def __str__(self):
        return f"Colección: {self.nombre_coleccion}"

# Clase Evento
class Evento:
    def __init__(self, nombre, fecha, descripcion):
        self.nombre = nombre
        self.fecha = fecha
        self.descripcion = descripcion

    def __str__(self):
        return f"Evento: {self.nombre}, Fecha: {self.fecha}, Descripción: {self.descripcion}"

# Clase Exposicion
class Exposicion:
    def __init__(self, artista, año, tema):
        self.artista = artista
        self.año = año
        self.tema = tema

    def __str__(self):
        return f"Exposición: {self.tema} por {self.artista}, Año: {self.año}"

# Clase Guia
class Guia:
    def __init__(self, nombre, apellido, nacionalidad, id_empleado):
        self.nombre = nombre
        self.apellido = apellido
        self.nacionalidad = nacionalidad
        self.id_empleado = id_empleado

    def __str__(self):
        return f"Guía: {self.nombre} {self.apellido} ({self.nacionalidad}), ID Empleado: {self.id_empleado}"

# Clase Obra
class Obra:
    def __init__(self, nombre_obra, nombre_artista, año_creacion):
        self.nombre_obra = nombre_obra
        self.nombre_artista = nombre_artista
        self.año_creacion = año_creacion

    def __str__(self):
        return f"Obra: {self.nombre_obra} por {self.nombre_artista}, Año: {self.año_creacion}"

# Clase Ticket
class Ticket:
    def __init__(self, tipo_entrada, precio, codigo):
        self.tipo_entrada = tipo_entrada
        self.precio = precio
        self.codigo = codigo

    def __str__(self):
        return f"Ticket: {self.tipo_entrada}, Precio: {self.precio}, Código: {self.codigo}"

# Clase Visitante
class Visitante:
    def __init__(self, nombre, apellido, nacionalidad, id_visitante):
        self.nombre = nombre
        self.apellido = apellido
        self.nacionalidad = nacionalidad
        self.id_visitante = id_visitante

    def __str__(self):
        return f"Visitante: {self.nombre} {self.apellido} ({self.nacionalidad}), ID Visitante: {self.id_visitante}"

# Clase principal
def main():

    # Crear un museo
    museo = Museo("Museo del Arte Contemporaneo", 2024)
    print(museo)

    # Crear un artista
    artista = Artista("1002192744", "Octavio Martinez", "Colombiana", "Habitos atomicos")
    print(artista)

    # Crear una colección
    coleccion = Coleccion("Colección de Arte Contemporaneo")
    print(coleccion)

    # Crear un evento
    evento = Evento("Exposición de Martinez", date.today(), "Una muestra de las obras de Martinez")
    print(evento)

    # Crear una exposición
    exposicion = Exposicion("Octavio Martinez", 2024, "Arte Contemporaneo")
    print(exposicion)

    # Crear un guía
    guia = Guia("Jonathan", "Tobon", "Colombiana", "1234792378")
    print(guia)

    # Crear una obra
    obra = Obra("Habitos Atomico", "Octavio Martinez", 2020)
    print(obra)

    # Crear un ticket
    ticket = Ticket("Entrada General", 50000, "TICKET1")
    print(ticket)

    # Crear un visitante
    visitante = Visitante("Alexis", "Paez", "Australiana", "1003456324")
    print(visitante)

# Ejecutar la clase principal
if __name__ == "__main__":
    main()
