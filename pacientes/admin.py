from django.contrib import admin
from .models import Paciente, Anamnese,HabitosAlimentares, Avaliacao, Adipometria, Circunferencia, Resultado

admin.site.register(Paciente)
admin.site.register(Anamnese)
admin.site.register(HabitosAlimentares)
admin.site.register(Avaliacao)
admin.site.register(Adipometria)
admin.site.register(Circunferencia)
admin.site.register(Resultado)

# Register your models here.
