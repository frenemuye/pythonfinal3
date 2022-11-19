from django import forms
# esto es un formulario creado con django
class FormulariosRegistrosEmpleados(forms.Form):
    # crear tupla que es un vector constante
    PLATOS=(
        (1, 'Entrada'),
        (2, 'Plato fuerte'),
        (3, 'Postres'),
        (4, 'Bebidas')
    )

    # input del formulario con sus atributos, esteas metodos son monoliticos se van enteros a la vista
    nombreEmpleado=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        max_length=25,
        required=True,
        label="Nombre del Empleado"
    )
    apellidoEmpleado=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        max_length=50,
        required=True,
        label="Apellidos del Empleado"
    )
    cargoEmpleado=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        required=True,
        label="Cargo del Empleado"
    )
    direccionEmpleado=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        max_length=200,
        required=True,
        label="Dirección del Empleado"
    )
