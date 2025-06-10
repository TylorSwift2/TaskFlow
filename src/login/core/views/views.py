from django.shortcuts import render, HttpResponse
from login import forms

def login(request):
    return render(request, "index.html", context={"form" : forms.LoginForm})

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