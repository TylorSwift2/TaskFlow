from django.urls import path # Removed unused imports
from painel.core.view.views import home
urlpatterns = [
    path('', home, name="home"),
    
]
