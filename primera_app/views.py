from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import *



def familiar(request):
    familiar_1 = Familia(nombre = "Julio", apellido = "Salazar", edad = 20, fecha_nacimiento = 2002-2-5)
    # familiar_1.save()
    diccionario = {"familiar_1" : familiar_1}
    plantilla = loader.get_template("familiares.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)
