from django.db import models

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
    periodo = models.CharField(max_length=20, choices=escolha_periodo, default='MATUTINO')
    modalidade = models.CharField(max_length=20, choices=escolha_modalidade, default='PRESENCIAL')

    def __str__(self):
        return self.nome

