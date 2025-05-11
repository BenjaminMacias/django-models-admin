from django.urls import path

from pages import views
from .views import mostrar_objetos 

urlpatterns = [
    path("", views.home, name="home"),
    path('objetos/', mostrar_objetos, name='mostrar_objetos'), 
]
