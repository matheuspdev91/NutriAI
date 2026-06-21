from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404

from .models import Paciente

def listar_pacientes(request):
    pacientes = Paciente.objects.all().order_by('nome')

    return render(
        request,
        "pacientes/listar.html",
        {"pacientes": pacientes}
    )

def novo_paciente(request):

    if request.method == "POST":

        Paciente.objects.create(
            nome=request.POST.get("nome"),
            sexo=request.POST.get("sexo"),
            altura=request.POST.get("altura"),
            peso=request.POST.get("peso"),
            data_nascimento=request.POST.get("data_nascimento"),
            email=request.POST.get("email"),
            telefone=request.POST.get("telefone"),
        )

        return redirect("listar_pacientes")
    return render(request, "pacientes/novo_paciente.html")

def detalhe_paciente(request, paciente_id):

    paciente = get_object_or_404(
        Paciente,
        id=paciente_id,
    )

    return render(
        request,
        "pacientes/detalhe.html",
        {"paciente": paciente},
    )

