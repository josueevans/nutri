from django import forms
from ..models import Dietas, Platillos

class DietasForm(forms.ModelForm):

    id_platillo = forms.ModelChoiceField(queryset=Platillos.objects.all())

    class Meta:
        model = Dietas
        fields = '__all__'
    