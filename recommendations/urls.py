from django.urls import path
from . import views

urlpatterns = [
    path("", views.recommended_careers, name="recommended_careers"),
]
