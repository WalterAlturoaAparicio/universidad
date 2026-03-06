from django.urls import path
from . import views

app_name = "universidad"

urlpatterns = [
    path("", views.home, name="home"),
]

