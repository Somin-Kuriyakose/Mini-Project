from django.contrib import admin
from .models import Interest, Career, CareerBookmark

@admin.register(Interest)
class InterestAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name", "slug")

@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "is_active", "salary_min", "salary_max")
    list_filter = ("category", "is_active")
    search_fields = ("title", "description", "skills_required")

@admin.register(CareerBookmark)
class CareerBookmarkAdmin(admin.ModelAdmin):
    list_display = ("user", "career", "created_at")
    search_fields = ("user__username", "career__title")
