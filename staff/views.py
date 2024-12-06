from django.shortcuts import render, redirect



def staffdashboard(request):
    return render(request, 'staff/staff_dashboard.html')