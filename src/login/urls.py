from django.urls import path
from login.core.views.views import index, registrer, home, login
app_name = 'login'
urlpatterns = [
    path('index/', index, name="index" ),
    path('home/', home, name="home"),
    path('registrer/', registrer, name="registrer"),
    path('login/', login, name="login")
]