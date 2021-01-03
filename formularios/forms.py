from django import forms
from django.core import validators
from django.core.exceptions import ValidationError



    # list_exam = (
    #                 ('Hemograma', 'Hemograma'), ('Perfil Bioquimico', 'Perfil Bioquimico'),
    #                 ('Perfil Lipidico', 'Perfil Lipidico'),
    #                 ('Orina', 'Orina'), ('Coagulación', 'Coagulación'),
    #                 ('Glicemia', 'Glicemia'), ('Electrocardiograma', 'Electrocardiograma')
    #             )
    # select_exam = forms.ChoiceField(label='Tipo examen', choices=list_exam)

class Hemograma(forms.Form):
    ''' Formulario Hemograma '''

    fecha_ingreso = forms.DateField()
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

    diagnostico         = forms.CharField(
                                            required=True
    )


class PerfilBioquimico(forms.Form):
    ''' Formulario Perfil Bioquimico '''
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

    diagnostico         = forms.CharField(
                                            required=True
    )


class PerfilLipidico(forms.Form):
    ''' Formulario Perfil Lipidico '''
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

    diagnostico         = forms.CharField(
                                            required=True
    )

class Orina(forms.Form):
    ''' Formulario Orina'''
    estado =    (
                ('Positivo', 'Positivo'), 
                ('Negativo', 'Negativo')
                )

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

    bilirrubina         = forms.ChoiceField(
                                            choices=(estado)
    )

    diagnostico         = forms.CharField(
                                            required=True
    )

class Coagulacion(forms.Form):
    ''' Formulario Coagulacion '''
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

    diagnostico         = forms.CharField(
                                            required=True
    )


class Glicemia(forms.Form):
    ''' Formulario Glicemia '''
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

    diagnostico         = forms.CharField(
                                            required=True
    )


class Electrocardiograma(forms.Form):
    ''' Formulario Electrocardiograma '''
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

    diagnostico         = forms.CharField(
                                            required=True
    )
