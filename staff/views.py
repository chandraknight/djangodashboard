from django.shortcuts import render, redirect
from django.views import View
from userauth.models import MyUser
from appointment.models import Appointment
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy



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

class UpdateAppointmentView(UpdateView):
    template_name='staff/update_appointment.html'
    model=Appointment
    fields=['patient', 'doctor', 'symptoms', 'date', 'status'] 

    def get_success_url(self):
    
        return reverse_lazy('staffdashboardhome')

class DeleteAppointmenrView(DeleteView):
    template_name='staff/staff_dashboard.html'
    model=Appointment
    success_url = reverse_lazy("staffdashboardhome")