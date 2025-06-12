from django.urls import path # Removed unused imports
from core.core.views.views import home, registro
urlpatterns = [
    path('', home, name="home"),
    path('registrer/', registro, name="registrer")
]