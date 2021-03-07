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

# initial connection to database
from django.db.backends.signals import connection_created
from django.contrib import messages

@receiver(user_logged_out, sender=User)
def logout_success(sender, request, **kwargs):
    messages.warning(request, 'You Are Logout')


@receiver(user_logged_in, sender=User)
def login_success(sender, request, **kwargs):
    messages.warning(request, 'You Are Login')


@receiver(user_login_failed)
def log_fail(sender, credentials,  request, **kwargs):
    messages.error(request, 'Login Failed')