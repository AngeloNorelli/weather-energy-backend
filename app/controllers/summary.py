import numpy as np
from fastapi import APIRouter, Query
from app.services.weather_services import fetch_weather_summary
from app.utils.validators import validate_coordinates

router = APIRouter()

@router.get("/weather/summary")
def get_weather_forecast(latitude: float = Query(...), longitude: float = Query(...)):
    validate_coordinates(latitude, longitude)
    weather_data = fetch_weather_summary(latitude, longitude)

    rainy_days = sum(1 for rain in weather_data['daily']['precipitation_sum'] if rain > 0)
    
    
    summary = [{
        "average_pressure": np.mean(weather_data['hourly']['pressure_msl']),
        "average_sunshine": np.mean(weather_data['daily']['sunshine_duration']) / 3600,
        "temperature_min": min(weather_data['daily']['temperature_2m_min']),
        "temperature_max": min(weather_data['daily']['temperature_2m_max']),
        "summary": "Tydzień z opadami" if rainy_days > 3 else "Tydzień bez opadów"
    }]
    
    return summary