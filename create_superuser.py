import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "roomBooking.settings")  # Replace with your actual project name
django.setup()

User = get_user_model()

username = "admin"
email = "admin@email.com"
password = "admin"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print("Superuser created successfully.")
else:
    print("Superuser already exists.")
