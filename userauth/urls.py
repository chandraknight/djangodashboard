from django.urls import path
from userauth import views
from userauth.views import register_view, LoginView

urlpatterns = [path('register/', register_view.as_view(), name='register'),
               path('login/', LoginView.as_view(), name='login'),
            
     ]