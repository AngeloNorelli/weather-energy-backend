from app.services.energy_services import calculate_daily_energy

def test_calculate_daily_energy():
    result = calculate_daily_energy(5)
    assert result == 2.5 * 5 * 0.2