from django.urls import path
from AppPortafolio import views


urlpatterns = [
    path('', views.home, name='Home')
]
