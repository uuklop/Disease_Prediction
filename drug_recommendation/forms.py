from django import forms
from .models import PatientDetails

class PatientForm(forms.ModelForm):
    class Meta:
        model = PatientDetails
        fields = ['gender', 'age', 'disease']
