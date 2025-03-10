from django.urls import path
from userauth import views
from userauth.views import register_view, LoginView, LogoutView, home

urlpatterns = [path('register/', register_view.as_view(), name='register'),
               path('login/', LoginView.as_view(), name='login'),
               path("logout/", LogoutView.as_view(), name="logout"),
               path('', views.home, name='home')
     ]