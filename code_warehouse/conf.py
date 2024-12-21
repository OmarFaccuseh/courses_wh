import os

def get_settings():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'code_warehouse.settings')
    from django.conf import settings
    return settings
