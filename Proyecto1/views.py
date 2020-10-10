from datetime import datetime
from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render
import os

# Cada función creada en el archivo 'views' es llamada "vista"
# Una vista recibe como primer argumento un objeto request
# Una vista devuelve un objeto HttpResponse
def saludo(request): #Vista saludo.
    return HttpResponse("Hola Mundo!")

def despedida(request):
    return HttpResponse('Adios Mundo!')

# Cargando vistas manualmente con el metodo open.
def plantilla(request):
    doc_externo = open(os.getcwd() + '/Proyecto1/templates/plantilla.html')

    plt = Template(doc_externo.read())

    doc_externo.close()

    ctx = Context({"nombre": "Momantai", "tags": ['Mensajes', 'Amigos', 'Social']})

    documento = plt.render(ctx)

    return HttpResponse(documento)

# Cargando vistas con cargadores (loader)
def plantilla_dos(request):
    template = loader.get_template('plantillados.html')

    return HttpResponse(template.render({"nombre": "Momantai"}))

# Cargando vistas con shortcuts con el metodo render.
def plantilla_dos_render(request):
    return HttpResponse(render(request, 'plantillados.html', {"nombre": "Momantai"}))

def fecha(request):
    fecha_actual = datetime.now()

    html = f"""
        Fecha y hora actuales: {fecha_actual} 
    """

    return HttpResponse(html)

def calculaEdad(request, edad, anio):
    periodo = anio-2020
    edadFutura = edad + periodo

    html = f"En el año {anio} tendras {edadFutura}"

    return HttpResponse(html)
