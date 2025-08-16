from django.contrib import admin
from .models import Question, Choice, TestAttempt, Answer

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "text", "is_active", "topic")
    list_filter = ("is_active", "topic")
    search_fields = ("text",)
    inlines = [ChoiceInline]

@admin.register(TestAttempt)
class TestAttemptAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "started_at", "submitted_at", "total_score", "iq_category")
    list_filter = ("iq_category",)

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("attempt", "question", "choice", "score")
