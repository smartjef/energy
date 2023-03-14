from django import forms
from .models import EnergyConsumption

class EnergyConsumptionForm(forms.ModelForm):
    class Meta:
        model = EnergyConsumption
        fields = ['company', 'amount', 'date']
