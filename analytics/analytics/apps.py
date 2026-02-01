from django.apps import AppConfig
from django.core.management import call_command

class AnalyticsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'analytics'
    
    def ready(self):
        try:
            call_command('update_aqi')
        except Exception as e:
            print(f"Error running update_aqi {e}")
