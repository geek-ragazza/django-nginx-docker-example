from django.contrib import admin

from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "is_employee",
        "status",
    )
    list_filter = ("is_employee",)
    list_editable = ("is_employee",)
