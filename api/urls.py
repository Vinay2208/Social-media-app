from django.urls import path
from . import views



urlpatterns = [
    path('', views.home),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
]