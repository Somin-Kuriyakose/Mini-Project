from django.db import models
from django.conf import settings

class IQCategory(models.TextChoices):
    LOW = "LOW", "Low"
    AVERAGE = "AVERAGE", "Average"
    HIGH = "HIGH", "High"

class Question(models.Model):
    text = models.TextField()
    is_active = models.BooleanField(default=True)
    # optional tagging for future analytics
    topic = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.text[:60]

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices")
    text = models.CharField(max_length=300)
    score = models.IntegerField(default=0)  # scoring basis for IQ

    def __str__(self):
        return f"{self.question_id} -> {self.text[:40]}"

class TestAttempt(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="test_attempts")
    started_at = models.DateTimeField(auto_now_add=True)
    submitted_at = models.DateTimeField(null=True, blank=True)
    total_score = models.IntegerField(default=0)
    iq_category = models.CharField(max_length=10, choices=IQCategory.choices, blank=True)

class Answer(models.Model):
    attempt = models.ForeignKey(TestAttempt, on_delete=models.CASCADE, related_name="answers")
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    class Meta:
        unique_together = ("attempt", "question")
