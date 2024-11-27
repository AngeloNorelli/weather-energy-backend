from fastapi import APIRouter, Query
from app.services.weather_services import fetch_weather_data
from app.utils.validators import validate_coordinates

router = APIRouter()

@router.get("/weather/summary")
def get_weekly_summary(latitude: float = Query(...), longitude:float = Query(...)):
    validate_coordinates(latitude, longitude)
    weather_data = fetch_weather_data(latitude, longitude)
    
    daily = weather_data["daily"]
    avg_pressure = sum(daily["pressure_mean_sea_level"]) / len(daily["pressure_mean_sea_level"])
    avg_sunshine = sum(daily["sunshine_duration"]) / (7 * 60)
    temp_min = min(daily["temperature_2m_min"])
    temp_max = max(daily["temperature_2m_max"])
    precipitation_days = sum(1 for p in daily["precipitation_sum"] if p > 0)
    
    return {
        "average_pressure": avg_pressure,
        "average_sunshine_hours": avg_sunshine,
        "temperature_range": {"min": temp_min, "max": temp_max},
        "summary": "with precipitation" if precipitation_days >= 4 else "without precipitation"
    }