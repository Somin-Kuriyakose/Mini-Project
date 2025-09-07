from .models import IQCategory

def categorize_iq(score):
    if score >= 80:
        return "High"
    elif score >= 50:
        return "Average"
    else:
        return "Low"

