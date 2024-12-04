from django.db import models
from userauth.models import MyUser
from django.db.models.signals import post_save
from django.dispatch import receiver

from datetime import date


# Create your models here.
class PatientProfile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    Patient_id = models.IntegerField(unique=True,null=True, blank=True)
    phone_number= models.IntegerField(null=False, blank=False)
    dob= models.DateField(null=False, blank=False)
    address= models.CharField(null=False, blank=False, max_length=100)
    SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    ]
    sex = models.CharField(max_length=1,choices=SEX_CHOICES)
    enroll_date=models.DateTimeField(auto_now_add=True)
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]
    blood_group= models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES)
    age = models.PositiveIntegerField(editable=False)  # Auto-calculated age, not editable directly

    def save(self, *args, **kwargs):
        # Calculate age from dob
        if self.dob:
            today = date.today()
            self.age = today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
        super().save(*args, **kwargs)  # Call the original save method
    occupation= models.CharField(max_length=100, null=True, blank=True)


    

