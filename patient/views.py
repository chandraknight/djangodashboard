
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PatientProfileForm
from .models import PatientProfile

@login_required
def update_profile(request):
    # Ensure the patient profile exists for the logged-in user
    try:
        profile = PatientProfile.objects.get(user=request.user)
    except PatientProfile.DoesNotExist:
        # Redirect or handle missing profile case if needed
        profile = PatientProfile(user=request.user)

    if request.method == 'POST':
        form = PatientProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return render(request,'patient_dashboard.html')  
    else:
        form = PatientProfileForm(instance=profile)
    
    return render(request, 'update_profile.html', {'form': form})








