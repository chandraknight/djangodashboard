from django.urls import path
from doctor import views
from doctor.views import DoctorProfileView, DoctorsAppointment

urlpatterns=[path('dashboard/', views.doctordashboard_search, name='doctordashboard'),
             path('doctorprofile/', DoctorProfileView.as_view(), name='doctorprofile'),
             path('doctor_appointment/', DoctorsAppointment.as_view(), name='doctorappointment')]

