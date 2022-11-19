from django.contrib import admin
from django.urls import path

from web.views import Home,PlatosVista,EmpleadosVista #importo desde la carpeta web/views la funcion home
urlpatterns = [
    path('admin/', admin.site.urls), #se queda por default
    path('', Home, name='H'),  
    path('platos/', PlatosVista, name='P'), #name es opcional, es un sobrenombre para las url lasrgas
    path('empleados/', EmpleadosVista, name='E'), #name es opcional, es un sobrenombre para las url lasrgas
]
