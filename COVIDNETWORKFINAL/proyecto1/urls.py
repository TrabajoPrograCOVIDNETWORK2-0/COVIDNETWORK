"""proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from proyecto1.views import index, formulario, covidno, covidsi, viejosi, viejono, cardiono, cardiosi, inmusi, inmuno, salsi, salno, informacion

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('formulario/', formulario),
    path('formulario/covidno/', covidno),
    path('formulario/covidsi/', covidsi),
    path('formulario/covidno/viejosi/', viejosi),
    path('formulario/covidno/viejono/', viejono),
    path('cardiosi/', cardiosi),
    path('cardiono/', cardiono),
    path('cardiono/inmusi', inmusi),
    path('cardiono/inmuno', inmuno),
    path('cardiono/salsi', salsi),
    path('cardiono/salno', salno),
    path('informacion', informacion),
]
