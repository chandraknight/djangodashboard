from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, LoginForm
from .models import MyUser
from django.views.generic import CreateView, FormView



class register_view(CreateView):
    form_class= UserRegistrationForm
    template_name= 'register.html'
    success_url='/login/'



# User Registration View
class LoginView( FormView):
    form_class = LoginForm
    
    success_url = 'dashboard.html'
    template_name = 'loginpage.html'

    
    def form_valid(self, form):
        request=self.request
        
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
                #   Redirect to dashboard after login
            if user.role == MyUser.Role.ADMIN:
                return render(request, 'admin_dashboard.html')
            elif user.role == MyUser.Role.DOCTOR:
                return render(request, 'dashboard.html')
            elif user.role == MyUser.Role.PATIENT:
                return render(request, 'student_dashboard.html')
            else:
                return render(request, 'dashboard.html')
               
        else:
            return render(request, 'loginpage.html', {'form': form, 'error': 'Invalid credentials'})








