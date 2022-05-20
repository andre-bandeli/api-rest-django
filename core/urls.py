
from re import template
from django.urls import path

from .views import home, cadastrar_usuario


urlpatterns = [
    path('', home, name="index"),
    path('novouser', cadastrar_usuario, name="register"),
]
