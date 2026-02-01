from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import PollutionData
from .serializer import PollutionDataSerializer

# Create your views here.
def dashboard(request,city):
    return render(request, 'dashboard.html', {'city': city})

def base(request):
    return render(request, 'base.html')

class PollutionDataAPIView(APIView):
    def get(self, request, city):
        # Fetch fresh data from external API
        from .api import fetch_aqi
        # API Token from update_aqi.py
        token = '38abf87b6de4a7b5cdfa52f63ceea66fdd910103' 
        
        try:
            external_data = fetch_aqi(city, token)
            if external_data and external_data.get('status') == 'ok':
                data_point = external_data['data']
                
                # Add "Live Sensor Noise" to simulate real-time fluctuations
                # The external API updates hourly, but we want to show liveliness
                import random
                noise = random.randint(-3, 3) 
                
                # Jitter for pollutants
                pollutants = data_point.get('iaqi', {})
                for key, val in pollutants.items():
                    if isinstance(val, dict) and 'v' in val:
                         # Add +/- 0.5 to 2.5 random noise to pollutant values
                        pollutants[key]['v'] = round(val['v'] + random.uniform(-1.5, 1.5), 1)

                PollutionData.objects.create(
                    location=city,
                    aqi=int(data_point['aqi']) + noise,
                    pollutants=pollutants,
                    lat=data_point['city']['geo'][0],
                    lng=data_point['city']['geo'][1],
                )
        except Exception as e:
            print(f"Error fetching/saving external data: {e}")

        # Return the latest 2000 records (approx 2.5-3 hours of 5s data)
        data = PollutionData.objects.filter(location=city).order_by('-timestamp')[:2000]
        serializer = PollutionDataSerializer(data, many=True)
        return Response(serializer.data)
    
def map(request):
    return render(request,'map.html')