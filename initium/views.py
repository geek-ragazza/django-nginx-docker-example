from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View


class CustomLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse_lazy('login'))  

