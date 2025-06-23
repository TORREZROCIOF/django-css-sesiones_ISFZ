from django.urls import path
from . import views

urlpatterns = [
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),
    path('editar/', views.editar_perfil, name='editar_perfil'),
]