def compute_stability(temperature: float, vibration: float, load: float) -> float:
    """Simple heuristic stability score 0-100 (higher is better). Tweak weights as needed."""
    # normalize estimates
    temp_score = max(0, 100 - (temperature - 20))  # ideal temp ~20
    vib_score = max(0, 100 - (vibration * 100))   # smaller vibration better
    load_score = max(0, 100 - abs(load - 50))     # ideal load ~50
    stability = (0.4 * temp_score + 0.3 * vib_score + 0.3 * load_score)
    return round(max(0, min(100, stability)), 2)
