from django import forms
from ..models import Platillos

class PlatillosForm(forms.ModelForm):
    class Meta:
        model = Platillos
        fields = '__all__'