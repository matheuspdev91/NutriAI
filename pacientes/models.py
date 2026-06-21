from django.db import models

# ===============
# PACIENTES
# ==============


class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=10)
    data_nascimento = models.DateField()
    altura = models.FloatField()
    peso = models.FloatField()

    email = models.EmailField()
    telefone = models.CharField(max_length=20, blank=True, null=True)

    criado_em = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return self.nome


# ===========
# ANAMNESE
# ==========

class Anamnese(models.Model):
    paciente = models.OneToOneField(
        Paciente,
        on_delete=models.CASCADE,
        related_name="anamnese"
    )

    objetivo = models.CharField(max_length=100)

    profissao = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    hora_de_sono = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True
    )

    consumo_de_agua = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True
    )

    medicamentos = models.TextField(
        blank=True,
        null=True
    )

    patologias = models.TextField(
        blank=True,
        null=True
    )

    alergias = models.TextField(
        blank=True,
        null=True
    )

    observacoes = models.TextField(
        blank=True,
        null=True
    )

    nivel_estresse = models.IntegerField(
    blank=True,
    null=True
)

    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Anamnese"- {self.paciente.nome}
    


# ===================
# HÁBITOS ALIMENTARES
# ===================

class HabitosAlimentares(models.Model):

    paciente = models.OneToOneField(
        Paciente,
        on_delete=models.CASCADE,
        related_name="habitos_alimentares"
    )

    cafe_da_manha = models.BooleanField(default=True)

    almoco = models.BooleanField(default=True)

    jantar = models.BooleanField(default=True)

    lanches = models.BooleanField(default=False)

    consumo_alcool = models.BooleanField(default=False)

    fumante = models.BooleanField(default=False)

    frequencia_fast_food = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    alimentos_preferidos = models.TextField(
        blank=True,
        null=True
    )

    alimentos_rejeitados = models.TextField(
        blank=True,
        null=True
    )

    suplementacao = models.TextField(
        blank=True,
        null=True
    )

    observacoes = models.TextField(
        blank=True,
        null=True
    )

    quantidade_refeicoes = models.IntegerField(
    blank=True,
    null=True

    )

    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Hábitos Alimentares - {self.paciente.nome}"


# ===============
# AVALIAÇÕES
# ===============


class Avaliacao(models.Model):
    OBJETIVOS = [
        ("Emagrecimento", "Emagrecimento"),
        ("Ganho de Massa Muscular", "Ganho de Massa Muscular"),
        ("Melhora da Saúde Geral", "Melhora da Saúde Geral"),
    ]

    paciente = models.ForeignKey(
        Paciente, on_delete=models.CASCADE, related_name="avaliacoes"
    )

    data_avaliacao = models.DateField()

    criado_em = models.DateTimeField(auto_now_add=True)


# ============
# ADIPOMETRIA
# ============


class Adipometria(models.Model):

    avaliacao = models.OneToOneField(
        Avaliacao, on_delete=models.CASCADE, related_name="adipometria"
    )

    tricipital = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )

    subescapular = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )

    supra_iliaca = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )

    abdominal = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )

    coxa = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    peito = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    axilar_media = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )


# =================
# CIRCUNFERENCIAS
# =================


class Circunferencia(models.Model):

    avaliacao = models.OneToOneField(
        Avaliacao, on_delete=models.CASCADE, related_name="circunferencias"
    )

    ombros = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    torax = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    cintura = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    abdome = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    quadril = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    braco_direito = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )

    braco_esquerdo = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )

    coxa_direita = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )

    coxa_esquerda = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )

    panturrilha_direita = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )

    panturrilha_esquerda = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )

    def __str__(self):
        return f"Circunferências - {self.avaliacao.paciente.nome}"


# ============
# RESULTADOS
# ============


class Resultado(models.Model):
    avaliacao = models.OneToOneField(
        Avaliacao, on_delete=models.CASCADE, related_name="resultado"
    )

    densidade_corporal = models.FloatField(null=True, blank=True)

    percentual_gordura = models.FloatField(null=True, blank=True)

    massa_magra = models.FloatField(null=True, blank=True)

    massa_gorda = models.FloatField(null=True, blank=True)

    tmb = models.FloatField(null=True, blank=True)

    get = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"Resultado - {self.avaliacao.paciente.nome}"
