from django.core.management.base import BaseCommand
from analytics.models import PollutionData  # Use absolute import here
from analytics.api import fetch_aqi  # Use absolute import here


class Command(BaseCommand):
    help = "Fetch AQI data and update the database"
    
    def handle(self, *args, **kwargs):
        loca = [
            'delhi','chennai','bangalore',
            'mumbai', 'pune', 'kolkata', 'hyderabad', 'ahmedabad',
            'jaipur', 'lucknow', 'chandigarh', 'nagpur'
        ]
        
        for city in loca:
            # Fetch AQI data using the fetch_aqi function
            data = fetch_aqi(city, '38abf87b6de4a7b5cdfa52f63ceea66fdd910103')  # Replace with your actual API key
            
            if data:
                try:
                    # If data is fetched successfully, store it in the database
                    PollutionData.objects.create(
                        location=city,
                        aqi=data['data']['aqi'],
                        pollutants=data['data']['iaqi'],  # You can modify this based on the structure of the response
                        lat = data['data']['city']['geo'][0],  # Latitude
                        lng = data['data']['city']['geo'][1],  # Longitude

                    )
                    self.stdout.write(self.style.SUCCESS(f"Successfully updated AQI for {city}"))
                except Exception as e:
                     self.stdout.write(self.style.ERROR(f"Error processing {city}: {e}. Data: {data}"))
            else:
                self.stdout.write(self.style.ERROR(f"Failed to fetch AQI data for {city}"))
