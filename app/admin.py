from django.contrib import admin

from .models import Curso


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Informações Básicas ', {'fields': ('nome', 'descricao')}),
        ('Horário ', {'fields': ('periodo', 'modalidade')})

    ]

    list_display = ('nome', 'descricao', 'periodo', 'modalidade')
