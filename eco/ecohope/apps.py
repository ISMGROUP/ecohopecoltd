from django.apps import AppConfig

class EcohopeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ecohope'

    def ready(self):
        import ecohope.signals  # Make sure this matches your actual module name
