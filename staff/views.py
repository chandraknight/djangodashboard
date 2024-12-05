from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Appointment, MyUser

@login_required
def staff_dashboard(request):
    if request.user.role != MyUser.Role.ADMIN:
        return redirect('staffdashboardhome')  # Restrict non-admin users.

    appointments = Appointment.objects.filter(created_by=request.user)

    if request.method == 'POST':
        patient_id = request.POST['patient']
        doctor_id = request.POST.get('doctor')  
        symptoms = request.POST['symptoms']
        date = request.POST['date']

        Appointment.objects.create(
            patient_id=patient_id,
            doctor_id=doctor_id,
            created_by=request.user,
            symptoms=symptoms,
            date=date
        )
        return redirect('dashboardappointment')

    patients = MyUser.objects.filter(role=MyUser.Role.PATIENT)
    doctors = MyUser.objects.filter(role=MyUser.Role.DOCTOR)
    return render(request, 'staff/appointment.html', {
        'appointments': appointments,
        'patients': patients,
        'doctors': doctors
    })


def staffdashboard(request):
    return render(request, 'staff/staff_dashboard.html')