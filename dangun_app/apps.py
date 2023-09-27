from django.apps import AppConfig


class DangunAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dangun_app'


    def ready(self):
        import dangun_app.signals