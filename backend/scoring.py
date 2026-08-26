def calculate_risk(flags: list, ml_scam_probability: float = 0.0) -> dict:
    """
    Combines rule-based flag points with the ML model's scam probability
    to produce a final risk score + level.
    """
    rule_points = sum(flag["points"] for flag in flags)

    # ML contributes up to 30 points, scaled by its confidence
    ml_points = ml_scam_probability * 30

    total_points = rule_points + ml_points
    score = min(round(total_points), 100)  # cap at 100

    if score <= 20:
        level = "Low"
    elif score <= 50:
        level = "Medium"
    else:
        level = "High"

    return {
        "score": score,
        "level": level
    }
