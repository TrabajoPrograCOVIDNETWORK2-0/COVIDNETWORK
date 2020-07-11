from django.http import HttpResponse , HttpRequest
from django.template import RequestContext
from django.template import Template,Context
from django.db import models
from django.shortcuts import render


def index(request):
    return render(request, "0html_startup.html")
#__________________________________________________________________________________________
def formulario(request):
    return render(request, "1formulario.html")
#__________________________________________________________________________________________
def covidsi(request):
    return render(request, "2covidsi.html")
#__________________________________________________________________________________________
def covidno(request):
    return render(request, "2covidno.html")
 #__________________________________________________________________________________________
def viejosi(request):
    return render(request, "3viejosi.html")
     #__________________________________________________________________________________________
def viejono(request):
    return render(request, "3viejono.html")
     #__________________________________________________________________________________________
def cardiosi(request):
    return render(request, "4cardiosi.html")
     #__________________________________________________________________________________________
def cardiono(request):
    return render(request, "4cardiono.html")
         #__________________________________________________________________________________________
def inmuno(request):
    return render(request, "5inmuno.html")
         #__________________________________________________________________________________________
def inmusi(request):
    return render(request, "5inmusi.html")
             #__________________________________________________________________________________________
def salsi(request):
    return render(request, "6salsi.html")
         #__________________________________________________________________________________________
def salno(request):
    return render(request, "6salno.html")
             #__________________________________________________________________________________________
def informacion(request):
    return render(request, "informaciones.html")
