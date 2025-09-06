from django.contrib import admin
from .models import Career, Interest, CareerBookmark


@admin.register(Interest)
class InterestAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)


@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "is_active", "salary_min", "salary_max")
    list_filter = ("category", "is_active", "interests")
    search_fields = ("title", "description", "skills_required", "education_pathway")
    filter_horizontal = ("interests",)
    ordering = ("title",)
    fieldsets = (
        (None, {
            "fields": ("title", "category", "description", "is_active")
        }),
        ("Details", {
            "fields": ("skills_required", "education_pathway", "salary_min", "salary_max")
        }),
        ("Interests", {
            "fields": ("interests",)
        }),
    )


@admin.register(CareerBookmark)
class CareerBookmarkAdmin(admin.ModelAdmin):
    list_display = ("user", "career", "created_at")
    search_fields = ("user__username", "career__title")
    list_filter = ("created_at",)
