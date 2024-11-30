from fastapi import APIRouter, Query
from app.services.weather_services import fetch_weather_data
from app.services.energy_services import calculate_daily_energy
from app.utils.validators import validate_coordinates

router = APIRouter()

@router.get("/weather/forecast")
def get_weather_forecast(latitude: float = Query(...), longitude: float = Query(...)):
    validate_coordinates(latitude, longitude)
    weather_data = fetch_weather_data(latitude, longitude)
    
    forecast = []
    
    for i in range(7):
        sunshine_hours = weather_data['daily']["sunshine_duration"][i] / 60
        energy = calculate_daily_energy(sunshine_hours)
        
        forecast.append({
            "date": weather_data['daily']["time"][i],
            "weather_code": weather_data['daily']["weather_code"][i],
            "temp_min": weather_data['daily']["temperature_2m_min"][i],
            "temp_max": weather_data['daily']["temperature_2m_max"][i],
            "energy_kwh": energy
        })
    
    return forecast