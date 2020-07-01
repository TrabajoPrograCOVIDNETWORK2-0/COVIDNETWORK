from django.http import HttpResponse
from django.template import RequestContext
from django.template import Template,Context
from django.db import models
from django.shortcuts import render


def index(request):
 #   doc_externo: str= "C:/Users/sdiaz/OneDrive/Escritorio/ProyextoPROGRA/proyecto1/proyecto1/plantillas/html_startup.html"
 #   plt= Template(doc_externo.read())
 #   doc_externo.close()
 #   ctx= Context()
 #   html_startup = plt.render(ctx)
    return render(request, "html_startup.html")

#__________________________________________________________________________________________
def formulario(request):
    return render(request, "formu.html")
#__________________________________________________________________________________________
def rutcovi(request):
    rut = 17345908-7
    print("Bienvenido al programa de control de COVID")
    permisos = ['18837903-K', '18:30', '18836902-K', '19:15','20857683-6', '4:20']
    contagiados = ['17345908-7', '12677800-3', '9990234-1', '18836902-K']
    datos = ['Andrea Campos', '17345908-7', 1968, 'Raquel Salinas',
             '4231998-K', 1940, 'Pedro Meza', '12677800-3', 1975, 'Sergio Pezoa',
             '9990234-1', 1965, 'Alvaro Vasquez', '18836902-K', 1970, 'Jaime Oliva',
             '18837903-K', 1997,'Anne-Sophie Cataldo','20857683-6', 2001]
    # Para saber si tiene Co-Vid
    covid = 0
    for x in range(0, len(contagiados) - 1, 1):
        c = contagiados[x]
        if (rut == c):
            covid = 1
    # Para saber si tiene permiso
    permiso = 0
    horario = 0
    if (covid == 0):
        for x in range(0, len(permisos) - 1, 1):
            p = permisos[x]
            if (rut == p):
                permiso = 1
                horario = permisos[x + 1]  # Horario
    # Para saber la edad y
    verif = 0
    for x in range(0, len(datos) - 1, 1):
        d = datos[x]
        if (rut == d):
            nombre = datos[x - 1]
            año = datos[x + 1]
            verif = 1
    # imprimir dependiendo de lo que tenga
    if (verif == 1):
        if (covid == 1):
            resp =(f"{nombre} RUT: {rut} registra COVID")
        elif (covid == 0):
            if (permiso == 1):
                resp =(f"{nombre} RUT: {rut} tiene permiso temporal hasta las {horario} horas.")
            elif (permiso == 0):
                if (año <= 1945):
                    resp =(f"{nombre} RUT: {rut} es mayor de 75 años y no tiene permiso temporal")
                elif (año > 1945):
                    resp =(f"{nombre} RUT: {rut} no tiene permiso temporal")
    elif (verif == 0):
        resp =("El rut no se encuentra en la base de datos.") 
    return render(request, "covidchecker.html")

#__________________________________________________________________________________________
