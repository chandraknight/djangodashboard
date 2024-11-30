from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, LoginForm
from .models import MyUser, Student, Teacher

# User Registration View
def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Don't save to Database as password need to be hashed
            user.set_password(form.cleaned_data['password'])  # Hash password for
            user.save()  # Save the user
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})



def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                  # Redirect to dashboard after login
                if request.user.role == MyUser.Role.ADMIN:
                    return render(request, 'admin_dashboard.html')
                elif request.user.role == MyUser.Role.TEACHER:
                    return render(request, 'teacher_dashboard.html')
                elif request.user.role == MyUser.Role.STUDENT:
                    return render(request, 'student_dashboard.html')
                else:
                    return render(request, 'dashboard.html')
               
            else:
                return render(request, 'login.html', {'form': form, 'error': 'Invalid credentials'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})



def logout_user(request):
    logout(request)
    return redirect('login')



# @login_required
# def dashboard(request):
#     if request.user.role == MyUser.Role.ADMIN:
#         return render(request, 'admin_dashboard.html')
#     elif request.user.role == MyUser.Role.TEACHER:
#         return render(request, 'teacher_dashboard.html')
#     elif request.user.role == MyUser.Role.STUDENT:
#         return render(request, 'student_dashboard.html')
#     else:
#         return render(request, 'dashboard.html')
