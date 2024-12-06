from django import forms
from doctor.models import DoctorProfile

class Patient_Search_form(forms.Form):
    patient_unique_id = forms.IntegerField(required=True)
    
class DoctorProfileForm(forms.ModelForm):
    class Meta:
        model=DoctorProfile
        fields=['phone_number',
            'NMC_registered_number',
            'address',
            'specialization',
            'availability_status',]