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
    fecha_ingreso       = forms.DateField()
    eritrocito          = forms.DecimalField(max_digits=3, decimal_places=1, required=True)
    leucocitos          = forms.DecimalField(max_digits=3, decimal_places=1, required=True)
    hemoglobina         = forms.DecimalField(max_digits=3, decimal_places=1, required=True)
    hematocrito         = forms.DecimalField(max_digits=3, decimal_places=1, required=True)
    vcm                 = forms.DecimalField(label='V.C.M.', max_digits=3, decimal_places=1, required=True)
    chcm                = forms.DecimalField(label='C.H.C.M.', max_digits=3, decimal_places=1, required=True)
    plaquetas           = forms.DecimalField(max_digits=4, decimal_places=1, required=True)
    diagnostico         = forms.CharField(required=True)


class PerfilBioquimico(forms.Form):
    ''' Formulario Perfil Bioquimico '''
    fecha_ingreso       = forms.DateField()
    glucosa             = forms.DecimalField(max_digits=3, decimal_places=1, required=True)
    nitrogeno_ureico    = forms.DecimalField(max_digits=3, decimal_places=1, required=True)
    calcio              = forms.DecimalField(max_digits=3, decimal_places=1, required=True)
    fosforo             = forms.DecimalField(max_digits=2, decimal_places=1, required=True)
    proteinas_totales   = forms.DecimalField(max_digits=2, decimal_places=1, required=True)
    albumina            = forms.DecimalField(max_digits=2, decimal_places=1, required=True)
    colesterol_total    = forms.DecimalField(max_digits=3 decimal_places=1, required=True)
    acido_urico         = forms.DecimalField(max_digits=2, decimal_places=1, required=True)
    fosfatas_alcalinas  = forms.DecimalField(max_digits=3, decimal_places=1, required=True)
    bilirrubina_total   = forms.DecimalField(max_digits=1, decimal_places=1, required=True)
    ldh                 = forms.DecimalField(max_digits=3, decimal_places=1, required=True, label='LDH')
    got_ast             = forms.DecimalField(max_digits=2, decimal_places=1, required=True, label='GOT/AST')
    creatina            = forms.DecimalField(max_digits=1, decimal_places=1, required=True)
    diagnostico         = forms.CharField(required=True)


class PerfilLipidico(forms.Form):
    ''' Formulario Perfil Lipidico '''
    fecha_ingreso       = forms.DateField()
    colesterol_total    = forms.IntegerField(MinValueValidator=1,  MaxValueValidator=200, required=True)
    ldl                 = forms.IntegerField(MinValueValidator=1,  MaxValueValidator=100, required=True, label='Colesterol LDL')
    hdl                 = forms.IntegerField(MinValueValidator=40,  MaxValueValidator=60, required=True, label='Colesterol HDL')
    vldl                = forms.IntegerField(MinValueValidator=2,  MaxValueValidator=30, required=True, label='Colesterol VLDL')
    trigleceridos       = forms.IntegerField(MinValueValidator=1,  MaxValueValidator=150, required=True)
    diagnostico         = forms.CharField(required=True)

class Orina(forms.Form):
    ''' Formulario Orina'''
    estado =    (
                ('Positivo': 'Positivo'), 
                ('Negativo': 'Negativo')
                )

    fecha_ingreso       = forms.DateField()
    color               = forms.CharField()
    densidad            = forms.DecimalField()
    ph                  = forms.DecimalField()
    glucosa             = forms.IntegerField(MinValueValidator=1, MaxValueValidator=20, required=True)
    cetonas             = forms.ChoiceField(choices=(estado))
    Urobilinogeno       = forms.DecimalField(MaxValueValidator=1, max_digits=1, decimal_places=1, required=True)
    bilirrubina         = forms.ChoiceField(choices=(estado))
    diagnostico         = forms.CharField(required=True)

class Coagulacion(forms.Form):
    ''' Formulario Coagulacion '''
    fecha_ingreso       = forms.DateField()
    tiempo_protrombina = forms.IntegerField(MinValueValidator=12, MaxValueValidator=14, required=True)
    _%_protombina = forms.IntegerField(MinValueValidator=35, MaxValueValidator=45, required=True)
    diagnostico         = forms.CharField(required=True)


class Glicemia(forms.Form):
    ''' Formulario Glicemia '''
    fecha_ingreso       = forms.DateField()
    glicemia_basal      = forms.IntegerField(MinValueValidator=60, MaxValueValidator=100, required=True)
    glicemia_120min     = forms.IntegerField(MinValueValidator=60, MaxValueValidator=140, required=True)
    diagnostico         = forms.CharField(required=True)


class Electrocardiograma(forms.Form):
    ''' Formulario Electrocardiograma '''
    fecha_ingreso       = forms.DateField()
    ritmo               = forms.CharField(required=True)
    conduccion_AV       = forms.DecimalField(max_digits=1, decimal_places=2, required=True)
    conduccion_IV       = forms.DecimalField(max_digits=1, decimal_places=2, required=True)
    frecuencia          = forms.IntegerField(MinValueValidator=10, MaxValueValidator=100, required=True)
    eje_electrico       = forms.IntegerField(MinValueValidator=10, MaxValueValidator=100, required=True)
    otros               = forms.IntegerField(MinValueValidator=1, MaxValueValidator=100, required=True)
    diagnostico         = forms.CharField(required=True)
