from django.db.models.signals import post_save
from django.dispatch import receiver
from doctor.models import DoctorProfile

@receiver(post_save, sender=DoctorProfile)   #receiver function trigger after the post gets send
def set_patient_id(sender, instance, created, **kwargs):
    if created and not instance.doctor_id:       #checked instance of patient id
        instance.doctor_id = 9000 + instance.id  # Start from 9001
        instance.save()
