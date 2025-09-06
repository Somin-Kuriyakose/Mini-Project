from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
    path("assessments/", include("assessments.urls")),
    path("careers/", include("careers.urls")),
    path("recommendations/", include("recommendations.urls")),
    path("admin/reports/", include("admin_reports.urls")),
]
