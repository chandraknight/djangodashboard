from django.shortcuts import render
from .forms import Patient_Search_form
from patient.models import PatientProfile
# from common.decorators import check_role


    
# @check_role('doctor')
def doctordashboard_search(request):
    patient_data = None
    error_message = None

    if request.method == "POST":
        form = Patient_Search_form(request.POST)
        if form.is_valid():
            patient_id = form.cleaned_data['patient_unique_id']
            try:
                # Fetch patient details using the Patient_id field
                patient_data = PatientProfile.objects.get(Patient_id=patient_id)
            except PatientProfile.DoesNotExist:
                error_message = f"No patient found with ID: {patient_id}"
    else:
        form = Patient_Search_form()

    return render(request, 'doctor/doctor_dashboard.html', {
        'form_search': form,
        'patient_data': patient_data,
        'error_message': error_message,
    })
    
