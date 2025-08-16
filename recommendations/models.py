from django.db import models
from assessments.models import IQCategory
from careers.models import Career, Interest

class RecommendationRule(models.Model):
    """
    Rule-based mapping: if user's IQ category >= min_iq AND (has any of linked interests),
    recommend the associated career.
    """
    career = models.ForeignKey(Career, on_delete=models.CASCADE, related_name="rules")
    min_iq = models.CharField(max_length=10, choices=IQCategory.choices)
    interests = models.ManyToManyField(Interest, blank=True)

    is_active = models.BooleanField(default=True)
    notes = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.career.title} >= {self.min_iq}"
