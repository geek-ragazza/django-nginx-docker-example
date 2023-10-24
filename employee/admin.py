from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from employee.models import Employee
from django.contrib import messages


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "is_employee",
        "status",
    )
    list_filter = ("is_employee",)
    list_editable = ("is_employee",)


admin.site.unregister(Employee)


class CustomAdminSite(admin.AdminSite):
    def login(self, request, extra_context=None):
        response = super().login(request, extra_context)

        if request.user.is_authenticated:
            if not request.user.is_superuser:
                if request.user.has_perm("employee.is_employee"):
                    messages.info(request, "Welcome, Employee.")
                else:
                    messages.error(request, "You are not an employee.")

        return response


custom_admin_site = CustomAdminSite()

admin.site.unregister(User)
custom_admin_site.register(User)
custom_admin_site.register(Employee)
