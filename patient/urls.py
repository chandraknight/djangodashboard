from django.urls import path
from patient import views

urlpatterns = [path('updateprofile/', views.update_profile, name='update_profile'),
               ]
