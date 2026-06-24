from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .models import Anamnese, Paciente

from .models import Paciente

def listar_pacientes(request):
    pacientes = Paciente.objects.all().order_by('nome')

    return render(
        request,
        "pacientes/listar_pacientes.html",
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

    anamnese = getattr(paciente, "anamnese", None)
    print("PACIENTE:", paciente)
    print("ANAMNESE:", anamnese)

    return render(
        request,

        "pacientes/detalhe_paciente.html",
        {
        "paciente": paciente,
        "anamnese": anamnese,
        }
    )

# ===================
# HOME
# ===================
def home(request):
    return render(request, "pacientes/home.html")

# ===================
# CADASTRAR ANAMNESE
# ===================

def cadastrar_anamnese(request, paciente_id):

    paciente = get_object_or_404(
        Paciente,
        id=paciente_id
    )

    if request.method == "POST":

        Anamnese.objects.create(
            paciente=paciente,
            objetivo=request.POST.get("objetivo"),
            profissao=request.POST.get("profissao"),
            hora_de_sono=request.POST.get("hora_de_sono"),
            consumo_de_agua=request.POST.get("consumo_de_agua"),
            medicamentos=request.POST.get("medicamentos"),
            patologias=request.POST.get("patologias"),
            alergias=request.POST.get("alergias"),
            observacoes=request.POST.get("observacoes"),
            nivel_estresse=request.POST.get("nivel_estresse"),
        )

        return redirect(
            "detalhe_paciente",
            paciente_id=paciente.id
        )

    return render(
        request,
        "pacientes/anamnese.html",
        {
            "paciente": paciente
        }
    )

