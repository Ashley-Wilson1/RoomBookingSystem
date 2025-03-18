# roomBooking/signals.py
from django.apps import apps
from django.conf import settings
from allauth.account.forms import SignupForm
from .custom_forms import get_signup_form
from django.db.models.signals import AppConfigReady
from django.dispatch import receiver

@receiver(AppConfigReady)
def set_signup_form(sender, **kwargs):
    settings.ACCOUNT_SIGNUP_FORM_CLASS = get_signup_form()
