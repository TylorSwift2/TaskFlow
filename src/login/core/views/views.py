from django.shortcuts import render, HttpResponse, redirect
from login import forms
from core.models import Pessoa
# Create your views here.
def index(request):

    # Render the index page with the login form

    return render(request, "index.html", context={"form": forms.LoginForm})
def home(request):
    # Render the home page with the registration form

    return render(request, "home.html", context={"form": forms.RegistrationForm})

def registrer(request):

    if request.method != "POST":
        # Error if try to access without post
        return HttpResponse(300)
    
    # If the request is POST, we will try to register a new user
    # Create a form instance with the POST data
    # and validate it
    if "user" not in request.POST or "password" not in request.POST:
        
        # Error if the required fields are not present
        return HttpResponse(300)
    


    form = forms.RegistrationForm(request.POST)
    if not form.is_valid():
        # Error if try invalid formulary
        return HttpResponse(300)
    else:
        user = form.cleaned_data["user"]
        password = form.cleaned_data["password"]
        if Pessoa.objects.filter(user=user).exists():
            return HttpResponse("Usuário já existe", status=400)
        # Save the user in the database
            try:
                Pessoa.registrer( form.cleaned_data["user"], form.cleaned_data["password"])
                print("User registered successfully")
            except Exception as e:
            # Error if the user already exists
                print(f"Error registering user: {e}")
                return HttpResponse(300)
    return redirect('home')

def sucess(request):
    # Here I receive the form to do something
    
    if request.method != "POST":
        # Error if try to access without post
        return HttpResponse(300)
    
    form = forms.LoginForm(request.POST)
    
    if not form.is_valid():
        # Error if try invalid formulary
        return HttpResponse(300)
    
    # Print success and render
    
    print("Success")

    return render(request, "home.html")