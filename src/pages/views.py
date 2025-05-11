import os

from django import get_version
from django.conf import settings
from django.shortcuts import render

from django.http import HttpResponse
from .classes import Libro, Mascota  # importar clases creadas


def home(request):
    context = {
        "debug": settings.DEBUG,
        "django_ver": get_version(),
        "python_ver": os.environ["PYTHON_VERSION"],
    }

    return render(request, "pages/home.html", context)


def mostrar_objetos(request):
    libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 1967)
    mascota1 = Mascota("Firulais", "perro", 3)

    # Ejemplos de uso y atributos mostrados en la página
    contenido = f"""
    <h2>Libro: {libro1.titulo}</h2>
    <p>{libro1.descripcion()}</p>
    
    <h2>Mascota: {mascota1.nombre}</h2>
    <p>{mascota1.descripcion()}</p>
    """

    return HttpResponse(contenido)