from django.urls import path
from userauth import views
from userauth.views import register_view, LoginView, LogoutView

urlpatterns = [path('register/', register_view.as_view(), name='register'),
               path('', LoginView.as_view(), name='login'),
               path("logout/", LogoutView.as_view(), name="logout"),
            
     ]