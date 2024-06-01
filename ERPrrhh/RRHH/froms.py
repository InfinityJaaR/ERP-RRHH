from django import forms
from .models import Cargo,Area

class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = '__all__'


class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields='__all__'