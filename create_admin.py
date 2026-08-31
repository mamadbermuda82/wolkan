import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

username = os.environ.get("ADMIN_USERNAME")
password = os.environ.get("ADMIN_PASSWORD")

if username and password and not User.objects.filter(username=username).exists():
    User.objects.create_superuser(
        username=username,
        password=password
    )
    print("Admin created!")
else:
    print("Admin already exists or variables are missing.")
