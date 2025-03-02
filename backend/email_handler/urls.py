from django.urls import path
from email_handler.views import google_login

urlpatterns = [
    path("api/auth/google/", google_login, name="google_login"),
]