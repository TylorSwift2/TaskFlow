from django.shortcuts import render, HttpResponse, redirect
from login import forms
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from django.http import HttpResponseBadRequest
from core.models import Pessoa

class AuthenticationService:
    """
    Handles authentication logic for users.
    """
    @staticmethod
    def authenticate(username, password):
        try:
            pessoa = Pessoa.objects.get(user=username)
            if check_password(password, pessoa.senha):
                return pessoa
        except Pessoa.DoesNotExist:
            return None
        return None

class RegistrationService:
    """
    Handles user registration logic.
    """
    @staticmethod
    def register(user, password1, password2, email):
        if password1 != password2:
            raise ValueError("Passwords must match!")
        if Pessoa.objects.filter(user=user).exists():
            raise ValueError("User already exists")
        return Pessoa.registrer(user, password1, email=email)

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
    """
   
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["user"]
            password = form.cleaned_data["password"]
            pessoa = AuthenticationService.authenticate(username, password)
            if pessoa:
                request.session['user_id'] = pessoa.id
                request.session['user_name'] = pessoa.user
                request.session['is_authenticated'] = True  # Adicione esta flag
                messages.success(request, f'Welcome, {pessoa.user}!')
                return redirect('login:home')
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid form data")
        return render(request, "login.html", {'form': form})
    else:
        form = forms.LoginForm()
        return render(request, "login.html", {'form': form})

def registrer(request):
    """
    Handles user registration.
    """
    if request.method != "POST":
        return HttpResponseBadRequest("Invalid method!")

    form = forms.RegistrationForm(request.POST)
    if not form.is_valid():
        return HttpResponseBadRequest("Invalid data!")

    user = form.cleaned_data["user"]
    password1 = form.cleaned_data["password1"]
    password2 = form.cleaned_data["password2"]
    email = form.cleaned_data["email"]

    try:
        RegistrationService.register(user, password1, password2, email)
        return redirect('home')
    except ValueError as ve:
        return HttpResponse(str(ve), status=400)
    except Exception as e:
        return HttpResponse(f"Error registering user: {e}", status=500)

def sucess(request):
    """
    Handles a successful form submission.
    Only accepts POST requests and validates the login form.
    Renders the home page on success.
    """
    if request.method != "POST":
        return HttpResponse(300)
    
    form = forms.LoginForm(request.POST)
    if not form.is_valid():
        return HttpResponse(300)
    
    print("Success")
    return render(request, "home.html")