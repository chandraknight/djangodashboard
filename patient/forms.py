from django import forms
from patient.models import PatientProfile
class PatientProfileForm(forms.ModelForm):
    class Meta:
        model= PatientProfile
        fields=['phone_number', 'dob', 'address', 'sex', 'blood_group', 'occupation']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }
