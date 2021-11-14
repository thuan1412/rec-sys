from django.apps import AppConfig


class RecsysConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'recsys'

    def ready(self):
        print("server stask")
        from .tasks import retrain_model
        retrain_model()
