# Login-logoout-loginfailed
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
# pre-init,pre-save,pre-delete,pre-migrate,post-init,post-save,post-delete,post-migrate
from django.db.models.signals import pre_init, pre_save, pre_delete, pre_migrate, post_migrate, post_delete, post_init, post_migrate, post_save
#  request-failed, request-start, request-end
from django.core.signals import request_finished, request_started, got_request_exception
# User import
from django.contrib.auth.models import User
# receiver
from django.dispatch import receiver
from .models import Info
# initial connection to database
from django.db.backends.signals import connection_created

@receiver(user_logged_in, sender=User)
def login_success(sender, request, **kwargs):
    print('-*------------------------------------*- test')
    print('login-success')
    print('sender', sender)
    print('request', request)
    print('user', User)
    print(f'kwargs:{kwargs}')


@receiver(user_logged_out, sender=User)
def logout_success(sender, request, **kwargs):
    print('+++++++++++++++++++++++++++++++++++++++++ test')
    print('logout')
    print('sender', sender)
    print('request', request)
    print('user', User)
    print(f'kwargs:{kwargs}')


@receiver(user_login_failed)
def log_fail(sender, credentials,  request, **kwargs):
    print('?????????????????????????????????????? test')
    print('login failed')
    print('sender', sender)
    print('credentials', credentials)
    print('request', request)
    print('user', User)
    print(f'kwargs:{kwargs}')


@receiver(pre_init, sender=Info)
def pre_init_model(sender, **kwargs):
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! test')
    print('sender', sender)
    print(f'kwargs:{kwargs}')


@receiver(post_init, sender=Info)
def post_init_model(sender, **kwargs):
    print('!-!-!-!-!-!-!-!-!-!!-1-!-!-!-!--!-!-!-!-!-!-!-! test')
    print('sender', sender)
    print(f'kwargs:{kwargs}')


@receiver(pre_save, sender=Info)
def pre_save_model(sender, instance, **kwargs):
    print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< test')
    print('sender', sender)
    print('instance', instance)
    print(f'kwargs:{kwargs}')


@receiver(post_save, sender=Info)
def post_save_model(sender, instance, **kwargs):
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> test')
    print('sender', sender)
    print('instance', instance)
    print(f'kwargs:{kwargs}')


@receiver(pre_delete, sender=Info)
def pre_delete_model(sender, instance, **kwargs):
    print('|||||||||||||||||||||||||||||||||||||||||||||||||||| test')
    print('sender', sender)
    print('instance', instance)
    print(f'kwargs:{kwargs}')


@receiver(post_delete, sender=Info)
def post_delete_model(sender, instance, **kwargs):
    print('\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ +++++-----')
    print('sender', sender)
    print('instance', instance)
    print(f'kwargs:{kwargs}')


@receiver(request_started)
def request_start(sender, environ, **kwargs):
    print('request send')
    print('############################################## test')
    print('environ', environ)
    print(f'kwargs:{kwargs}')


@receiver(request_finished)
def request_end(sender, **kwargs):
    print('request finished')
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ test')
    print(f'kwargs:{kwargs}')


@receiver(got_request_exception)
def request_fail(sender, request, **kwargs):
    print('request failed')
    print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% test')
    print('request failed', request)
    print(f'kwargs:{kwargs}')

@receiver(pre_migrate)
def pre_migration_signal(sender, **kwargs):
    print('pre migrations signals')
    print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ test')
    print(f'kwargs:{kwargs}')


@receiver(post_migrate)
def post_migration_signal(sender, **kwargs):
    print('pre migrations signals')
    print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& test')
    print(f'kwargs:{kwargs}')

@receiver(connection_created)
def connect_database(sender, **kwargs):
    print('connection created')
    print('************************************************************** test')
    print(f'kwargs:{kwargs}')
