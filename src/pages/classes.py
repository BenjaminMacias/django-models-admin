# Ejemplo de clases Python

class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio

    def descripcion(self):
        return f"{self.titulo} por {self.autor}, publicado en {self.anio}"

class Mascota:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def descripcion(self):
        return f"{self.nombre} es un(a) {self.especie} y tiene {self.edad} años"
