from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.views.generic import TemplateView
from employee.models import Employee
from .views import CustomLogoutView
from employee.admin import custom_admin_site
from django.contrib.auth.models import User


urlpatterns = [
    path("admin/", custom_admin_site.urls),
    path("", auth_views.LoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("employee/", include("employee.urls", namespace="employee")),
    path("home/", TemplateView.as_view(template_name="index.html"), name="home"),
]
