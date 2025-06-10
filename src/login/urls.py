from django.urls import path
from login.core.views.views import login, sucess
urlpatterns = [
    path('login/', login, name="login" ),
    path('sucess/', sucess, name="sucess")
]