# -*- coding: utf-8 -*-
from django.contrib import admin
from comunidadingenio.profesores.models import (
    Ciudad, Comuna, Colegio, Asignatura, Capacitacion, Profesor
)

class ComunaInline(admin.TabularInline):
    model = Comuna

class CiudadAdmin(admin.ModelAdmin):
    inlines = [ComunaInline]

class ColegioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'direccion', 'comuna')
    list_filter = ('tipo', 'comuna__ciudad', 'comuna')
    search_fields = ['nombre']

class AsignaturaAdmin(admin.ModelAdmin):
    pass

class CapacitacionAdmin(admin.ModelAdmin):
    pass

class ProfesorAdmin(admin.ModelAdmin):
    filter_horizontal = ('capacitaciones',)
    list_display = ('nombre', 'email', 'celular', 'colegio', 'asignatura',
                    'educacion')
    list_filter = ('educacion', 'asignatura', 
                   'capacitaciones',
                   'colegio__comuna__ciudad', 'colegio__comuna',
                   'colegio')
    search_fields = ['nombre', 'email', 'celular', 
                     'colegio__nombre', 'asignatura__nombre']
    actions = ['send_email']
    def send_email(self, request, queryset):
        self.message_user(request, "No implementado aún")
    send_email.short_description = 'Enviar email'

admin.site.register(Ciudad)
admin.site.register(Comuna)
admin.site.register(Colegio, ColegioAdmin)
admin.site.register(Asignatura, AsignaturaAdmin)
admin.site.register(Capacitacion, CapacitacionAdmin)
admin.site.register(Profesor, ProfesorAdmin)


