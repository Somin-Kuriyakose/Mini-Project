from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Auth
    path("signup/", views.signup, name="signup"),
    path("login/", auth_views.LoginView.as_view(template_name="users/login.html", redirect_authenticated_user=True), name="login"),
    path("logout/",views.custom_logout, name="logout"),

    # Profile
    path("profile/", views.view_profile, name="view_profile"),
    path("profile/edit/", views.edit_profile, name="edit_profile"),

    # Goals
    path("goal/", views.my_goal, name="my_goal"),
    path("goal/set/<int:career_id>/", views.set_goal, name="set_goal"),
    path("goal/update/<int:goal_id>/", views.update_goal_progress, name="update_goal_progress"),

    # Privacy & Security
    path("password/change/", auth_views.PasswordChangeView.as_view(template_name="users/change_password.html"), name="password_change"),
    path("password/change/done/", auth_views.PasswordChangeDoneView.as_view(template_name="users/change_password_done.html"), name="password_change_done"),
    path("delete/", views.delete_account, name="delete_account"),
]
