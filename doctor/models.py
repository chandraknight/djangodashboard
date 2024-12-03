from django.db import models
from userauth.models import MyUser
from django.contrib.auth.models import BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
# Proxy models for specific roles
# Extend myuser to impose the role specific behaviour


class DoctorManager(BaseUserManager):
    def get_queryset(self):
        return super().get_queryset().filter(role=MyUser.Role.DOCTOR)

class Doctor(MyUser):
    base_role = MyUser.Role.DOCTOR
    objects = DoctorManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "Welcome, Doctor!"

# Signals to create profiles
# This is to store the addition information
# Signals automatically create profiles when a user with a specific role is created.



#similarly for teachers

class TeacherProfile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    teacher_id = models.IntegerField(null=True, blank=True)

@receiver(post_save, sender=Doctor)
def create_teacher_profile(sender, instance, created, **kwargs):
    if created and instance.role == MyUser.Role.TEACHER:
        TeacherProfile.objects.create(user=instance)