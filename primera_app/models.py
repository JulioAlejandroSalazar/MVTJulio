from django.db import models


class Familia(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()

class Animal(models.Model):
    nombre = models.CharField(max_length=20)
    habitad = models.CharField(max_length=20)
    esperanza_vida = models.IntegerField()
    puede_volar = models.BooleanField()
