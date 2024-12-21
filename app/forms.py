from django import forms
from .models import Nota

class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ['contenido']
        widgets = {
            'contenido': forms.TextInput(attrs={'class': 'form-control w-full', 'placeholder': 'Escribe una nueva nota'}),
        }
    