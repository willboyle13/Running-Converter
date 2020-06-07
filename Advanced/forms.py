from django import forms
from .models import AdvancedCalc

class CalculatorForm(forms.ModelForm):
    class Meta:
        model = AdvancedCalc 
        fields = [
            'eventconv',
            'time'
        ]