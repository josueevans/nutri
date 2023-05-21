from django import forms
from ..models import Dietas, Platillos, DietasPlatillos

class DietasPlatillosForm(forms.ModelForm):

    id_platillo = forms.ModelChoiceField(queryset=Platillos.objects.all())
    id_dieta = forms.ModelChoiceField(queryset=Dietas.objects.all())

    class Meta:
        model = DietasPlatillos
        fields = '__all__'
    