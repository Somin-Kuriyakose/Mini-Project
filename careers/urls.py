from django.urls import path
from . import views

urlpatterns = [
    path("bookmarks/", views.bookmarked_careers, name="bookmarked_careers"),
    # path("bookmark/add/<int:career_id>/", views.add_bookmark, name="add_bookmark"),
    path("bookmark/remove/<int:bookmark_id>/", views.remove_bookmark, name="remove_bookmark"),
    path("recommendations/", views.career_recommendations, name="career_recommendations"),
    path("bookmark/<int:career_id>/", views.bookmark_career, name="bookmark_career"),
    # path("bookmarks/", views.my_bookmarks, name="my_bookmarks"),
]
