# -*- coding: utf-8 -*-
from django.db import models

class Ciudad(models.Model):
    nombre = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "Ciudades"
    def __unicode__(self):
        return self.nombre

class Comuna(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.ForeignKey(Ciudad)
    def __unicode__(self):
        return self.nombre

class Colegio(models.Model):
    TIPOS = (
        ('M', 'Municipal'),
        ('S', 'Particular Subvencionado'),
        ('P', 'Particular')
    )
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=1, choices=TIPOS)
    direccion = models.CharField(max_length=200)
    comuna = models.ForeignKey(Comuna)
    def __unicode__(self):
        return self.nombre
    
class Asignatura(models.Model):
    nombre = models.CharField(max_length=100)
    def __unicode__(self):
        return self.nombre

class Capacitacion(models.Model):
    nombre = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "Capacitaciones"
    def __unicode__(self):
        return self.nombre
    
class Profesor(models.Model):
    TIPOS_EDUCACION = (
        ('B', 'Básica'),
        ('M', 'Media')
    )
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    celular = models.CharField(max_length=15)
    colegio = models.ForeignKey(Colegio)
    asignatura = models.ForeignKey(Asignatura)
    educacion = models.CharField(max_length=1, choices=TIPOS_EDUCACION)
    capacitaciones = models.ManyToManyField(Capacitacion, 
                                            related_name="profesores",
                                            blank=True)
    class Meta:
        verbose_name_plural = "Profesores"
    def __unicode__(self):
        return self.nombre

