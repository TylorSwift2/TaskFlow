from django.contrib import admin
from django.urls import path
from core.core.views.views import home
urlpatterns = [
    path('', home, name="home" )
]