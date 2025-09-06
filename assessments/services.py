from .models import IQCategory

def categorize_iq(score: int) -> str:
    """Return IQ category based on score."""
    if score < 40:
        return IQCategory.LOW
    elif score <= 70:
        return IQCategory.AVERAGE
    return IQCategory.HIGH
