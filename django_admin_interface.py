# pip install django-admin-interface

INSTALLED_APPS = [
    "admin_interface",
    "colorfield",
    ...
]

X_FRAME_OPTIONS = "SAMEORIGIN"
SILENCED_SYSTEM_CHECKS = ["security.W019"]

# python manage.py migrate

# python manage.py collectstatic