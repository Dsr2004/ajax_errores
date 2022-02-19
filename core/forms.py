from django import forms
from .models import frutas

class frutaForm(forms.ModelForm):
    class Meta:
        model=frutas
        fields="__all__"