import os
import string
import random
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "initium.settings")
django.setup()
from django.contrib.auth.models import User
from employee.models import Employee


names = ["Vicky", "Ben", "Christine", "Jose"]


def generate_random_password():
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for _ in range(10))


for name in names:
    username = name.lower()

    password = generate_random_password()

    user = User.objects.create_user(username=username, password=password, is_staff=True)

    employee_status = random.choice(
        [status[0] for status in Employee.EmployeeStatus.choices]
    )

    employee = Employee.objects.create(
        user=user, name=name, is_employee=True, status=employee_status
    )

admin_username = "admin"
admin_password = "Initium1022"
User.objects.create_superuser(username=admin_username, password=admin_password)
