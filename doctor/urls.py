from django.urls import path
from doctor import views
from doctor.views import DoctorProfileView

urlpatterns=[path('dashboard/', views.doctordashboard_search, name='doctordashboard'),
             path('doctorprofile/', DoctorProfileView.as_view(), name='doctorprofile')]

