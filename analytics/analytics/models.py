from django.db import models

# Create your models here.

class PollutionData(models.Model):
    location = models.CharField(max_length=255)
    aqi = models.IntegerField()
    pollutants = models.JSONField()
    timestamp = models.DateTimeField(auto_now_add=True)
    lat = models.FloatField()  
    lng = models.FloatField()
    
    def __str__(self) -> str:
        return f"{self.location}"
    
class VehicalData(models.Model):
    location = models.CharField(max_length=255)
    vehical_counts = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)