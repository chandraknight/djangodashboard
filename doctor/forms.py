from django import forms


class Patient_Search_form(forms.Form):
    patient_unique_id = forms.IntegerField(required=True)
    