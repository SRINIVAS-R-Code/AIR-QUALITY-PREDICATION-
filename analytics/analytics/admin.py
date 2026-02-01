from django.contrib import admin
from .models import PollutionData, VehicalData
# Register your models here.

admin.site.register(PollutionData)
admin.site.register(VehicalData)