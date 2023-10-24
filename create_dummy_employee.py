import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "initium.settings")
django.setup()
from django.contrib.auth.models import User
from employee.models import Employee
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

names = ["Vicky", "Ben", "Christine", "Jose"]


password = "Initium1022"

content_type = ContentType.objects.get_for_model(Employee)

permission, created = Permission.objects.get_or_create(
    codename="is_employee", content_type=content_type, name="Is Employee"
)


for name in names:
    username = name.lower()

    user = User.objects.create_user(username=username, password=password, is_staff=True)
    if name != "Jose":
        user.user_permissions.add(permission)

    employee = Employee.objects.create(
        user=user,
        name=name,
    )

admin_username = "admin"
admin_password = password
User.objects.create_superuser(username=admin_username, password=admin_password)
