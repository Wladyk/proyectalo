from django.apps import AppConfig


class ProyectaloConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'proyectalo'
    def ready(self):
        import proyectalo.signals