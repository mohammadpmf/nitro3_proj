from django.apps import AppConfig


class MyapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapi'

    def ready(self) -> None:
        from . import signals