from django.urls import path
from doctor import views


urlpatterns=[
            
            path('dashboard/', views.doctordashboard_search, name='doctordashboard')]

