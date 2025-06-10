from django.urls import path # Removed unused imports
from core.core.views.views import home
urlpatterns = [
    path('', home, name="home"),
]