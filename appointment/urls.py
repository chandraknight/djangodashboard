from django.urls import path
from appointment.views import PatientAppointmentView

urlpatterns=[path('patient_appointment/', PatientAppointmentView.as_view(), name='patientappointment')]