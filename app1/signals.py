import requests
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from .models import UserActivityLog
from django.utils import timezone
from datetime import timedelta

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if ip:
        ip = ip.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    location = "Unknown"
    if ip and ip != '127.0.0.1' and ip != 'localhost':
        try:
            response = requests.get(f"https://ipapi.co/{ip}/json/", timeout=3)
            if response.status_code == 200:
                data = response.json()
                city = data.get("city")
                country = data.get("country_name")
                if city and country:
                    location = f"{city}, {country}"
        except:
            pass
    recent_time = timezone.now() - timedelta(seconds=5)
    existing_log = UserActivityLog.objects.filter(user=user, timestamp__gte=recent_time).exists()
    if not existing_log:
        UserActivityLog.objects.create(
            user=user, 
            action='Logged into the account', 
            ip_address=ip,
            location=location
        )