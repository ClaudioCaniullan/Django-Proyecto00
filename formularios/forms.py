from django import forms
from django.core import validators
from django.core.exceptions import ValidationError


class DiagnosticoExamen(forms.Form):
    '''
    hemograma
    '''
    list_exam = (
                    ('Hemograma', 'Hemograma'), ('Perfil Bioquimico', 'Perfil Bioquimico'),
                    ('Perfil Lipidico', 'Perfil Lipidico'),
                    ('Orina', 'Orina'), ('Coagulación', 'Coagulación'),
                    ('Glicemia', 'Glicemia'), ('Electrocardiograma', 'Electrocardiograma')
                )

    
    select_exam = forms.ChoiceField(label='Tipo examen', choices=list_exam)

    fecha_ingreso = forms.DateField()
    eritrocito = forms.DecimalField(max_digits=3, decimal_places=1, required=True)
    leucocitos = forms.DecimalField(max_digits=3, decimal_places=1, required=True)
    hemoglobina = forms.DecimalField(max_digits=3, decimal_places=1, required=True)
    hematocrito = forms.DecimalField(max_digits=3, decimal_places=1, required=True)
    vcm = forms.DecimalField(label='V.C.M.', max_digits=3, decimal_places=1, required=True)
    chcm = forms.DecimalField(label='C.H.C.M.', max_digits=3, decimal_places=1, required=True)
    plaquetas = forms.DecimalField(max_digits=4, decimal_places=1, required=True)
    diagnostico = forms.CharField(required=True)
