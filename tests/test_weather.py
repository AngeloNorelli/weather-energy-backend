from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_weather_forecast():
    response = client.get("/weather/forecast?latitude=52.2297&longitude=21.0122&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m")
    assert response.status_code == 200
    assert len(response.json()) == 7