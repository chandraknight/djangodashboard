from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .forms import UserRegistrationForm, LoginForm
from .models import MyUser
from django.views.generic import CreateView, FormView

from django.contrib.auth import logout
from django.views.generic import View

class register_view(CreateView):
    form_class= UserRegistrationForm
    template_name= 'userauth/register.html'
    success_url='/login/'



# User Registration View
class LoginView(FormView):
    form_class = LoginForm
    
    
    template_name = 'userauth/loginpage.html'

    
    def form_valid(self, form):
        request=self.request
        
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
                #   Redirect to dashboard after login
            if user.role == MyUser.Role.ADMIN:
                return redirect('staffdashboardhome')
            elif user.role == MyUser.Role.DOCTOR:
                return redirect('doctordashboard')
            elif user.role == MyUser.Role.PATIENT:
                return redirect('patientdashboard')
            else:
                return redirect('patientdashboard')
            
               
        else:
            return render(request, 'userauth/loginpage.html', {'form': form, 'error': 'Invalid credentials'})


# Option 1: Basic Class-Based Logout View
class LogoutView(View):
    """
    Simple logout view that logs out the user and redirects to login page.
    """

    def get(self, request):
        logout(request)
        return redirect('login')









