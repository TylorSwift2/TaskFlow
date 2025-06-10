from django.contrib import admin
from django.urls import path, include
from login.core.views.views import login
urlpatterns = [
    path('login/', login, name="login" ),
]