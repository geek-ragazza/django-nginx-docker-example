from django.urls import path

from . import views

app_name = "employee"

urlpatterns = [
    path("register/", views.register_employee, name="register"),
]
