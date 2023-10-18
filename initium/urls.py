from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.views.generic import TemplateView

from .views import CustomLogoutView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', auth_views.LoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path("employee/", include("employee.urls", namespace="employee")),
    path("home/", TemplateView.as_view(template_name="index.html"), name="home"),
]
