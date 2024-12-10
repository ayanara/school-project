from django.contrib import admin

from .models import Curso, Aluno, Coordenador, Professor, Matricula, Turma, Disciplina, Atividade


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Informações Básicas ', {'fields': ('nome', 'descricao')}),
        ('Horário ', {'fields': ('periodo', 'modalidade')})

    ]

    list_display = ('nome', 'descricao', 'periodo', 'modalidade')

    search_fields = ['nome']

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Informações do Aluno ', {'fields': ('ra', 'usuario')}),

    ]

    list_display = ('ra', 'usuario')

    search_fields = ['ra']

@admin.register(Coordenador)
class CoordenadorAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Informações do Coodernador ', {'fields': ('usuario', 'celular')}),

    ]

    list_display = ('usuario', 'celular')

    search_fields = ['usuario']


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Informações do Professor ', {'fields': ('usuario', 'celular')}),
        ('Disciplinas Lecionadas ', {'fields': ('disciplina',)}),

    ]

    list_display = ('usuario', 'celular')

    search_fields = ['usuario']


@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Informações da disciplina ', {'fields': ('nome', 'carga_horaria')}),
        ('participantes ', {'fields': ('curso',)}),

    ]

    list_display = ('nome', 'carga_horaria')


@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Informações da turma ', {'fields': ('turma', 'curso', 'semestre')}),

    ]

    list_display = ('turma', 'curso', 'semestre')

@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Informações da matricula ', {'fields': ('aluno', 'curso', 'turma', 'dt_inicio', 'dt_final', 'status')}),

    ]

    list_display = ('aluno', 'curso', 'turma', 'dt_inicio', 'dt_final', 'status')


@admin.register(Atividade)
class AtividadeAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Atividade', {'fields': ('titulo', 'descricao', 'status', 'atividade',)}),
        ('Profesor', {'fields': ('professor',)}),
        ('Disciplina', {'fields': ('disciplina',)}),
        ('Datas', {'fields': ('dt_inicio', 'dt_final',)}),

    ]

    list_display = ('titulo', 'descricao', 'status', 'atividade','dt_inicio', 'dt_final', 'professor', 'disciplina')