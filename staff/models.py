from django.db import models
from django.conf import settings
from userauth.models import MyUser

class Appointment(models.Model):
    class Status(models.TextChoices):
        PENDING = "Pending", "Pending"
        RESCHEDULED = "Rescheduled", "Rescheduled"
        COMPLETED = "Completed", "Completed"

    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        limit_choices_to={'role': MyUser.Role.PATIENT}, 
        related_name="appointments"
    )
    doctor = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        limit_choices_to={'role': MyUser.Role.DOCTOR}, 
        related_name="assigned_appointments", 
        null=True, 
        blank=True
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        limit_choices_to={'role': MyUser.Role.ADMIN}, 
        related_name="created_appointments"
    )
    symptoms = models.TextField()
    date = models.DateTimeField()
    status = models.CharField(
        max_length=20, 
        choices=Status.choices, 
        default=Status.PENDING
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Appointment for {self.patient.username} with {self.doctor.username if self.doctor else 'Unassigned'}"
