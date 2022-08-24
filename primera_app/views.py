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


def animal(request):
    animal_1 = Animal(nombre = "lobo", habitad = "montañas", esperanza_vida = "20", puede_volar = False)
    animal_2 = Animal(nombre = "colibri", habitad = "selvas", esperanza_vida = "10", puede_volar = True)
    animal_3 = Animal(nombre = "pato", habitad = "lagos", esperanza_vida = "15", puede_volar = True)

    # animal_1.save()
    # animal_2.save()
    # animal_3.save()

    diccionario = {
        "animal_1" : animal_1,
        "animal_2" : animal_2,
        "animal_3" : animal_3,
    }

    plantilla = loader.get_template("animales.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)