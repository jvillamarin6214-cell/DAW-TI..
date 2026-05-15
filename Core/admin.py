from django.contrib import admin
from Core.models import Persona

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ['nombres', 'apellidos', 'correo', 'titulo_academico']
