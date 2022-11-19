# esto se llama views sin embargo funciona realmente como controllers
from django.shortcuts import render
# from carpeta web. carpeta formularios.nombre_de_archivo import clase
from web.formularios.formularioPlatos import FormulariosRegistrosPlatos
# from carpeta web. carpeta formularios.nombre_de_archivo import clase
from web.formularios.formularioEmpleados import FormulariosRegistrosEmpleados
# from carpeta web. carpeta models .nombre_de_archivo import clase 
from web.models import Platos, Empleados


# Create your views here.
#cada vista es una funcion de PY
def Home(request):
    return render(request,'index.html')

def PlatosVista(request):
    # cargar o instanciar el formulario de registros de platos
    formulario = FormulariosRegistrosPlatos()
    # en formularios tengo los inputs y estos deben irse para la vista, por eso creamos un diccionario para enviar datos al template/platos
    diccionarioEnvioDatos = {
        'formulario':formulario
    }
    # cargar las registros

    # recibiendo datos del formulario 
    # peticion tipo post DESDE EL FORMULARIO HTML  platos.html
    if request.method == 'POST':
        datosFormulario = FormulariosRegistrosPlatos(request.POST)
        # imprimimos sin filtrar e imprime una tabla
        # print(datosFormulario)
        # ahora filtramos para que no nos salga basura
        if datosFormulario.is_valid():
            datosLimpios=datosFormulario.cleaned_data
            #print(datosLimpios)
            #datos enviados a la base de datos
            platoNuevo=Platos(
                nombre=datosLimpios['nombrePlato'],
                descripcion=datosLimpios['descripcionPlato'],
                imagen=datosLimpios['fotoPlato'],
                precio=datosLimpios['precioPlato'],
                tipo=datosLimpios['tipoPlato']
            ) # instancio el models plato en el objeto platoNuevo
            platoNuevo.save()
    return render(request,'platos.html',diccionarioEnvioDatos)


def EmpleadosVista(request):
    # cargar o instanciar el formulario de registros de platos
    formulario = FormulariosRegistrosEmpleados()
    # en formularios tengo los inputs y estos deben irse para la vista, por eso creamos un diccionario para enviar datos al template/platos
    diccionarioEnvioDatos = {
        'formulario':formulario
    }
    # cargar las registros

    # recibiendo datos del formulario 
    # peticion tipo post DESDE EL FORMULARIO HTML  platos.html
    if request.method == 'POST':
        datosFormulario = FormulariosRegistrosEmpleados(request.POST)
        # imprimimos sin filtrar e imprime una tabla
        # print(datosFormulario)
        # ahora filtramos para que no nos salga basura
        if datosFormulario.is_valid():
            datosLimpios=datosFormulario.cleaned_data
            #print(datosLimpios)
            #datos enviados a la base de datos
            empleadoNuevo=Empleados(
                nombre=datosLimpios['nombreEmpleado'],
                apellido=datosLimpios['apellidoEmpleado'],
                cargo=datosLimpios['cargoEmpleado'],
                direccion=datosLimpios['direccionEmpleado'],
            ) # instancio el models plato en el objeto platoNuevo
            empleadoNuevo.save()
    return render(request,'empleados.html',diccionarioEnvioDatos)