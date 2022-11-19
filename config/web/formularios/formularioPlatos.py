from django import forms
# esto es un formulario creado con django
class FormulariosRegistrosPlatos(forms.Form):
    # crear tupla que es un vector constante
    PLATOS=(
        (1, 'Entrada'),
        (2, 'Plato fuerte'),
        (3, 'Postres'),
        (4, 'Bebidas')
    )

    # input del formulario con sus atributos, esteas metodos son monoliticos se van enteros a la vista
    nombrePlato=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        max_length=25,
        required=True,
        label="Nombre de Plato"
    )
    descripcionPlato=forms.CharField(
        widget=forms.Textarea(attrs={"class":"form-control mb-3"}),
        max_length=50,
        required=True,
        label="descripcion Plato"
    )
    fotoPlato=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        required=True,
        label="foto Plato"
    )
    precioPlato=forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        max_length=200,
        required=True,
        label="precio Plato"
    )
    tipoPlato=forms.ChoiceField(
        widget=forms.Select(attrs={"class":"form-control mb-3"}),
        choices=PLATOS
    )