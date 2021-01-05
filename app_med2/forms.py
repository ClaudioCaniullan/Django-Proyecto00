from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from localflavor.cl.forms import CLRutField
import datetime
import json 




def validar_fecha(fecha):
    fecha_mayor = datetime.datetime.strptime("2020-12-31", "%Y-%m-%d").date()
    if fecha <= fecha_mayor:
        return fecha
    else:
        raise ValidationError("Sólo fechas de diciembre 2020")

class CrearUsuario(forms.Form):
    dni = forms.CharField(widget = forms.TextInput(
                                attrs = {'style': 'background-color: pink;'}),
                                    validators=[validators.MinLengthValidator(9, "Ingresar dni en el siguiente formato 77111666-5"), 
                                        validators.MaxLengthValidator(11, "Ingresar dni en el siguiente formato 77111666-5")])

    nombre = forms.CharField(widget = forms.TextInput(
                                attrs = {'style': 'background-color: green;'}),
                                    validators=[validators.MinLengthValidator(10, "El nombre debe tener minimo 10 caracteres"), 
                                        validators.MaxLengthValidator(30, "El nombre puede tener hasta 30 caracteres")])

    edad =  forms.IntegerField(widget = forms.TextInput( 
                                attrs = {'style': 'background-color: yellow;'}),
                                    validators=[validators.MinValueValidator(1, "Error, la edad no puede ser menor a 1 "),
                                        validators.MaxValueValidator(99, "Error, la edad no puede tener menos más de 3 numero")])

    direccion = forms.CharField(widget = forms.TextInput(
                                attrs = {'style': 'background-color: red;'}),
                                    validators=[validators.MinLengthValidator(10, "Error, la dirección debe contener más de 10 caracteres"),
                                                validators.MaxLengthValidator(50, "Error, la dirección puede contener hasta 30 caracteres ")])                                                
    tipo_usuario = forms.CharField(widget = forms.TextInput(
                                attrs = {'style': 'background-color: orange;'}),
                                    validators=[validators.MinLengthValidator(1, "El tipo de usuario puede ser A o U"),
                                                validators.MaxLengthValidator(1, "El tipo de usuario puede ser A o U")])
                                                        
    #fecha_creacion = forms.DateField(validators=[validar_fecha])

class Contacto(forms.Form):
    
    nombre = forms.CharField(widget = forms.TextInput(
                attrs = {'style': 'background-color: green;'}),
                validators=[validators.MinLengthValidator(10, "El nombre debe tener minimo 10 caracteres"), 
                validators.MaxLengthValidator(30, "El nombre puede tener hasta 30 caracteres")])

    email = forms.EmailField(widget = forms.TextInput(
                attrs = {'style': 'background-color: pink;'}))

    mensaje_email = forms.CharField(widget = forms.TextInput(
                attrs = {'style': 'background-color: yellow;'}),
                validators=[ validators.MaxLengthValidator(100, "El nombre puede tener hasta 30 caracteres")])

class rutPacientes(forms.Form):

     # Generar copia de los datos de usuarios
    with open('../proyecto_web/app_med2/data/usuarios.json', 'r') as file:
        pacientes=json.load(file)

    #Extraer ruts para lista desplegable de cambio de usuario
    rut_pacs=[]
    for p in pacientes:
        rut_pacs.append((p,p))

    rut_pac= forms.ChoiceField(choices=(rut_pacs))



class Hemograma(forms.Form):
    ''' Formulario Hemograma '''

    rut                 = forms.IntegerField()
    fecha_ingreso       = forms.DateField()
    eritrocito          = forms.DecimalField(
                                            max_digits=3,
                                            decimal_places=1,
                                            required=True
    )

    leucocitos          = forms.DecimalField(
                                            max_digits=3,
                                            decimal_places=1,
                                            required=True
    )

    hemoglobina         = forms.DecimalField(
                                            max_digits=3, 
                                            decimal_places=1,
                                            required=True
    )

    hematocrito         = forms.DecimalField(
                                            max_digits=3, 
                                            decimal_places=1, 
                                            required=True
    )

    vcm                 = forms.DecimalField(
                                            label='V.C.M.',
                                            max_digits=3, 
                                            decimal_places=1, 
                                            required=True
    )

    chcm                = forms.DecimalField(
                                            label='C.H.C.M.',
                                            max_digits=3, 
                                            decimal_places=1, 
                                            required=True
    )

    plaquetas           = forms.DecimalField(
                                            max_digits=4, 
                                            decimal_places=1, 
                                            required=True
    )

    observaciones       = forms.CharField(
                                            required=True
    )


class PerfilBioquimico(forms.Form):
    ''' Formulario Perfil Bioquimico '''

    rut                 = CLRutField()
    fecha_ingreso       = forms.DateField()
    glucosa             = forms.DecimalField(
                                            max_digits=3, 
                                            decimal_places=1,
                                            required=True
    )

    nitrogeno_ureico    = forms.DecimalField(
                                            max_digits=3, 
                                            decimal_places=1, 
                                            required=True
    )

    calcio              = forms.DecimalField(
                                            max_digits=3, 
                                            decimal_places=1, 
                                            required=True
    )

    fosforo             = forms.DecimalField(
                                            max_digits=2, 
                                            decimal_places=1, 
                                            required=True
    )

    proteinas_totales   = forms.DecimalField(
                                            max_digits=2, 
                                            decimal_places=1, 
                                            required=True
    )

    albumina            = forms.DecimalField(
                                            max_digits=2, 
                                            decimal_places=1, 
                                            required=True
    )

    colesterol_total    = forms.DecimalField(
                                            max_digits=3, 
                                            decimal_places=1,
                                            required=True
    )

    acido_urico         = forms.DecimalField(
                                            max_digits=2, 
                                            decimal_places=1, 
                                            required=True
    )

    fosfatas_alcalinas  = forms.DecimalField(
                                            max_digits=3, 
                                            decimal_places=1, 
                                            required=True
    )

    bilirrubina_total   = forms.DecimalField(
                                            max_digits=1, 
                                            decimal_places=1,
                                            required=True
    )

    ldh                 = forms.DecimalField(
                                            max_digits=3, 
                                            decimal_places=1, 
                                            required=True, 
                                            label='LDH'
    )

    got_ast             = forms.DecimalField(
                                            max_digits=2, 
                                            decimal_places=1, 
                                            required=True, 
                                            label='GOT/AST'
    )

    creatina            = forms.DecimalField(
                                            max_digits=1,
                                            decimal_places=1, 
                                            required=True
    )

    observaciones       = forms.CharField(
                                            required=True
    )


class PerfilLipidico(forms.Form):
    ''' Formulario Perfil Lipidico '''

    rut                 = CLRutField()
    fecha_ingreso       = forms.DateField()
    colesterol_total    = forms.IntegerField(
                                            required=True,
                                            validators=[
                                                        validators.MinLengthValidator(1, 'rango entre 1 y 200'),
                                                        validators.MaxValueValidator(200), 
                                            ]
    )

    ldl                 = forms.IntegerField(
                                            required=True, 
                                            label='Colesterol LDL',
                                            validators=[
                                                        validators.MinLengthValidator(1),
                                                        validators.MaxValueValidator(100), 
                                            ]
    )

    hdl                 = forms.IntegerField(
                                            required=True, 
                                            label='Colesterol HDL',
                                            validators=[
                                                        validators.MinLengthValidator(40),
                                                        validators.MaxValueValidator(60), 
                                            ]
    )

    vldl                = forms.IntegerField(
                                            required=True, 
                                            label='Colesterol VLDL',
                                            validators=[
                                                        validators.MinLengthValidator(2),
                                                        validators.MaxValueValidator(30), 
                                            ] 
    )

    trigleceridos       = forms.IntegerField(
                                            required=True,
                                            validators=[
                                                        validators.MinLengthValidator(1),
                                                        validators.MaxValueValidator(150), 
                                            ]
    )

    observaciones       = forms.CharField(
                                            required=True
    )

class Orina(forms.Form):
    ''' Formulario Orina'''

    estado =    (
                ('Positivo', 'Positivo'), 
                ('Negativo', 'Negativo')
                )


    rut                 = CLRutField()
    fecha_ingreso       = forms.DateField(
                                            required=True
    )

    color               = forms.CharField(
                                            required=True
    )

    densidad            = forms.DecimalField(
                                            min_value=1,
                                            decimal_places=3,
                                            required=True
    )

    ph                  = forms.DecimalField(
                                            min_value=1,
                                            decimal_places=1,
                                            required=True
    )

    glucosa             = forms.IntegerField(
                                            required=True,
                                            validators=[
                                                        validators.MinLengthValidator(1),
                                                        validators.MaxValueValidator(20), 
                                            ]
    )

    cetonas             = forms.ChoiceField(
                                            choices=(estado)
    )

    Urobilinogeno       = forms.DecimalField(
                                            max_digits=1, 
                                            decimal_places=1, 
                                            required=True
    )

    bilirrubina         = forms.DecimalField(
                                            max_digits=1, 
                                            decimal_places=1, 
                                            required=True
    )

    observaciones       = forms.CharField(
                                            required=True
    )

class Coagulacion(forms.Form):
    ''' Formulario Coagulacion '''

    rut                 = CLRutField()
    fecha_ingreso       = forms.DateField()
    tiempo_protrombina  = forms.IntegerField(
                                            required=True,
                                            validators=[
                                                        validators.MinLengthValidator(12),
                                                        validators.MaxValueValidator(14), 
                                            ]

    )

    protombina       = forms.IntegerField(
                                            required=True,
                                            label='% Protombina',
                                            validators=[
                                                        validators.MinLengthValidator(35),
                                                        validators.MaxValueValidator(45), 
                                            ] 

    )

    observaciones       = forms.CharField(
                                            required=True
    )


class Glicemia(forms.Form):
    ''' Formulario Glicemia '''

    rut                 = CLRutField()
    fecha_ingreso       = forms.DateField()
    glicemia_basal      = forms.IntegerField(
                                            required=True,
                                            validators=[
                                                        validators.MinLengthValidator(60),
                                                        validators.MaxValueValidator(100), 
                                            ]

    )

    glicemia_120min     = forms.IntegerField(
                                            required=True,
                                            validators=[
                                                        validators.MinLengthValidator(60),
                                                        validators.MaxValueValidator(140), 
                                            ] 

    )

    observaciones       = forms.CharField(
                                            required=True
    )


class Electrocardiograma(forms.Form):
    ''' Formulario Electrocardiograma '''

    rut                 = CLRutField()
    fecha_ingreso       = forms.DateField()
    ritmo               = forms.CharField(
                                            required=True
    )

    conduccion_AV       = forms.DecimalField(
                                            max_digits=1, 
                                            decimal_places=2, 
                                            required=True
    )

    conduccion_IV       = forms.DecimalField(
                                            max_digits=1, 
                                            decimal_places=2, 
                                            required=True
    )

    frecuencia          = forms.IntegerField(
                                            required=True,
                                            validators=[
                                                        validators.MinLengthValidator(10),
                                                        validators.MaxValueValidator(100), 
                                            ] 

    )

    eje_electrico       = forms.IntegerField(
                                            required=True,
                                            validators=[
                                                        validators.MinLengthValidator(10),
                                                        validators.MaxValueValidator(100), 
                                            ]

    )

    otros               = forms.IntegerField(
                                            required=True,
                                            validators=[
                                                        validators.MinLengthValidator(1),
                                                        validators.MaxValueValidator(100), 
                                            ]

    )

    observaciones       = forms.CharField(
                                            required=True
    )