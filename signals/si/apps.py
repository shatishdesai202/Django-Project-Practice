from django.apps import AppConfig


class SiConfig(AppConfig):
    name = 'si'
    def ready(self):
        import si.signals
