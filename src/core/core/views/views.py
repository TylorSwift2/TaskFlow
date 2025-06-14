from django.shortcuts import render, HttpResponse, redirect
from login import forms
from ...models import Pessoa
def home(request):
    return render(request, "home.html")

