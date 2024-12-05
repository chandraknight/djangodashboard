from django.http import HttpResponseRedirect
from django.urls import reverse
from functools import wraps

def check_role(required_role):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            # Check if the user is authenticated
            if not request.user.is_authenticated:
                return HttpResponseRedirect(reverse('login'))  # Redirect to login if not authenticated
            
            # Check the user's role
            user_role = getattr(request.user, 'role', None)  # Assuming the role is stored in the user model
            if user_role != required_role:
                if user_role== 'patient':
                    return HttpResponseRedirect(reverse('patientdashboard'))  # Redirect to dashboard if role doesn't match
                else:
                    return HttpResponseRedirect(reverse('doctordashboard'))
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
