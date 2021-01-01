from django import forms



class DiagnosticoExamen(forms.Form):
    '''
    Ingresos de diagnósticos y exámenes
    '''
    fecha_ingreso = forms.DateField()
    examen = forms.CharField()
    diagnóstico = forms.CharField()