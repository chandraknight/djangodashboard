
from django.views import View
from django.shortcuts import render, redirect
from .models import Appointment, MyUser

class PatientAppointmentView(View):
    template_name = 'appointment/appointment.html'

    def get(self, request):
        # Restrict non-admin users
        if request.user.role != MyUser.Role.ADMIN:
            return redirect('staffdashboardhome')
        
        # Fetch appointments, patients, and doctors
        appointments = Appointment.objects.filter(created_by=request.user)
        patients = MyUser.objects.filter(role=MyUser.Role.PATIENT)
        doctors = MyUser.objects.filter(role=MyUser.Role.DOCTOR)
        
        # Render the template with the context
        return render(request, self.template_name, {
            'appointments': appointments,
            'patients': patients,
            'doctors': doctors
        })

    def post(self, request):
        # Handle appointment creation
        if request.user.role != MyUser.Role.ADMIN:
            return redirect('staffdashboardhome')

        patient_id = request.POST['patient']
        doctor_id = request.POST.get('doctor')  # Doctor is optional
        symptoms = request.POST['symptoms']
        date = request.POST['date']

        # Create the appointment
        Appointment.objects.create(
            patient_id=patient_id,
            doctor_id=doctor_id,
            created_by=request.user,
            symptoms=symptoms,
            date=date
        )

        # Redirect to the same view after creation
        return redirect('patientappointment')
