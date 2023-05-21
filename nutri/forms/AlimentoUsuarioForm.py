from django import forms
from ..models import Usuarios, Platillos, AlimentoUsuario

class AlimentoUsuarioForm(forms.ModelForm):

    id_usuario = forms.ModelChoiceField(queryset=Usuarios.objects.all())
    id_platillo = forms.ModelChoiceField(queryset=Platillos.objects.all())

    class Meta:
        model = AlimentoUsuario
        fields = '__all__'