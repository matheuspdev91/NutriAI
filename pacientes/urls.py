from django.urls import path

from . import views

urlpatterns = [
    path("", views.listar_pacientes, name="listar_pacientes"),

    path(
        "novo/",
        views.novo_paciente,
        name="novo_paciente"
    ),

    path(
        "<int:paciente_id>/",
        views.detalhe_paciente,
        name="detalhe_paciente"
    ),

    path(
        "<int:paciente_id>/anamnese/",
        views.cadastrar_anamnese,
        name="cadastrar_anamnese"
    ),
    
    path("home/", views.home, name="home")
]