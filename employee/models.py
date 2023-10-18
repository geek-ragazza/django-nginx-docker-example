from django.contrib.auth.models import User
from django.db import models


class Employee(models.Model):
    class EmployeeStatus(models.IntegerChoices):
        EMPLOYEE = 1, "Employee"
        WORKER = 2, "Worker"
        SELF_EMPLOYED = 3, "Self-employed"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    is_employee = models.BooleanField(
        verbose_name="Is Employee", default=False, editable=True
    )
    status = models.IntegerField(
        choices=EmployeeStatus.choices, default=None, null=True, blank=True
    )
    create_dt = models.DateTimeField(auto_now_add=True)
    update_dt = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"
        db_table = "employee"
