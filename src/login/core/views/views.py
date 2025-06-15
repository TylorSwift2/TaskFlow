from django.shortcuts import render, HttpResponse, redirect
from login import forms
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from django.http import HttpResponseBadRequest
from core.models import Pessoa

# Create your views here.

def index(request):
    """
    Renders the index page with the registration form.
    """
    return render(request, "index.html", context={"form": forms.RegistrationForm})

def home(request):
    """
    Renders the home page with the registration form.
    """
    return render(request, "home.html", context={"form": forms.RegistrationForm})

def login(request):
    """
    Handles user login.
    If the request is POST, validates the login form, checks user credentials,
    and sets session variables if successful. Otherwise, shows error messages.
    If the request is GET, renders the login form.
    """
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["user"]
            password = form.cleaned_data["password"]

            try:
                pessoa = Pessoa.objects.get(user=username)
            except Pessoa.DoesNotExist:
                messages.error(request, "User not found")
                return render(request, "login.html", {'form': form})

            if check_password(password, pessoa.senha):
                request.session['user_id'] = pessoa.id
                request.session['user_name'] = pessoa.user
                messages.success(request, f'Welcome, {pessoa.user}!')
                return redirect('login:home')
            else:
                messages.error(request, "Incorrect password")
                return render(request, "login.html", {'form': form})
        else:
            return render(request, "login.html", {'form': form})

    else:
        form = forms.LoginForm()
        return render(request, "login.html", {'form': form})

def registrer(request):
    """
    Handles user registration.
    Only accepts POST requests. Validates required fields and form data,
    checks if passwords match and if the user already exists.
    Registers the user if all checks pass.
    """
    if request.method != "POST":
        return HttpResponseBadRequest("Invalid method!")

    if "user" not in request.POST or "password1" not in request.POST or "password2" not in request.POST:
        return HttpResponseBadRequest("Missing required fields!")

    form = forms.RegistrationForm(request.POST)
    if not form.is_valid():
        return HttpResponseBadRequest("Invalid data!")

    user = form.cleaned_data["user"]
    password1 = form.cleaned_data["password1"]
    password2 = form.cleaned_data["password2"]
    email = form.cleaned_data["email"]

    if password1 != password2:
        return HttpResponseBadRequest("Passwords must match!")

    if Pessoa.objects.filter(user=user).exists():
        return HttpResponse("User already exists", status=400)

    try:
        Pessoa.registrer(user, password1, email=email)
        return redirect('home')
    except Exception as e:
        return HttpResponse(f"Error registering user: {e}", status=500)

def sucess(request):
    """
    Handles a successful form submission.
    Only accepts POST requests and validates the login form.
    Renders the home page on success.
    """
    if request.method != "POST":
        # Error if accessed without POST
        return HttpResponse(300)
    
    form = forms.LoginForm(request.POST)
    
    if not form.is_valid():
        # Error if form is invalid
        return HttpResponse(300)
    
    # Print success and render
    print("Success")
    return render(request, "home.html")