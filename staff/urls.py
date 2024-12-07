from django.urls import path
from staff import views
from staff.views import StaffDashboard, UpdateAppointmentView, DeleteAppointmenrView

urlpatterns=[path('staff_dashboard_home/', StaffDashboard.as_view(), name='staffdashboardhome'),
             path('update_appointment/<int:pk>/', UpdateAppointmentView.as_view(), name='updateappointment'),
]
    
            

