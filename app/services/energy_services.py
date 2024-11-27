from app.config import MOC_INSTALACJI, EFEKTYWNOSC_PANELI

def calculate_daily_energy(sunshine_hours: float) -> float:
    return MOC_INSTALACJI * sunshine_hours * EFEKTYWNOSC_PANELI