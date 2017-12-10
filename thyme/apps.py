from django.apps import AppConfig


class ThymeConfig(AppConfig):
    name = 'thyme'

    def ready(self):
        from thyme import signals
