from django.contrib.auth.models import User
from django.db import models


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    create_dt = models.DateTimeField(auto_now_add=True)
    update_dt = models.DateTimeField(auto_now=True)
    is_employee = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"
        db_table = "employee"
        permissions = [
            ("is_employee", "Is Employee"),
        ]
