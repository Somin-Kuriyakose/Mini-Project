from django.contrib import admin
from .models import Profile, CareerGoal, Skill

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "age", "education_level", "last_iq_category")
    search_fields = ("user__username", "education_level")

@admin.register(CareerGoal)
class CareerGoalAdmin(admin.ModelAdmin):
    list_display = ("user", "target_career", "progress", "created_at")
    list_filter = ("progress",)
