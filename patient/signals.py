from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PatientProfile

@receiver(post_save, sender=PatientProfile)   #receiver function trigger after the post gets send
def set_patient_id(sender, instance, created, **kwargs):
    if created and not instance.Patient_id:       #checked instance of patient id
        instance.Patient_id = 1000 + instance.id  # Start from 1001
        instance.save()
