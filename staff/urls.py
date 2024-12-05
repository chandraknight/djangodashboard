from django.urls import path
from staff import views

urlpatterns=[path('staff_dashboard_home/', views.staffdashboard, name='staffdashboardhome'),
            path('dashboard_appointment/', views.staff_dashboard, name='dashboardappointment'),]
            


