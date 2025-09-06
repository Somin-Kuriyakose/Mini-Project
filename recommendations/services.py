from .models import RecommendationRule
from careers.models import Career
from assessments.models import IQCategory

def get_recommended_careers(user):
    """
    Return a queryset of careers recommended for the user
    based on their IQ category and selected interests.
    """
    profile = user.profile
    iq = profile.last_iq_category
    interests = profile.interests.all()

    if not iq:
        return Career.objects.none()  # No test taken yet

    # Find rules where min_iq <= user’s iq
    rules = RecommendationRule.objects.filter(is_active=True)

    # Filter by IQ
    if iq == IQCategory.LOW:
        rules = rules.filter(min_iq=IQCategory.LOW)
    elif iq == IQCategory.AVERAGE:
        rules = rules.filter(min_iq__in=[IQCategory.LOW, IQCategory.AVERAGE])
    elif iq == IQCategory.HIGH:
        rules = rules  # high IQ can see all

    # Match interests (if user selected any)
    if interests.exists():
        rules = rules.filter(interests__in=interests).distinct()

    careers = Career.objects.filter(rules__in=rules, is_active=True).distinct()
    return careers
