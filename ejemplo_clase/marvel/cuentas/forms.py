from django import forms
from .models import PerfilUsuario

class PerfilUsuarioForm(forms.ModelForm):
    class Meta:
        model = PerfilUsuario
        fields = ['pais', 'provincia', 'ciudad', 'codigo_postal', 'telefono']
