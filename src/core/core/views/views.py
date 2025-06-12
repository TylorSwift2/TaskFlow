from django.shortcuts import render, HttpResponse, redirect
from login import forms
from ...models import Pessoa
def home(request):
    return render(request, "home.html")
def registro(request):
    if request.method != "POST":
        return HttpResponse(300)
    if "user" not in request.POST  or "email" not in request.POST or "password1" not in request.POST or "password2" not in request.POST:
        return HttpResponse(300)
    form = forms.RegistrationForm(request.POST)
    if not form.is_valid():
        return HttpResponse(300)
    else:
       
        if request.POST["password1"] == request.POST["password2"]:
            senha = "password2"
            try:
                Pessoa.registrer(form.cleaned_data["user"], form.cleaned_data["password"])
            except Exception as error:
                print(f"error{error}")
                return HttpResponse(300)
            return redirect("home")