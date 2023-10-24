# forms.py
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Employee


class RegistrationEmployeeForm(forms.ModelForm):
    username = forms.CharField(max_length=150, label="Username")
    password1 = forms.CharField(widget=forms.PasswordInput, label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = Employee
        fields = ("name",)

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords do not match.")

        return cleaned_data

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data["username"],
            password=self.cleaned_data["password1"],
            is_staff=True,
        )

        employee = super().save(commit=False)
        employee.user = user
        if commit:
            user.save()
            employee.save()
        return employee
