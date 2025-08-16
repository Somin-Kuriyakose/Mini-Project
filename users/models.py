from django.db import models
from django.conf import settings
from careers.models import Interest
from assessments.models import IQCategory

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    age = models.PositiveIntegerField(null=True, blank=True)
    education_level = models.CharField(max_length=120, blank=True)
    interests = models.ManyToManyField(Interest, related_name="users", blank=True)
    last_iq_category = models.CharField(max_length=10, choices=IQCategory.choices, blank=True)

    def __str__(self):
        return f"Profile({self.user.username})"

class CareerGoal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="goals")
    target_career = models.ForeignKey("careers.Career", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # simple progress percentage for now
    progress = models.PositiveIntegerField(default=0)  # 0..100

    def __str__(self):
        return f"{self.user.username} -> {self.target_career}"
