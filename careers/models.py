from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Interest(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name


class Career(models.Model):
    class Category(models.TextChoices):
        ACADEMIC = "ACADEMIC", "Academic"
        TECHNICAL = "TECHNICAL", "Technical"
        VOCATIONAL = "VOCATIONAL", "Vocational"
        CREATIVE = "CREATIVE", "Creative"

    title = models.CharField(max_length=200, unique=True)
    category = models.CharField(max_length=20, choices=Category.choices)
    description = models.TextField()
    skills_required = models.TextField(blank=True)
    education_pathway = models.TextField(blank=True)
    salary_min = models.PositiveIntegerField(null=True, blank=True)
    salary_max = models.PositiveIntegerField(null=True, blank=True)
    interests = models.ManyToManyField(Interest, related_name="careers", blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class CareerBookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookmarks")
    career = models.ForeignKey(Career, on_delete=models.CASCADE, related_name="bookmarked_by")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "career")
        verbose_name = "Career Bookmark"
        verbose_name_plural = "Career Bookmarks"

    def __str__(self):
        return f"{self.user.username} → {self.career.title}"
