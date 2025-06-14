from django.urls import path
from login.core.views.views import index, registrer, home
app_name = 'login'
urlpatterns = [
    path('login/', index, name="index" ),
    path('home/', home, name="home"),
    path('registrer/', registrer, name="registrer")
]