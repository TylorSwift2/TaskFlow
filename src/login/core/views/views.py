from django.shortcuts import render, redirect

def login(request):
    return render(request, "index.html")
def sucess(request):
    return render(request, "home.html")