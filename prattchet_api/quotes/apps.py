"""Приложение quotes."""
from django.apps import AppConfig


class QuotesConfig(AppConfig):
    """Регистрация приложения quotes."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'quotes'
