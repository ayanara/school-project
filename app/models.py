from django.db import models
from django.db.models import UniqueConstraint
from django.contrib.auth.models import User
from datetime import date

#Model Curso
class Curso(models.Model):

    MATUTINO = 'MATUTINO'
    NOTURNO = 'NOTURNO'
    DIURNO = 'DIURNO'

    escolha_periodo = [
        (MATUTINO, 'MATUTINO'),
        (NOTURNO, 'NOTURNO'),
        (DIURNO, 'DIURNO')
    ]

    PRESENCIAL = 'PRESENCIAL'
    ONLINE = 'ONLINE'

    escolha_modalidade = [
        (PRESENCIAL, 'PRESENCIAL'),
        (ONLINE, 'ONLINE')
    ]

    nome = models.CharField(max_length=30)
    descricao = models.CharField(max_length=500, default=None)
    periodo = models.CharField(max_length=20, choices=escolha_periodo, default=MATUTINO)
    modalidade = models.CharField(max_length=20, choices=escolha_modalidade, default=PRESENCIAL)

    def __str__(self):
        return self.nome
    
#Model Disciplina
class Disciplina(models.Model):
    nome = models.CharField('Disciplina', max_length=50, unique=True)
    curso = models.ManyToManyField(Curso)
    carga_horaria = models.IntegerField(verbose_name='Carga horaria')
    class Meta:
        verbose_name = 'Disciplina'
        verbose_name_plural =  'Disciplinas'

    def __str__(self):
        return self.nome
    
#Model Turma
class Turma(models.Model):
    A = 'Turma A'
    B = 'Turma B'
    C = 'Turma C'
    D = 'Turma D'

    escolha_turma = [
        (A, 'Turma A'),
        (B, 'Turma B'),
        (C, 'Turma C'),
        (D, 'Turma D'),
    ]

    PRIMEIRO_SEMESTRE = 'PRI-SEM'
    SEGUNDO_SEMESTRE = 'SEG-SEM'
    TERCEIRO_SEMESTRE = 'TER-SEM'
    QUARTO_SEMESTRE = 'QUA-SEM'

    escolha_semestre = [
        (PRIMEIRO_SEMESTRE, 'PRIMEIRO SEMESTRE'),
        (SEGUNDO_SEMESTRE, 'SEGUNDO SEMESTRE'),
        (TERCEIRO_SEMESTRE, 'TERCEIRO SEMESTRE'),
        (QUARTO_SEMESTRE, 'QUARTO SEMESTRE'),
    ]

    turma = models.CharField('Turma', max_length=7, choices=escolha_turma, default=None)
    disciplina = models.ManyToManyField(Disciplina)
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT, related_name='turmas')
    semestre = models.CharField(max_length=20, choices=escolha_semestre, default=PRIMEIRO_SEMESTRE)

    class Meta:
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'

        constraints = [
            UniqueConstraint(fields=['turma', 'curso', 'semestre'], name='unique_turma_curso_semestre',)
]

        def __str__(self):
            return self.turma

#Model Aluno
class Aluno(models.Model):
    ra = models.CharField(max_length=10, unique=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.usuario.first_name
    
    #Model Professor
class Professor(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Usuario')
    celular = models.CharField(max_length=20, verbose_name='Celular')
    disciplina = models.ManyToManyField(Disciplina, blank=True)

    def __str__(self):
        return self.usuario.username
    
#Model Coordenador
class Coordenador(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Usuario')
    celular = models.CharField(max_length=20, verbose_name='Celular')

    class Meta:
        verbose_name = 'Coordenador'
        verbose_name_plural = 'Coordenadores'

    def __str__(self):
        return self.usuario.last_name
    
#Model Matricula
class Matricula(models.Model):
    ATIVA = 'Atv'
    CANCELADA = 'Canc'
    EM_ANALISE = 'An'
    SOLICITADO = 'So'

    escolha_situacao = [
        (ATIVA, 'Ativa'),
        (CANCELADA, 'Cancelada'),
        (EM_ANALISE, 'Em Analise'),
        (SOLICITADO, 'Solicitada'),
    ]


    status = models.CharField(max_length=4, choices=escolha_situacao, default=None)
    aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT, related_name='matriculas')
    turma = models.ForeignKey(Turma, on_delete=models.PROTECT, related_name='matriculas')
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT, related_name='matriculas')
    dt_inicio = models.DateField()
    dt_final = models.DateField()
    
    class Meta:
        verbose_name = 'Matricula'
        verbose_name_plural = 'Matriculas'

        constraints = [
            UniqueConstraint(fields=['turma', 'curso', ], name='unique_turma',)
        ]

        def __str__(self) -> str:
            return self.status
        
# Models Atividades
class Atividade(models.Model):
    ABERTA = 'ABERTA'
    FECHADA = 'FECHADA'
    PRORROGADA = 'PRORROGADA'

    escolha_status = [
        (ABERTA,'ABERTA'),
        (FECHADA, 'FECHADA'),
        (PRORROGADA,'PRORROGADA'),
    ]

    ATV1 = 'ATV1'
    ATV2 = 'ATV2'
    ATV3 = 'ATV3'
    ATV4 = 'ATV4'
    

    escolha_atividade = [
        ( ATV1, 'ATV1'),
        ( ATV2, 'ATV2'),
        ( ATV3, 'ATV3'),
        ( ATV4, 'ATV4'),
    ]


    titulo = models.CharField(max_length=255, unique=True)
    descricao = models.TextField(max_length=255)
    status = models.CharField(max_length=10, choices=escolha_status)
    atividade = models.CharField('Atividade Complementar', max_length=4, choices=escolha_atividade)

    dt_inicio = models.DateField('Data inicio', default=date(year=1900, month=1, day=1))
    dt_final = models.DateField('Data Fim', default=date(year=1900, month=1, day=1))

    professor = models.ForeignKey(Professor, on_delete=models.PROTECT, related_name='atividade')

    disciplina = models.ForeignKey(Disciplina, on_delete=models.PROTECT, related_name='atividade')
    
    
    class Meta:
        verbose_name_plural = 'Atividades'

        def __str__(self):
            return self.titulo
    

