from django.urls import path, reverse_lazy, reverse
from django.contrib.auth.views import  LogoutView, PasswordChangeDoneView, PasswordChangeView
from .custom_clases import CustomLoginView
from .views import register_view, profile_view, edit_profile_view, google_login, login_from_fastapi

app_name = 'auth'

urlpatterns = [
    path("register/", register_view, name="register"),
    path("login/", CustomLoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/", profile_view, name="profile"),
    path("login/google/", google_login, name="google_login"),
    path("login/from_fastapi/", login_from_fastapi, name="login_from_fastapi"),
    path("profile/edit/", edit_profile_view, name="edit_profile"),
    path("password/change/",PasswordChangeView.as_view(
            template_name="users/password_change.html",
            success_url= reverse_lazy("auth:password_change_done")),
            name="password_change"),
    path("password/change/done/",PasswordChangeDoneView.as_view(
            template_name="users/password_change_done.html"),name="password_change_done"
    ),
    #path(
    #    "password/reset/",
    #    PasswordResetView.as_view(
    #        template_name="password/password_reset.html",
    #        email_template_name="password/password_reset_email.txt",
    #        success_url=reverse_lazy("auth:password_reset_done"),
    #    ),
    #    name="password_reset",
    #),
    #path(
    #    "password/reset/done/",
    #    PasswordResetDoneView.as_view(
    #        template_name="password/password_reset_done.html"
    #    ),
    #    name="password_reset_done",
    #),
    #path(
    #    "password/reset/<uidb64>/<token>/",
    #    PasswordResetConfirmView.as_view(
    #        template_name="password/password_reset_confirm.html",
    #        success_url=reverse_lazy("auth:password_reset_complete"),
    #    ),
    #    name="password_reset_confirm",
    #),
    #path(
    #    "password/reset/complete/",
    #    PasswordResetCompleteView.as_view(
    #        template_name="password/password_reset_complete.html"
    #    ),
    #    name="password_reset_complete",
    #),
]