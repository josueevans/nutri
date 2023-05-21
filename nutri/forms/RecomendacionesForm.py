from django import forms
from ..models import Usuarios, Dietas, Recomendaciones

class RecomendacionesForm(forms.ModelForm):

    id_usuario = forms.ModelChoiceField(queryset=Usuarios.objects.all())
    id_dieta = forms.ModelChoiceField(queryset=Dietas.objects.all())

    class Meta:
        model = Recomendaciones
        fields = '__all__'