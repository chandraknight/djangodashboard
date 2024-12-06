from django.shortcuts import render, redirect
from doctor.forms import Patient_Search_form, DoctorProfileForm
from patient.models import PatientProfile
from doctor.models import DoctorProfile
# from common.decorators import check_role
from django.views import View
from django.views.generic import FormView
from django.http import HttpResponseForbidden
from userauth.models import MyUser

    
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
    

class DoctorProfileView(FormView):
    template_name = 'doctor/doctor_profile.html'
    form_class=DoctorProfileForm
    def get(self, request, *args, **kwargs):
        # Check if the user is a doctor
        if request.user.role != MyUser.Role.DOCTOR:
        
            return HttpResponseForbidden("You are not authorized to access this page.")

        # Prefill the form with existing profile data if available
        doctor_profile = DoctorProfile.objects.filter(user=request.user).first()
        form = self.form_class(instance=doctor_profile)
        return render(request, 'doctor/doctor_profile.html', {'form': form})

    def post(self, request, *args, **kwargs):
        # Check if the user is a doctor
        if request.user.role != MyUser.Role.DOCTOR:
        
            return HttpResponseForbidden("You are not authorized to access this page.")

        # Process the form submission
        doctor_profile = DoctorProfile.objects.filter(user=request.user).first()
        form = self.form_class(request.POST, instance=doctor_profile)

        if form.is_valid():
            # Save the form data to the database
            doctor_profile = form.save(commit=False)
            doctor_profile.user = request.user
            doctor_profile.save()
            return redirect('doctordashboard')  

        return render(request, 'doctor/doctor_profile.html', {'form': form})
    
