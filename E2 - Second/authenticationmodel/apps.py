from django.apps import AppConfig


class AuthenticationmodelConfig(AppConfig):
    name = 'authenticationmodel'
    def ready(self):
        import authenticationmodel.signals