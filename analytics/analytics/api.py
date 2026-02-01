import requests

def fetch_aqi(city, api_key):
    url =f"http://api.waqi.info/feed/{city}/?token={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

