from django.contrib import admin

from .models import Causa, Entidad, Oportunidad


@admin.register(Causa)
class CausaAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
    search_fields = ("nombre",)


@admin.register(Entidad)
class EntidadAdmin(admin.ModelAdmin):
    list_display = ("nombre", "web", "email")
    search_fields = ("nombre",)


@admin.register(Oportunidad)
class OportunidadAdmin(admin.ModelAdmin):
    list_display = ("titulo", "causa", "fecha_inicio", "lugar", "plazas")
    list_filter = ("causa", "entidades")
    search_fields = ("titulo", "lugar")
    date_hierarchy = "fecha_inicio"
    # asi es mas facil elegir las entidades
    filter_horizontal = ("entidades",)
