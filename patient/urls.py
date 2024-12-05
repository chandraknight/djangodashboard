from django.urls import path
from patient import views

urlpatterns = [path('updateprofile/', views.update_profile, name='update_profile'),
               path('patient_dashboard/', views.patientdashboard, name='patientdashboard')
               ]
