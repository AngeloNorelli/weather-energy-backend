import requests
from app.config import OPEN_METEO_API_URL
from app.utils.error_handler import handle_api_error

def fetch_weather_data(latitude: float, longitude: float):
    params = {
        'latitude': latitude,
        'longitude': longitude,
        'daily': 'weather_code,temperature_2m_min,temperature_2m_max,sunshine_duration',
        'forecast_days': 7,
        'timezone': 'auto'
    }
    
    response = requests.get(OPEN_METEO_API_URL, params=params)
    handle_api_error(response)
    
    return response.json()

def fetch_weather_summary(latitude: float, longitude: float):
    params = {
        'latitude': latitude,
        'longitude': longitude,
        'daily': 'temperature_2m_min,temperature_2m_max,sunshine_duration,precipitation_sum',
        'hourly': 'pressure_msl',
        'forecast_days': 7,
        'timezone': 'auto'
    }
    
    response = requests.get(OPEN_METEO_API_URL, params=params)
    handle_api_error(response)
    
    return response.json()