from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render

from .forms import RegistrationEmployeeForm
from .models import Employee


def register_employee(request):
    if request.method == "POST":
        form = RegistrationEmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegistrationEmployeeForm()
    return render(request, "employee/register.html", {"form": form})
