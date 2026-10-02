from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserActivityLog
@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
  ip = request.META.get('REMOTE_ADDR') if request else None
  UserActivityLog.objects.create(user=user, action='Logged into the account', ip_address=ip)
@receiver(post_save, sender=User)
def log_user_signup(sender, instance, created, **kwargs):
  if created:
    UserActivityLog.objects.create(
        user=instance,
        action='Account registered successfully',
        ip_address='127.0.0.1',
    )