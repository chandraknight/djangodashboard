from django.db import models
from userauth.models import MyUser


class DoctorProfile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, unique=True)
    doctor_id = models.AutoField(primary_key=True)  # Auto-generate unique IDs
    phone_number = models.CharField(
        max_length=15,
    )
    NMC_registered_number = models.CharField(max_length=50, unique=True)
    address = models.TextField()
    specialization = models.CharField(max_length=100, null=True, blank=True)
    availability_status = models.BooleanField(default=True)  # True for available, False for not

    def __str__(self):
        return f"Dr. {self.user.username} ({self.user.email})"