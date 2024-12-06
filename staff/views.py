from django.shortcuts import render, redirect
from django.views import View
from userauth.models import MyUser
from appointment.models import Appointment



class StaffDashboard(View):
    template_name = 'staff/staff_dashboard.html'

    def get(self, request):
        # Restrict non-admin users
        if request.user.role != MyUser.Role.ADMIN:
            return redirect('staffdashboardhome')
        
        # Fetch appointments, patients, and doctors
        appointments = Appointment.objects.all()
        patients = MyUser.objects.filter(role=MyUser.Role.PATIENT)
        doctors = MyUser.objects.filter(role=MyUser.Role.DOCTOR)
        
        # Render the template with the context
        return render(request, self.template_name, {
            'appointments': appointments,
            'patients': patients,
            'doctors': doctors
        })
