from django.shortcuts import render
def home(request):
    """
    Render the home page.
    """
    return render(request, 't.html')