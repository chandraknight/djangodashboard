


from django.apps import AppConfig

class PatientAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'patient'

    def ready(self):
        import patient.signals  
