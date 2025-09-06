from django.urls import path
from . import views

urlpatterns = [
    path("start/", views.start_test, name="take_test"),
    path("question/<int:attempt_id>/<int:question_index>/", views.show_question, name="show_question"),
    path("submit/<int:attempt_id>/", views.submit_test, name="submit_test"),
]
