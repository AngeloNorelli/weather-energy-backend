import requests
from app.config import OPEN_METEO_API_URL
from app.utils.error_handler import handle_api_error

def fetch_weather_data(latitude: float, longitude: float):
    params = {
        'latitude': latitude,
        'longitude': longitude,
        'daily': 'temperature_wm_min,temperature_wm_max,sunshine_duration',
        'timezone': 'auto'
    }
    
    response = requests.get(OPEN_METEO_API_URL, params=params)
    handle_api_error(response)
    
    return response.json()