from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import *



def familiar(request):
    familiar_1 = Familia(nombre = "Julio", apellido = "Salazar", edad = "20", fecha_nacimiento = "2002-2-5")
    familiar_2 = Familia(nombre = "Paola", apellido = "Salazar", edad = "23", fecha_nacimiento = "1999-9-18")
    familiar_3 = Familia(nombre = "Julio", apellido = "Salazar", edad = "50", fecha_nacimiento = "1972-12-23")
    familiar_4 = Familia(nombre = "Mercedes", apellido = "Salazar", edad = "48", fecha_nacimiento = "1974-11-17")
    # familiar_1.save()
    # familiar_2.save()
    # familiar_3.save()
    # familiar_4.save()

    diccionario = {
        "familiar_1" : familiar_1,
        "familiar_2" : familiar_2,
        "familiar_3" : familiar_3,
        "familiar_4" : familiar_4,
        }
        
    plantilla = loader.get_template("familiares.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)
