from django.contrib import admin
from .models import RecommendationRule

@admin.register(RecommendationRule)
class RecommendationRuleAdmin(admin.ModelAdmin):
    list_display = ("career", "min_iq", "is_active")
    list_filter = ("min_iq", "is_active")
    search_fields = ("career__title",)
